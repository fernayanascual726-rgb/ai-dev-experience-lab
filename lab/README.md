# Lab

本目录用于保存轻量级 AI workflow demo。

这些 demo 的目标不是展示复杂 AI 能力，而是观察 AI 如何进入开发者工作流：在什么环节提供帮助，哪些判断仍然需要开发者完成，以及如何把过程沉淀为可复用的协作模式。

## 为什么存在这些 demo

AI Developer Experience 不只发生在模型输出结果的瞬间，也发生在上下文准备、提示词表达、人工确认、代码修改和最终提交之间。

因此，本目录中的示例会尽量保持简单、可运行、低依赖。它们更像工作流样本，而不是完整产品或框架项目。

## AI Workflow 的定位

这里的 AI Workflow 关注三件事：

- AI 在开发流程中的介入点
- 开发者如何验证和修正 AI 输出
- 团队如何保留可复核的协作记录

## 当前 Demo

| Demo | 说明 |
| --- | --- |
| [AI Code Review Demo](ai-code-review-demo.py) | 模拟 AI 如何辅助开发者发现可读性、命名、异常处理和优化问题 |
| [AI Code Review Workflow](ai-code-review-workflow.md) | 使用 Mermaid 描述 Code Review 中的人机协作流程 |

## 后续方向

- AI Debug Workflow
- AI Code Review
- Prompt Collaboration
- Human-in-the-loop Development

## 维护原则

- 示例应保持可运行、可阅读、低依赖
- 每个 demo 只展示一个明确的工作流场景
- 代码复杂度服务于说明 Developer Experience，不追求炫技
- AI 建议必须保留人工确认和复核环节
