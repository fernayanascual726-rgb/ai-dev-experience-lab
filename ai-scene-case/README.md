# AI Engineering Patterns & Cases

本目录用于沉淀 AI 在工程研发场景中的可复用实践。

它从具体 AI 使用案例库扩展为 AI Engineering Patterns & Cases，重点记录：

- 工程模式（Pattern）
- 实践案例（Case）
- 最佳实践（Best Practice）

本目录仍然关注真实问题、使用过程、效果边界和可复用经验，不用于存放趋势分析文章、行业观察或观点型长文。

趋势分析内容应放在 `experience-summary/`，例如上下文债务、Memory 竞争、Workflow 状态管理等主题。

## Scope

适合收录：

- Memory Engineering 的工程分层、裁剪和项目记忆实践
- Agent README / `CLAUDE.md` / `AGENTS.md` 的工程化维护方式
- Context Debt 的检测、清理和隔离模式
- AI Workflow 的状态设计、恢复和可观测性实践
- AI Teammate 在 Review、Testing、协作中的可复用模式
- Multi-Agent 编排、协调和角色分工模式

不适合收录：

- 趋势分析文章
- 公众号风格观点文
- 模型评测或排行榜
- 工具推荐清单
- Prompt 技巧集合
- 单纯展示 AI 生成能力的内容

## Directory Map

- [`memory-engineering/`](memory-engineering/)：Memory 分层、裁剪、项目记忆实践
- [`agent-readme/`](agent-readme/)：Agent 可读上下文文件与协作规范
- [`context-debt/`](context-debt/)：上下文债务检测、裁剪和清理案例
- [`state-management/`](state-management/)：Workflow 状态、任务状态和恢复设计
- [`ai-teammate/`](ai-teammate/)：AI Reviewer、AI Tester 和团队协作案例
- [`multi-agent/`](multi-agent/)：多 Agent 协调、评审和编排模式

## Existing Templates

- [`content-guidelines.md`](content-guidelines.md)：内容规范
- [`example-template.md`](example-template.md)：案例模板

## Writing Principles

- 以工程问题为起点，而不是以工具能力为起点
- 描述可复用模式，而不是一次性操作经验
- 明确适用边界、失败模式和权衡
- 保留人工决策点和系统治理点
- 优先沉淀长期有效的工程实践
