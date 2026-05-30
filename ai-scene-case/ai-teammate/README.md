# AI Teammate

## 概览

AI Teammate 关注 AI 作为工程团队成员参与协作时的角色设计、职责边界和交付质量控制。它不是把 AI 当作一次性生成工具，而是把 AI 放入 Review、Testing、Debugging 和知识整理流程中。

## 为什么重要

AI 参与团队协作后，关键问题不只是“能否生成代码”，而是能否以稳定角色承担可复用职责，并在合适的边界内支持人类决策。

## 常见 Pattern

- AI Reviewer Pattern：辅助发现一致性、风险和遗漏
- AI Tester Pattern：辅助补充测试思路和验证路径
- Human Approval Gate：关键决策必须由人确认
- Role Boundary：明确 AI 的建议权和执行权

## 典型 Case

- AI 作为 Pull Request Reviewer
- AI 辅助生成测试策略，而不是直接替代测试设计
- AI 协助团队理解遗留模块
- AI 在变更前后对比风险清单

## 相关文档

- [AI Reviewer Pattern](ai-reviewer-pattern.md)
- [AI Tester Pattern](ai-tester-pattern.md)
- [AI Code Review Case](ai-code-review-case.md)
