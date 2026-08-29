# China Financial Official Documents Skill

中国金融业务全链条官方法律规范检索、效力分析与专业合同审核 Skill。

本项目采用 **Agent Skills** 结构：核心入口为 `SKILL.md`，详细资料按需放在 `references/`、`examples/` 等目录，便于 Agent 按“发现 → 激活 → 按需加载参考资料”的方式使用。

## Skill 入口

`skills/china-financial-official-documents/SKILL.md`

当前版本：**2.2.0**

## 适用范围

用于检索、核验和分析与中国金融业务相关的：

- 全国人大及其常委会、国务院及部委法律法规文件；
- 最高人民法院、最高人民检察院、各省高院及相关司法文件；
- 金融监管总局及原银保监会/银监会/保监会历史文件；
- 中国人民银行、证监会、外汇局；
- 财政、税务、市场监管、国资、公安、司法行政等机关文件；
- 民法典、公司、破产、仲裁、民诉执行、刑事、反洗钱、数据合规、跨境等衔接法域；
- 地方金融管理及地方司法规则；
- 借款/授信、担保、债权转让、不良资产、SPV、资产管理、催收、债务重组等合同的专业审核。

## 合同审核能力

v2.2.0 新增完整合同审核方法论，不采用“逐条挑错”的低效模式，而是先重建交易，再审核条款。

核心框架：

**交易与法律结构 → 合同结构与完整性 → 风险分配与谈判位置 → 履约、证据与争议执行**

支持：

- 交易结构识别；
- 缺失条款发现；
- 法律/商业/运营/文本四类风险分类；
- Critical / High / Medium / Low 风险分级；
- 逐条修改建议；
- 谈判底线；
- 替代控制措施；
- 数字、利率、期限、公式复核；
- 主合同与担保、附件、资产清单等跨文件一致性检查；
- 管理层红线版合同审核简报。

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
        │   ├── CONTRACT_REVIEW_METHODOLOGY.md
        │   ├── CONTRACT_REVIEW_CHECKLIST.md
        │   └── OUTPUT_TEMPLATES.md
        └── examples/
            └── README.md
```

## 安装/使用

将整个 `skills/china-financial-official-documents/` 目录复制到 Agent 客户端所支持的 Skills 目录中。不同客户端的发现路径可能不同，但 Skill 本体保持自包含。

如平台支持 ZIP 导入，建议将 **`china-financial-official-documents` 目录本身**打包后导入，并保持其中 `SKILL.md` 与 `references/`、`examples/` 的相对路径不变。

## 设计原则

- 官方原文优先，第三方只作线索；
- 文件身份和现行效力分开核验；
- 机构改革不等于历史文件失效；
- 跨修法节点先建立时间轴；
- 核销/出表、税务损失与实体债权消灭严格区分；
- 实体法责任与执行程序追加依据严格区分；
- 合同审核先理解交易结构，再修改文字；
- 同时发现错误条款和缺失条款；
- “对我方不利”不自动等于“违法无效”；
- 静态清单只规定最低检索面，不能限制进一步扩展。

## 版本管理

采用 Semantic Versioning 风格：

- Major：核心方法或兼容结构发生不兼容变化；
- Minor：增加法域、检索规则、合同审核方法或参考资料；
- Patch：文字、链接、示例和非实质性错误修订。

详见 `CHANGELOG.md`。

## 贡献

法规纠错、效力更新、历史机构沿革修订、新法域扩展、合同审核方法改进均欢迎通过 Issue 或 Pull Request 提交。关键法规更新应尽量附官方来源，并说明是否存在修改、废止或新旧法衔接问题。

## License

MIT License。详见 `LICENSE`。
