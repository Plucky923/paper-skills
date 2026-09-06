# PaperSkills

面向系统研究论文的审查与改写 skills。按论文/venue/贡献类型 → 章节 → 段落 → 句子 → 词汇自上而下审查，并自下而上复核；每个单位都有可见 coverage 状态。自动识别段落作用，检查句间和段间逻辑；改写默认限于各原始段落内部，保留内容归属与论文格式，追求问题驱动、简洁、精确和技术含义保真。

Revise 默认只修具体问题，保留已经合格的原句；明显更优但非必要的表达单列为“可选写法”。缺少科学前提或证据时不补写、不擅自削弱结论，而是保留受影响的原文并指出缺口。要求只给正文时，正文之后仍保留一行 decision coverage 回执，并仅在必要时增加影响科学含义的最简问题提示。

## 从哪里开始

Review、Grill 和 Revise 使用同一套写作与逻辑标准与 [覆盖约定](skills/systems-paper-revise/references/coverage-contract.md)：Review 分别记录段落承诺的职责与实际交付，检查单一 reader obligation、段尾信息增量、相关工作的比较轴与 Root Cause；当一个 insight 声称同时产生多个主要结果时，还会逐条区分原文明示、文本可推出与 reviewer 脑补的因果边。Review 还把每个 finding 标为可直接修复、需作者澄清、需作者证据、外部阻塞或可选/不应用。Revise 先逐项完成所有安全修复，再自动用 Grill 的整轮提问方式询问当前可回答的作者项；收到回答后继续同一次 revision，而不是把待澄清项直接作为最终 `blocked`。Grill 区分不满意、作者意图、科学证据和真正的修改授权；三者的判断与衔接以 [共享约定](skills/systems-paper-revise/references/review-revise-contract.md) 为准。

| 要做什么 | 入口 |
| --- | --- |
| 审查指定材料，定位有逻辑问题的两句或两段，不改写原文 | [systems-paper-review](skills/systems-paper-review/SKILL.md) |
| 讨论论文逻辑与作者意图，保存中间结果和已确认决定 | [systems-paper-grill](skills/systems-paper-grill/SKILL.md) |
| 在各原始段落内部修改论文文字；明确要求时才起草或重组 | [systems-paper-revise](skills/systems-paper-revise/SKILL.md) |
| 查看系统论文写作要求及调研依据 | [写作要求调研](research/systems-paper-writing-requirements.md) |
| 检查 skill 行为与验收条件 | [合成回归测试与验收流程](benchmarks/README.md) |
| 使用当前获准的外部 benchmark | [外部评测使用说明](benchmarks/external/README.md) |
| 查看外部 benchmark 的任务依据与适用边界 | [外部 benchmark 准入依据](research/external-benchmark-admission.md) |

## 当前评测边界

ParaRev 用于受限段落改写；新输出需要人工盲评，并先检查技术含义是否保留。ParaReval 只用于校准对固定 A/B 输出的评价，不能直接给新改写评分。

现阶段没有获准使用的外部审稿 benchmark。外部数据不替代合成回归测试，也不能单独证明达到 OSDI、SOSP、EuroSys、ATC 或 ASPLOS 的写作要求。适用范围以 [admission.json](benchmarks/external/admission.json) 及准入依据为准。

## 目录职责

```text
skills/                   Review、Grill、Revise 三个自有 skills
benchmarks/
  fixtures/               原创合成回归案例
  external/               当前外部评测指南、准入策略与来源清单
    cache/                本地数据；Git 忽略
research/                 写作要求与准入依据
scripts/                  结构校验器与外部评测工具
tests/                    评测工具的确定性单元测试
```

准备和运行命令会按需创建 `benchmarks/external/work/` 与 `runs/`，两者均由 Git 忽略。

## 不调用模型的本地检查

在仓库根目录执行：

```bash
python3 -B scripts/validate_skills.py
python3 -B -m unittest discover -s tests
python3 -B scripts/external_benchmarks.py list
python3 -B scripts/external_benchmarks.py verify --source all --summary
```

前三条命令不要求下载语料；最后一条检查本地缓存，尚未下载时会报告缺失。下载、准备批次、模型调用及盲评步骤见外部评测使用说明；模型调用会消耗账户额度。

