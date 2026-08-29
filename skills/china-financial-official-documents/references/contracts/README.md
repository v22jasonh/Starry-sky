# 金融合同专项审核模块

本目录用于在通用合同审核方法论之上，对高频金融交易进行二次专业审查。

## 路由

- `BANK_CREDIT_REVIEW.md`：银行授信、借款、额度、流动资金贷款、固定资产贷款、循环授信等。
- `NPL_TRANSFER_REVIEW.md`：不良贷款、不良债权、债权资产包、批量转让、单户转让及其配套交割。
- `SPV_ASSET_DISPOSAL_REVIEW.md`：SPV受让、资产装入、委托管理、资产处置、回款归集、收益分配及退出安排。
- `CLAUSE_REDLINE_LIBRARY.md`：跨合同通用红线条款和标准修订语言。

## 使用顺序

1. 先读取上一级 `CONTRACT_REVIEW_METHODOLOGY.md`，确定审核立场、交易目标和风险偏好；
2. 再读取与合同类型对应的专项模块；
3. 需要逐条扫描时配合 `CONTRACT_REVIEW_CHECKLIST.md`；
4. 需要标准修订措辞时读取 `CLAUSE_REDLINE_LIBRARY.md`；
5. 涉及现行法律、监管或司法效力问题时继续调用 `SOURCE_MATRIX.md`、`LEGAL_COVERAGE_MATRIX.md` 和 `VALIDATION_CHECKLIST.md`。

专项模块不替代具体交易事实核验。合同名称不能决定法律性质，应以真实资金流、资产流、风险承担和控制权安排判断交易实质。
