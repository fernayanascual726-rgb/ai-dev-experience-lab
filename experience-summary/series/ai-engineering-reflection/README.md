# AI 工程化沉思录

这是一个关于 **AI Native Engineering** 的长期系列。

它聚焦 AI Coding 进入真实工程环境后，软件开发流程正在发生的变化：开发者如何维护上下文，如何 Review AI 输出，Prompt 如何承担工程约束，以及 AI Workflow 为什么需要状态管理。

这个系列不是 AI 工具分享，而是记录 AI 如何重构软件工程中的协作方式、知识沉淀方式和开发者体验。

## 系列主线

```text
上下文债务
→ Code Review
→ Prompt 架构化
→ Workflow 状态管理
```

## 文章目录

| 序号 | 主题 | 目录 | 一句话说明 |
| --- | --- | --- | --- |
| 01 | 上下文债务 | [01-context-debt](01-context-debt/) | 当 AI Coding 进入真实工程环境后，Context 正在成为新的复杂度来源。 |
| 02 | AI Code Review | [02-code-review](02-code-review/) | 当 AI 输出增多，Review 需要从代码检查扩展到风险、语义和责任边界确认。 |
| 03 | Prompt 架构化 | [03-prompt-architecture](03-prompt-architecture/) | 当 Prompt 承载越来越多工程约束，它开始接近临时架构文档和协作接口。 |
| 04 | Workflow 状态管理 | [04-workflow-state](04-workflow-state/) | 当 AI 深度参与多轮开发任务，状态连续性会成为可靠协作的关键问题。 |

## 目录约定

每个主题目录保留：

- `README.md`：该主题的说明和文章导航
- `assets/`：图表、截图和发布配图
- `examples/`：代码片段、Prompt 示例和 workflow demo

后续可按需增加：

```text
diagrams/
prompts/
workflow/
```

## 写作原则

- 关注真实工程流程，而不是工具功能展示
- 记录副作用、边界和长期维护成本
- 保留 Human-in-the-loop 的判断与责任
- 优先沉淀可复用的工作流观察