只将自有 skills、代码、合成案例、来源元数据、使用说明及适配所需许可证纳入 Git。第三方论文、人工标签、生成文本与运行日志留在被忽略的目录。实际论文的讨论记录保存在各论文项目中，不放进 skills 仓库。

## Review → Grill → Revise

Grill 就是“把这段话想表达的意思问清楚，并替你记下来”。你只需要提供原文或问题、回答和确认，不需要填写记录模板，也不需要管理状态。例如：

> 用 systems-paper-grill 和我讨论这段的因果关系，把讨论结果记录在这个论文项目里。

它会围绕具体疑点提问，将未解决的问题和确认的决定保存在 `paper-decisions.md`，但不改正文。讨论完后，你再要求 Revise 按记录修改。也可以不经过 Review，直接讨论某段原文。

在新任务中，可以说“在论文项目 `/你的论文路径` 中，按项目讨论记录 revise `manuscript.tex`”。三个 skills 使用同一查找约定：优先使用你指定的记录路径，否则读取已授权论文项目根目录的 `paper-decisions.md`；明确的论文项目中没有该文件就按零条历史继续。仅粘贴原文或项目归属不明时，skills 会询问记录路径，或者请你明确确认本次没有既有 decision history，不会擅自搜索其他项目或创建项目配置。记录按稳定 lineage 保存不可丢的完整版本；Grill 更新后会回读核对，你无需管理模板或状态。

1. Review 先清点全部授权单位，再按论文/贡献类型、章节、段落承诺职责与实际职责、单一义务与段尾信息增量、句子/句间关系、词汇位置逐层只读检查；对“一个 move 同时解决多个目标”的主张建立 source-grounded fan-out map，不能用 reviewer 自己补全的故事代替原文。组织、证据、语言和授权四个维度独立判断，正常单位也显示 `pass`，最后用 coverage receipt 对账。
2. 独立讨论时调用 systems-paper-grill，按问题依赖分轮澄清。它接收需作者澄清或作者证据的精确 finding，先确认共同改变的约束或边界，再确认每个目标的因果边和相应层次；获准记录时把每次实质变化保存为同一 lineage 下的完整版本，保留 finding/unit ID、原文锚点、resolution test、意图、证据、允许的修改，以及 `pending`、`confirmed`、`rejected`、`superseded` 状态。新的 pending 候选不会取代旧 confirmed head；只有确认 successor 时才在一次写入里建立双向接替链接。诸如“是不是应该放到 Challenge”属于待确认的放置假设，不自动授权拆段或移动；任何实质决定在写入并回读前都不能宣告完成或交还 Revise。
3. Revise 把 Review findings 当作主工作队列：先逐项落实直接可修且证据相容的修改，再对所有前置条件已满足的作者澄清/作者证据项自动发起一轮带建议的问题。此时 `pending clarification` 是等待回答的中间状态，不能输出最终 closure receipt；作者回答后自动恢复同一次修改。只有外部前提确实不可用，或作者明确拒绝、无法提供或确认不存在所需输入时，才能最终标为 `blocked`。未确认或被否决的建议不写入正文，证据缺口不靠措辞填补。
4. Review 和 Revise 每次都核算记录里的全部版本，派生 effective、applicable 和 executable 集合；只有 evidence-compatible、无冲突且对当前操作有权限的 confirmed head 能约束修改。Revise 完成修改后对完整授权范围重新运行同一层级检查，而不是只看改过的句子或相邻段落；每个原 finding 才最终标为 `closed`、`blocked`、`not applied` 或 `reopened`。输出同时以 `Unreviewed: 0` 和 `Unaccounted decisions: 0` 分别证明正文单位与决策历史均已核算。明确的语言问题可以跳过 Grill；单独请求 Review 不会自动改稿。

Systems Paper Grill 以 [mattpocock/skills 的 grilling 原文](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/SKILL.md) 为基础适配，保留问题依赖树、整轮提问、逐题建议、等待回答及最终确认。`grill-me` 本身只是调用 grilling 的入口。论文适配限定材料与证据范围、接入共享标准，并保存供 Revise 使用的讨论记录；不创建软件架构 ADR 或历史日志。来源与适配说明见 [grill-source.json](benchmarks/grill-source.json)，保留 MIT 许可证，运行时无需另装通用 grilling。
