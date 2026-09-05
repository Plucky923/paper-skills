# Grill 上游工作流与文档证据

## 核验范围

本次直接读取 mattpocock/skills 的 GitHub 页面、GitHub Git Trees API 与 raw 源文件。API 对 `main` 返回的 SHA 为 `3cca18b368ae95cdbdebbff572ccafa662551015`，且 `truncated: false`；因此本次核验时的当前上游恰好等于本项目指定的固定 commit，没有两个不同版本可供比较。下文源码链接均固定到该 commit，避免把未来 `main` 当成本次结果。[当前树 API](https://api.github.com/repos/mattpocock/skills/git/trees/main?recursive=1)、[固定版本](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015)

全文读取范围包括四个 `SKILL.md`、四个 `agents/openai.yaml`、domain-modeling 的两个格式文件、setup 的 `SKILL.md` 和 `domain.md`、上游关于 setup 软硬依赖的 ADR，以及 domain-modeling / grill-with-docs 的一方解释文档。本文只研究这些源码的指令含义，未实际运行交互访谈，也未把本地安装添加的 metadata 当成上游原文件。

## 四个技能的分工与配置

| 技能 | 上游实际内容 | 调用配置 |
| --- | --- | --- |
| grill-me | 仅转调 `grilling` 的入口；没有自己的文档记录规则。[源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grill-me/SKILL.md) | frontmatter 为 `disable-model-invocation: true`；上游 YAML 也有 `allow_implicit_invocation: false`。[YAML](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grill-me/agents/openai.yaml) |
| grilling | 实际问答协议：按设计树与当前可回答的问题前沿分轮追问。[源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/SKILL.md) | 有自然语言触发 description；YAML 只有界面名称与简述，没有关闭隐式调用的 policy。[YAML](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/agents/openai.yaml) |
| grill-with-docs | 仅要求分别调用 `grilling` 和 `domain-modeling`；是组合入口。[源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs/SKILL.md) | 同 grill-me：frontmatter 禁止模型自行调用，YAML 禁止隐式调用。[YAML](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs/agents/openai.yaml) |
| domain-modeling | 主动澄清领域概念，即时维护词汇表，择要提出 ADR；讨论术语、编辑 CONTEXT 或 ADR 都是其触发范围。[源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md) | YAML 只有界面信息，没有关闭隐式调用的 policy。[YAML](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/agents/openai.yaml) |

这些是不同职责的入口、问答协议与文档纪律，不是三个互相替代的 grill 版本。单装 grill-with-docs 而缺少两个依赖，会缺失它要求的行为；一方解释文档也明确指出依赖未加载或仅加载 grilling 会造成访谈进行而没有文档落盘。[grill-with-docs 解释文档](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/docs/engineering/grill-with-docs.md)

## 访谈、确认与写入时机

grilling 把决策组织成依赖树：一轮只问前提已经确定的问题，每题编号并给建议答案；等待用户回答后重算下一轮。环境事实交给子代理调查，能独立推进的问题继续问，依赖未查明事实的问题等待。决策交由用户回答；前沿为空代表所有分支已访问，并且在用户确认达成共同理解前不能据此行动。这是访谈协议的整体确认要求。[grilling 源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/SKILL.md)

domain-modeling 同时明确要求已解决的术语立即写入 `CONTEXT.md`，不能攒到最后。一方文档也把边问边写定义为 grill-with-docs 的设计行为。因此源码组合应理解为：访谈期间可以记录已经澄清的词汇，最终共同理解确认约束后续落实方案；不能把整体确认句解释成禁止访谈中一切文档写入。源码没有规定“每个词条都另做一次写盘审批”。[domain-modeling 源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md)、[组合技能解释](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/docs/engineering/grill-with-docs.md)

对 ADR，指令使用“提出创建”而不是把每个决策直接记入；一方解释文档明确写成 offered, not assumed。源码没有完整的逐 ADR 审批状态机，不能额外推导固定确认轮数或强制审批模板。[domain-modeling 解释文档](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/docs/engineering/domain-modeling.md)

## 固定文件、格式与内容边界

默认单领域项目采用根目录 `CONTEXT.md` 与 `docs/adr/`。只在第一条术语解决或第一个 ADR 需要出现时创建，不预先建空文件。根目录若有 `CONTEXT-MAP.md`，先按地图找到当前相关领域；各领域拥有自己的 `CONTEXT.md` 与 `docs/adr/`，系统级 ADR 仍可位于根下 `docs/adr/`。话题属于哪个领域不明确时才询问。[domain-modeling 源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md)、[CONTEXT 格式](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/CONTEXT-FORMAT.md)

词汇表模板是领域名称、一两句领域介绍、`Language` 下的规范术语及其一两句定义，并用 `_Avoid_` 标明弃用同义词。定义解释概念是什么，只收入本项目领域特有概念；排除一般编程概念。自然形成分组时可以增加小标题。`CONTEXT.md` 明确不得含实现细节、规格或草稿笔记，不能当作完整需求记录。[CONTEXT 格式](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/CONTEXT-FORMAT.md)、[内容边界](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md)

ADR 文件名是 `0001-slug.md`、`0002-slug.md` 等；扫描现存最大编号后加一。最低模板只有简短标题，以及一至三句话写清背景、决定和理由。Status frontmatter、Considered Options、Consequences 都是按价值选用，非强制；状态可以表达 proposed / accepted / deprecated / superseded。不是每次会话按日期生成日志。[ADR 格式](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/ADR-FORMAT.md)

只有三个条件同时成立才提出 ADR：逆转代价明显、后人没有背景会感到意外、确实比较过可行替代方案并有取舍。架构形态、领域集成方式、锁定成本高的技术、所有权与范围边界、偏离常见方案的选择、代码看不出的约束、非显然的弃用方案是可能合格的例子；并不是这些主题一出现就必写 ADR。[ADR 条件与示例](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/ADR-FORMAT.md)

## 让文档真正影响后续理解的规则

domain-modeling 要求即时指出用户用语与既有词汇表的冲突，拆开含糊或多义概念，设计具体边界场景检验概念关系，并用代码核对用户关于现有行为的描述。术语和代码不符时指出矛盾，而不是静默选择一边。这些主动校验与写文件同属于该技能职责。[主动建模规则](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md)

跨会话发现链来自独立的 setup 技能：它在项目现存 `CLAUDE.md`（优先）或 `AGENTS.md` 中加入 `Agent skills` 的 Domain docs 指针，并写 `docs/agents/domain.md`；若两者均没有才让用户选择创建哪个。setup 要先展示配置草案供用户修改，再写入，已有块原地更新并保留周围用户内容。这个确认属于 setup 的配置写入流程，不能移植成每次 grill 都必须先安装或重新配置。[setup 源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/setup-matt-pocock-skills/SKILL.md)

`docs/agents/domain.md` 的种子模板规定消费者探索前先读根 CONTEXT 或地图指向的相关 CONTEXT，以及触及领域的 ADR；文档不存在时静默继续，不要求预先创建。后续 issue 标题、重构提议、假设、测试名称采用词汇表规范术语，避免 `_Avoid_` 同义词；与 ADR 冲突必须显式指出，并说明为何值得重开讨论。由此形成“项目入口指针 → 消费规则 → 词汇/决策文档 → 后续输出约束”的链条。[消费者模板](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/setup-matt-pocock-skills/domain.md)

不能声称 grill 的前置条件是 setup：domain-modeling 自身允许无文档起步，上述消费者模板也允许文档缺失；上游 ADR 进一步区分必须有配置才能工作的技能与仅借文档改善输出的软依赖技能，反对无区别添加 setup 前置要求。[软硬依赖 ADR](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md)

## 没有被该工作流自动解决的部分

四个技能目录的完整树只含 `SKILL.md`、`agents/openai.yaml`，以及 domain-modeling 的两个 Markdown 格式文件；没有脚本、hook、数据库或自动同步程序。该判断限于这四个目录及其上述依赖，不能扩张成整个仓库没有其他脚本。setup 自己也明确声明是提示词驱动，非确定性脚本。[完整固定树 API](https://api.github.com/repos/mattpocock/skills/git/trees/3cca18b368ae95cdbdebbff572ccafa662551015?recursive=1)、[setup 源码](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/setup-matt-pocock-skills/SKILL.md)

该组合没有规定覆盖所有问题的决策台账，也没有问题 ID、原文锚点、证据状态或每项答案通向规格/工单/测试的追踪。除了已解决术语和满足门槛的 ADR，其他决定留在会话中；一方解释文档承认这一缺口，建议接续同一会话生成 spec 并对照回答核查。它也承认模型可能漏加载 domain-modeling，导致访谈正常而文档缺失。本文没有独立验证这些失效的发生概率，也不把技能文本的要求当成运行时保证。[记录边界及已知失败](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/docs/engineering/grill-with-docs.md)

## 与当前论文适配的对照

以下是本项目的论文适配，与上游规定分开说明。

- **提问主干已经保留。** 当前入口保留依赖树、整轮问题与建议、等待回答、重新计算下一轮。论文适配将查证限制在授权材料内，并允许明确记录证据阻塞。[本地入口](../skills/systems-paper-grill/SKILL.md)
- **记录范围有意不同。** 本地使用单一 paper-decisions.md，保存待确认事项、已确认决定和否决项，还保留原文定位与证据依据。这满足作者希望保留中间结果的需求，但不是原版 CONTEXT/ADR 的默认行为；不能直接用 ADR 的高门槛删掉这些中间结果。[记录规则](../skills/systems-paper-grill/references/decision-record.md)
- **采用简短记录。** 模板以 ID/状态、原文位置、短段落决定及证据组成，保留确认依据和必要的待确认或否决信息，而不要求填写逐项表格；兼容已有记录格式。更新后回读核对。[当前模板](../skills/systems-paper-grill/assets/paper-decisions-template.md)
- **主动澄清术语。** Grill 遇到与既有定义冲突的术语时明确追问，必要时以具体假设场景区分概念，将定义和应避免的混用词记在对应决定旁。假设场景不作为论文证据。[本地入口](../skills/systems-paper-grill/SKILL.md)
- **共享发现约定，不增加 setup。** 用户授权使用论文项目讨论记录后，三个 skills 优先读取指定路径，否则查项目根的 paper-decisions.md。单段或仅正文请求不触发邻近文件搜索。Revise 匹配原文并处理冲突；不会自动写入论文项目 AGENTS/CLAUDE。[交接约定](../skills/systems-paper-revise/references/review-revise-contract.md)

建议保留三个对外 skills 和一个论文记录文件，采用上游的轻量访谈、即时记录及显式消费思想；不照搬软件 issue tracker、CONTEXT-MAP、多份 ADR 或额外 setup 技能。
