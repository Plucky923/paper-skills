# Skill 与论文决策如何演化：现有做法调研

核验日期：2026-09-06

## 结论

现有实践把两种“进化”明确分开：

1. **Skill 源码进化**是一次受控的软件发布。规则、引用文件和脚本在 Git 中修改；候选版本经过结构校验和行为回归测试后，作为一个完整版本发布或安装。运行时可以指向最新版本，也可以固定在已验证版本上。
2. **Skill 产生的决策进化**是项目状态的演化。旧决定不被重写成“仿佛一开始就这样”；新的完整决定通过稳定 ID 和 `supersedes` / `superseded by` 关系接替旧决定。待确认候选不会提前取代当前已确认决定，被拒候选也保留为历史。

两者之间应只有受控反馈关系：真实使用暴露缺陷，缺陷变成可复现 fixture，fixture 驱动一个窄小的 skill 修改；某篇论文的具体决定本身不能自动上升为所有论文都必须遵守的新规则。OpenAI 当前的 skill-creator 也要求根据真实使用或已展示的失败迭代，并偏好窄修复而不是为每个例子累积普遍规则；结构 validator 不能证明 skill 做出了正确判断，行为验证应检查可观察结果而不是匹配固定措辞。该结论来自本机当前系统 skill `~/.codex/skills/.system/skill-creator/SKILL.md`，并与 OpenAI 关于测试触发行为、保持单一职责和显式输入输出的公开建议一致。[OpenAI Build skills](https://developers.openai.com/codex/skills)

因此，本项目最合适的模型不是“把 `paper-decisions.md` 继续原地改成最新状态”，也不是“每轮 Grill 写一份聊天日志”，而是：

- `PaperSkills` 仓库继续用 Git 提交、冻结的 baseline/candidate skill tree、fixtures、hard gates 和 acceptance record 演化；
- 每篇论文继续只有一个 `paper-decisions.md`，但文件内部改成**不可丢历史的版本化决策账本**；
- Review 和 Revise 每次读取并核算全部决策版本，只让当前有效、已确认且证据兼容的版本约束正文。

## 调研范围与证据边界

本次读取了以下第一方材料：

- OpenAI 的 Codex/ChatGPT skill 作者文档、Agent Skills 开放规范和 Skills API reference；
- Anthropic 的 Skill API 与 enterprise 分发/版本控制文档，用作另一个 Agent Skills 实现的交叉核验；
- 当前安装的 `skill-creator`、`domain-modeling`、`teach`、`wayfinder`、`grill-with-docs` 等 skill 源码；
- mattpocock/skills 的公开源码；
- Michael Nygard 的原始 ADR 说明与 MADR 模板；
- 本仓库现有 benchmark、validator、Git 历史和当前论文 decision-record 契约。

这里的“现有做法”只指上述已核验实现，不代表整个 skill 生态都采用同一机制。OpenAI Skills API 的托管版本对象与本地 Codex skill 文件夹是不同部署面；下文只把其不可变版本和活动指针作为可借鉴的发布机制，不声称本仓库已经使用该 API。

## 1. Skill 源码如何进化

### 1.1 本地 skill 是可版本控制的完整目录

Agent Skills 开放规范把 skill 定义为一个含 `SKILL.md` 和可选 `scripts/`、`references/`、`assets/` 的目录，并明确把它描述为可移植、可版本控制的文件夹。规范允许在自定义 metadata 中写 `version`，但没有定义跨实现通用的升级、迁移或决策历史协议；metadata 版本号本身不能替代 Git 历史或行为验证。[Agent Skills overview](https://agentskills.io/)、[format specification](https://agentskills.io/specification)

OpenAI 的本地 Codex 文档说明：Codex 会自动检测 skill 文件变化；未出现时重启。它还要求 skill 聚焦一个任务、用明确输入输出写步骤，并用测试 prompt 验证 description 的触发行为。[OpenAI Build skills](https://developers.openai.com/codex/skills)

这意味着本地 skill 的“进化单位”应是完整目录的一次可审查修改，而不是运行中的模型悄悄改写自身提示词。Git 负责来源、diff、review 和 rollback；测试负责判断新版本是否真的改善行为。

### 1.2 托管实现采用不可变完整版本和显式活动指针

OpenAI Skills API 把新 skill version 定义为不可变版本，并把“更新 skill”定义为移动默认版本指针；`latest_version` 与 `default_version` 是不同字段。[OpenAI Skills API](https://developers.openai.com/api/reference/go/resources/skills)

Anthropic 的实现给出更完整的部署纪律：新版本是完整快照而不是 delta；开发测试可用 `latest`，生产应固定精确版本；新版本须跑完整 eval，保留上一已知良好版本用于回滚，并可用 checksum 和签名 commit 验证完整性。[Anthropic Skills guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide)、[enterprise distribution and version control](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)

跨实现共同点是：

- 发布一个新版本，不覆盖旧版本；
- 一个版本是完整可执行快照，不依赖隐式 delta 回放；
- “最新”与“当前允许生产使用”是两个概念；
- promotion、rollback 和 provenance 都是显式操作。

### 1.3 本仓库已经具备正确的 skill 演化骨架

本仓库从 `2862b45` 到当前 `d411793` 的 Git 历史显示，三个 paper skills 通过连续的窄提交演化；最近几次修改都同时更新相应 reference、fixture、validator 或 unit test。现有 [benchmark protocol](../benchmarks/README.md) 已要求：

- 冻结不可变 baseline 和 candidate skill tree；
- 每个候选调用使用新上下文并保持 A/B 盲测；
- 先过越权、造事实、破坏语义等 hard gates，再比较质量；
- 候选不能低于 baseline；
- 接受前冻结 tree digest、环境、分数、访问记录和 failure closure。

这比在 `SKILL.md` frontmatter 手工增加一个版本号更强。版本号能命名版本，但上述证据链才能说明为什么应推广该版本。

## 2. 决策如何逐渐演化

### 2.1 ADR 模式：保留旧决定，用新决定接替

Nygard 的原始 ADR 做法要求编号单调递增、不复用；决定被反转时保留旧记录，把它标为 `superseded`，并指向替代记录。原因是旧决定曾经在当时上下文中有效，其动机仍是理解当前状态所需的历史证据。[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

MADR 的当前模板同样区分 `proposed`、`rejected`、`accepted`、`deprecated` 和 `superseded by ADR-0123`，并保留决定背景、备选项、结果和确认方式。[MADR template](https://github.com/adr/madr/blob/develop/template/adr-template.md)

mattpocock 的 `domain-modeling` 采用轻量版：ADR 顺序编号，状态可为 `proposed | accepted | deprecated | superseded by ADR-NNNN`，在值得记住时保存 rejected alternatives。[mattpocock ADR format](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/ADR-FORMAT.md)

共同约束不是固定模板，而是三件事：旧记录仍可读取，接替关系可机器和人追踪，当前有效决定可从历史中无歧义地求出。

### 2.2 teach 模式：知识加深时新增记录，不删除旧理解

mattpocock 的 `teach` skill 把 learning record 视为教学领域的 ADR。后续理解纠正或深化早期理解时，创建新的顺序记录，并把旧记录标为 `superseded by LR-NNNN`；它明确认为理解如何演化本身就是有价值的信号。[Learning Record Format](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md)

这与论文 Grill 最相似：作者的意图、证据认识和允许的编辑边界会随着讨论逐渐变清楚。只保留最终措辞会丢掉被拒解释、曾缺失的证据和决定为何改变；保存逐轮聊天又会把大量无效过程混成权威。合适粒度是“每个实质性状态变化一个短的决策版本”。

### 2.3 Wayfinder 模式：当前索引与历史明细分离

`wayfinder` 把一个长期决策过程存成 map 和 decision tickets。map 只是低分辨率索引，每个决定的完整内容只存在于一个有稳定身份的 ticket；答案写入 resolution comment，ticket 关闭后 map 只追加一行链接。待解决、已决定、尚无法精确表述和超出范围的状态分开表示。[Wayfinder source](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

这个模式说明“方便读取的当前视图”不应成为另一份会漂移的真相。若 `paper-decisions.md` 增加 current-head 索引，它只能是同一文件内由历史条目派生并可校验的索引；每个决定版本的正文仍只存一处。

### 2.4 可变当前视图与不可丢历史可以并存

已核验 skills 也会原地更新真正的当前投影。例如 `domain-modeling` 会即时修订 `CONTEXT.md` 的规范术语，`teach` 会在使命变化时更新 `MISSION.md`，但同时新增 ADR 或 learning record 保存为什么改变。

所以，以下两种写法用途不同：

- **当前投影**回答“现在采用什么”；可以更新，但必须能从记录核对；
- **历史记录**回答“曾考虑什么、为何改变”；核心内容不应被新结论覆盖。

本次调研开始时的论文 decision record 把二者混在一起：它明确要求“current-state record”、不留日期/版本/变更记录，并把 superseded decision 原地更新。这会保留当前答案，却无法证明决定如何逐渐形成，也无法让 Review/Revise 核算所有历史状态。该问题现已按本报告的版本链建议在 [decision-record 契约](../skills/systems-paper-grill/references/decision-record.md) 中修正。

## 3. 建议用于 PaperSkills 的具体模型

### 3.1 一个文件、多个不可丢的完整快照

仍使用作者授权项目中的一个 `paper-decisions.md`。每个逻辑问题拥有稳定 lineage，例如 `D7`；每次实质性变化产生完整版本 `D7.v1`、`D7.v2`，而不是在旧正文中覆盖答案，也不是只记差异。

每个版本至少包含：

- version ID 与 lineage；
- status：`pending | confirmed | rejected | superseded`；
- `proposes replacement for`、`supersedes`、`superseded by` 中适用的关系；
- source Review finding/unit IDs 和原文 anchor；
- 完整的当前问题、作者决定、理由、allowed edit；
- evidence state 与具体依据；
- resolution test；
- confirmation basis。

“完整快照”让 Review/Revise 读取一个有效版本即可知道当前决定；版本链同时保留演化过程，不要求模型把多段 delta 拼成最终含义。

### 3.2 状态转换

建议采用下列状态语义：

```text
没有旧决定
  -> pending candidate
  -> confirmed | rejected

已有 confirmed D7.v1
  -> pending D7.v2 proposes replacement for D7.v1
     D7.v1 继续有效
  -> D7.v2 confirmed
     同一次写入中：D7.v1 -> superseded by D7.v2
                   D7.v2 -> confirmed, supersedes D7.v1
  -> D7.v2 rejected
     D7.v1 继续有效；D7.v2 留作 rejected 历史
```

关键点是：

- 新的 pending 版本不能提前让旧 confirmed 版本失效；
- 只有作者确认的新版本可以 supersede 旧版本；
- rejected 和 superseded 是历史终态，不能原地复活；若重新考虑，创建新版本；
- 后续版本必须是该 lineage 的完整有效快照，包括仍保留的旧约束；
- 只允许修改旧版本的 lifecycle/link metadata 来补上双向接替关系，旧版本的问题、决定、理由、证据和确认正文保持不变；
- evidence 变为 missing/conflicting 或 anchor 不再匹配时，Review/Revise 报告冲突，不把“作者曾确认”当成事实可写入正文。

### 3.3 全历史消费与 coverage receipt

Review 和 Revise 每次必须先完整读取授权记录并构造四个集合：

1. all versions：所有 `pending`、`confirmed`、`rejected`、`superseded` 版本；
2. effective heads：没有被新 confirmed 版本接替的 confirmed 版本；
3. applicable heads：对当前 manuscript scope、anchor 和请求适用的 effective heads；
4. executable heads：同时 evidence-compatible、无冲突且允许当前动作的 applicable heads。

只有第 4 集可以约束实际修改。其他集合仍必须出现在核算中，以防重新提出 rejected 方案、恢复 superseded 结论、误用 pending 内容或漏掉冲突。

每次 Review/Revise 的 decision coverage receipt 应报告：

- record identity/path；
- 读取的全部 version IDs；
- 各 status 数量；
- effective/applicable/executable IDs；
- 不适用项及理由；
- 冲突或断链；
- `Unaccounted decisions: 0`。

即使用户要求只返回修改后正文，也保留一行最小 receipt。这里的零表示所有已读取版本都已分类，不表示所有决定都有效或都被应用。

### 3.4 Grill 的持久化完成门

Grill 可以在一次回答逐渐清楚时连续产生 pending 版本，但每个版本只在作者输入造成实质性状态或内容变化时创建；重复确认和纯措辞变化不创建新版本。

对于任何实质性决定：

1. 找到或取得授权的 record path；
2. 读取全历史和当前有效 head；
3. 追加新完整版本，必要时原子更新旧 head 的接替 metadata；
4. 回读新版本、旧 head 和未相关条目；
5. 验证作者回答、双向 link、证据边界和未相关内容均保留；
6. 只有此后才能宣布 standalone Grill 完成，或把控制权交还 embedded Revise。

明确论文项目但记录尚不存在时，报告历史为零并创建首个实质性版本。只有粘贴文字或归属不明时，必须先取得 path，或由作者明确确认本次无历史记录；不能把决定永久留在 chat-only 状态并声称流程完成。

### 3.5 Skill 自身的升级门

把新契约加入三个 skills 时，应沿用本仓库已有演化机制：

1. 先冻结当前 `d411793` 加现有工作树为 candidate 的真实基线边界，保留用户未提交修改；
2. 新增至少三类 cold-start fixtures：历史全量核算、confirmed 被 pending candidate 挑战但仍有效、confirmed successor 原子接替旧版本；
3. 再加入 rejected candidate、断链/conflict、prose-only 最小 receipt、Grill 未持久化不得完成等负例；
4. validator 检查状态词、关系字段、必读路由、receipt marker 和 fixture schema，但不把字符串存在当成行为正确；
5. 对冻结 baseline/candidate 运行隔离的行为比较，保留 hard-gate 与 failure-closure 证据；
6. 通过后同步安装完整三个 skill 目录，比较字节或 digest，并在新上下文做真实 smoke test。

这条链把一次具体论文讨论转化为可复现的产品缺陷，再把窄修复推广到 skill；它不会让某篇论文的领域决定污染通用写作规则。

## 4. 不建议采用的做法

- **仅依赖 Git 找旧决定。** Git 能恢复文件历史，但 Review/Revise 不应为每次论文操作重放 repository history；未提交记录、移动文件和非 Git 项目也会失效。
- **把旧 entry 全文原地改成最新答案。** 当前阅读方便，但 accepted/pending/rejected 的演化证据消失。
- **新 pending 一出现就 supersede 旧 confirmed。** 这会让尚未获作者确认的建议改变正文约束。
- **只追加 delta。** 历史完整，却迫使模型回放所有 delta 才能确定当前含义，容易漏字段和误合并。
- **为每轮对话建版本。** 这会把 transcript 噪声当成 decision history；版本触发应是实质性状态、含义、证据或 edit-authority 变化。
- **让 skill 自动吸收个案。** 没有 fixture、scope 分析和 regression gate 的“学习”会把局部偏好升级成全局绝对规则。
- **用 changelog 代替测试。** changelog 能说明声称改了什么，不能证明触发、判断、权限和证据边界仍正确。

## 5. 最终建议

采用“双版本链”：

- **Skill 链**：Git commit / frozen tree → structural validation → isolated behavioral fixtures → acceptance record → installed bundle verification；
- **Decision 链**：stable lineage → immutable full snapshots → explicit lifecycle and supersession links → derived effective head → mandatory all-history coverage receipt。

这个设计同时满足“decision 会逐渐进化”和“Review/Revise 不漏掉任何历史决定”。它借鉴现有 skill/ADR 的成熟部分，但比上游 `grill-with-docs` 更严格：上游只持久化术语和少量 ADR，不提供论文级全问题账本、证据状态、原文锚点、全历史消费或覆盖回执。[既有上游调研](grill-upstream-workflow.md)

实现前不需要再选择多文件 ADR、issue tracker 或数据库；对当前三-skill 工作流，一个授权的 Markdown 账本足够。需要锁定的新语义只有一项：**每次实质性演化生成完整新版本；pending successor 不取代旧 confirmed head，只有 confirmed successor 才以双向链接原子接替。**

实施状态：上述语义已落实到三个 skills、记录模板、共享工作流与覆盖契约，并由新增的全历史、接替链和冲突/prose-only 三类 fixtures 覆盖。结构校验和单元测试能证明契约、路由与 fixture 完整性；完整 baseline/candidate 盲评仍按 benchmark acceptance 流程单独执行，不能由这些确定性检查替代。
