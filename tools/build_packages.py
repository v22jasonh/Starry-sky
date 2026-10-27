"""Validate shared legal evidence and build deterministic release ZIPs (stdlib only)."""
from pathlib import Path
import argparse, hashlib, json, re, zipfile
ROOT=Path(__file__).resolve().parents[1]
NAME='china-financial-official-documents'
CORE=ROOT/'skills'/NAME
FOLDERS={'core':CORE,'claude':ROOT/'.claude/skills'/NAME,**{p:ROOT/'adapters/domestic-ai'/p for p in ('common','qwen','doubao','zhipu')}}
def digest(data):return hashlib.sha256(data).hexdigest()
def inventory(folder):return {p.relative_to(folder).as_posix():digest(p.read_bytes()) for p in folder.rglob('*') if p.is_file()}
def integer(s):
    digits=dict(zip('零一二三四五六七八九',range(10)));digits['〇']=0
    total=current=0
    for c in s:
        if c in digits:current=digits[c]
        else:total+=(current or 1)*{'十':10,'百':100,'千':1000}[c];current=0
    return total+current

def validate():
    config=json.loads((CORE/'VERSION.json').read_text(encoding='utf-8'))
    refs=inventory(CORE/'references');examples=inventory(CORE/'examples')
    manifest=json.loads((CORE/'references/LEGAL_MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['release_version']==config['version']
    assert config['legal_reviewed_on']==manifest['reviewed_on']
    assert config['full_review_complete']==manifest['full_review_complete']
    article_total=0
    for row in manifest['documents']:
        path=CORE/'references'/row['path'];text=path.read_text(encoding='utf-8')
        assert digest(path.read_bytes())==row['text_sha256'],path
        assert digest((ROOT/row['snapshot_path']).read_bytes())==row['source_sha256'],row['id']
        assert '\ufffd' not in text,path
        body=text.split('## 正文\n',1)[1]
        if row['article_count']:
            found=[integer(v) for v in re.findall(r'第([零〇一二三四五六七八九十百千]+)条\s',body)]
            assert found==list(range(1,row['article_count']+1)),row['id']
            article_total+=len(found)
        for target in re.findall(r'\]\(([^\s)]+)\)',text):
            if not re.match(r'https?://',target):assert (path.parent/target).exists(),(path,target)
        if row.get('image_sha256'):
            assert digest((CORE/'references/laws/images/vat_deduction_formula.png').read_bytes())==row['image_sha256']
    for row in manifest.get('supplemental_sources',[]):
        data=(CORE/'references'/row['path']).read_bytes()
        assert digest(data)==row['sha256'],row['path']
        assert data==(ROOT/row['snapshot_path']).read_bytes(),row['path']
        if row.get('extracted_path'):
            assert digest((CORE/'references'/row['extracted_path']).read_bytes())==row['extracted_sha256']
    for review in manifest.get('topic_reviews',[]):
        for relative in review['paths']:
            topic=CORE/'references'/relative
            text=topic.read_text(encoding='utf-8')
            assert '\ufffd' not in text,topic
            for target in re.findall(r'\]\(([^\s)]+)\)',text):
                if not re.match(r'https?://',target):assert (topic.parent/target).exists(),target
    for platform,folder in FOLDERS.items():
        meta=json.loads((folder/'VERSION.json').read_text(encoding='utf-8'))
        assert meta==dict(config,platform=platform),platform
        assert inventory(folder/'references')==refs,platform+' reference mismatch'
        assert inventory(folder/'examples')==examples,platform+' example mismatch'
        entry=folder/('SKILL.md' if platform in ('core','claude') else 'SYSTEM_PROMPT.md')
        text=entry.read_text(encoding='utf-8')
        assert 'references/LAW_INDEX.md' in text and 'references/LEGAL_MANIFEST.json' in text,platform
        assert 'references/BANK_ECL.md' in text and 'references/BANK_WRITEOFF.md' in text,platform
        if platform in ('core','claude'):
            assert f'version: "{config["version"]}"' in text,platform
            assert f'updated: "{config["updated"]}"' in text,platform
    print(json.dumps({'version':config['version'],'platforms':len(FOLDERS),'references_per_platform':len(refs),'documents':len(manifest['documents']),'complete_texts':sum(d['fulltext_complete'] for d in manifest['documents']),'articles':article_total,'full_review_complete':manifest['full_review_complete']},ensure_ascii=False))
    return config

def build(platform,config):
    folder=FOLDERS[platform];out=ROOT/'dist'/f'{NAME}-{platform}-v{config["version"]}.zip'
    out.parent.mkdir(exist_ok=True)
    expected={}
    stamp=tuple(map(int,config['updated'].split('-')))+(0,0,0)
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(p for p in folder.rglob('*') if p.is_file()):
            assert not path.is_symlink(),path
            arc=folder.name+'/'+path.relative_to(folder).as_posix();data=path.read_bytes()
            info=zipfile.ZipInfo(arc,stamp);info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,data);expected[arc]=digest(data)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None,out
        assert {n:digest(z.read(n)) for n in z.namelist()}==expected,out
    checksum=digest(out.read_bytes())
    Path(str(out)+'.sha256').write_text(checksum+'  '+out.name+'\n',encoding='ascii')
    print(out.name,len(expected),'files',checksum)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');parser.add_argument('--group',choices=['all','skills','domestic'],default='all');args=parser.parse_args()
    config=validate()
    if not args.check:
        for platform in FOLDERS:
            if args.group=='skills' and platform not in ('core','claude'):continue
            if args.group=='domestic' and platform in ('core','claude'):continue
            build(platform,config)