# China Financial Official Documents Skill

中国金融业务全链条官方法律规范检索、效力分析与专业合同审核 Skill。

本项目采用 **Agent Skills** 结构：核心入口为 `SKILL.md`，详细资料按需放在 `references/`、`examples/` 等目录，便于 Agent 按“发现 → 激活 → 按需加载参考资料”的方式使用。

## Skill 入口

`skills/china-financial-official-documents/SKILL.md`

当前版本：**2.3.0**

## 适用范围

用于检索、核验和分析与中国金融业务相关的：

- 全国人大及其常委会、国务院及部委法律法规文件；
- 最高人民法院、最高人民检察院、各省高院及相关司法文件；
- 金融监管总局及原银保监会/银监会/保监会历史文件；
- 中国人民银行、证监会、外汇局；
- 财政、税务、市场监管、国资、公安、司法行政等机关文件；
- 民法典、公司、破产、仲裁、民诉执行、刑事、反洗钱、数据合规、跨境等衔接法域；
- 地方金融管理及地方司法规则；
- 专业金融合同审核、风险分级、修订建议和谈判底线。

## 合同审核能力

在通用合同审核方法论之外，v2.3.0 增加三个专项模块：

- **银行授信/借款合同审核**：提款条件、利率费用、MAC、交叉违约、提前到期、账户扣收、担保联动；
- **NPL不良债权转让协议审核**：资产清单、债权权属、从权利、交割、回款切割、瑕疵担保、执行程序衔接、数据转移；
- **SPV/资产处置协议审核**：交易实质、风险隔离、资产/资金/控制权、处置权限、回款瀑布、服务机构冲突、执行/破产衔接、退出清算。

同时提供 `CLAUSE_REDLINE_LIBRARY.md`，用于高频风险条款的标准修订语言和替代控制措施。

## 目录结构

```text
Starry-sky/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
└── skills/
    └── china-financial-official-documents/
        ├── SKILL.md
        ├── references/
        │   ├── SOURCE_MATRIX.md
        │   ├── LEGAL_COVERAGE_MATRIX.md
        │   ├── VALIDATION_CHECKLIST.md
        │   ├── OUTPUT_TEMPLATES.md
        │   ├── CONTRACT_REVIEW_METHODOLOGY.md
        │   ├── CONTRACT_REVIEW_CHECKLIST.md
        │   └── contracts/
        │       ├── README.md
        │       ├── BANK_CREDIT_REVIEW.md
        │       ├── NPL_TRANSFER_REVIEW.md
        │       ├── SPV_ASSET_DISPOSAL_REVIEW.md
        │       └── CLAUSE_REDLINE_LIBRARY.md
        └── examples/
            └── README.md
```

## 安装/使用

将整个 `skills/china-financial-official-documents/` 目录复制到 Agent 客户端所支持的 Skills 目录中。不同客户端的发现路径可能不同，但 Skill 本体保持自包含。

如平台支持 ZIP 导入，建议将 **`china-financial-official-documents` 目录本身**打包后导入，并保持其中 `SKILL.md`、`references/`、`examples/` 的相对路径不变。

## 设计原则

- 官方原文优先，第三方只作线索；
- 文件身份和现行效力分开核验；
- 机构改革不等于历史文件失效；
- 跨修法节点先建立时间轴；
- 核销/出表、税务损失与实体债权消灭严格区分；
- 实体法责任与执行程序追加依据严格区分；
- 合同审核先看交易结构，再看文字；
- 商业不利与法律无效严格区分；
- 静态清单只规定最低检索面，不能限制进一步扩展。

## 版本管理

采用 Semantic Versioning 风格：

- Major：核心方法或兼容结构发生不兼容变化；
- Minor：增加法域、合同专项模块、检索规则、参考资料或兼容性改进；
- Patch：文字、链接、示例和非实质性错误修订。

详见 `CHANGELOG.md`。

## 贡献

法规纠错、效力更新、历史机构沿革修订、新法域扩展、合同审核规则和红线条款优化均欢迎通过 Issue 或 Pull Request 提交。关键法规更新应尽量附官方来源，并说明是否存在修改、废止或新旧法衔接问题。

## License

MIT License。详见 `LICENSE`。
