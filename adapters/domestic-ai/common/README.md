# 国内 AI 通用版

版本：**2.5.0**

更新时间：**2026-10-27（Asia/Shanghai）**。法规复核记录为2026-10-03；全量时效复核未完成。

适用于支持“系统提示词 / 角色设定 + 文件上传 / 知识库”的国内大模型平台，例如千问、豆包、智谱以及其他具有类似能力的平台。

## 使用方法

1. 将 `SYSTEM_PROMPT.md` 的完整内容放入平台的系统提示词、角色设定、智能体指令或等效位置；
2. 将 `references/` 下的资料上传到平台知识库或智能体文件区；
3. 如平台支持按文件检索，保持原文件名和目录语义；
4. 使用前阅读 `LICENSE.txt` 和 `DISCLAIMER.md`。

## 知识库建议

优先上传全部 `references/` 文件。若平台存在数量或容量限制，最低建议保留：

- `SOURCE_MATRIX.md`
- `LEGAL_COVERAGE_MATRIX.md`
- `VALIDATION_CHECKLIST.md`
- `CONTRACT_REVIEW_METHODOLOGY.md`
- `CONTRACT_REVIEW_CHECKLIST.md`
- `OUTPUT_TEMPLATES.md`

涉及授信、NPL或SPV时再追加 `references/contracts/` 对应专项文件。

## 注意

不同平台对“系统提示词”“知识库”“智能体”的产品名称和界面可能变化。本目录不依赖某个平台专有格式，核心原则是：**提示词负责方法论，知识库负责参考资料，联网能力负责现行官方文件核验。**

## 本版正文库

先上传 `references/LAW_INDEX.md`、`references/LEGAL_MANIFEST.json`，再按业务上传 `references/laws/`。图片公式、PDF原件如平台不支持，可从官方链接查阅。
