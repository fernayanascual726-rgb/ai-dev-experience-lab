# 标签体系

标签用于统一内容分类，便于长期检索和复盘。每篇内容建议选择 1-3 个标签，不建议堆叠过多。

## 标准标签

| 标签 | 适用内容 |
| --- | --- |
| `AI Coding` | AI 辅助编码、代码理解、重构、测试生成、Bug 排查等开发任务 |
| `Developer Experience` | 开发者体验、研发效率、心智负担、工具链体验和协作感受 |
| `AI Workflow` | AI 嵌入研发流程、团队协作流程、人机分工和检查点设计 |
| `Prompt Engineering` | 提示词结构、上下文组织、输出约束和 prompt 复盘 |
| `AI Collaboration` | 人与 AI、团队成员与 AI 之间的协作方式和责任边界 |
| `Dev Productivity` | 开发效率、交付节奏、重复劳动减少和工程反馈速度 |

## 标签使用规范

- 优先使用标准标签，避免同义标签分散内容
- 标签应描述内容主题，而不是结论态度
- 一篇内容通常选择 1-3 个标签
- 如果需要新增标签，应先确认已有标签无法覆盖

## 推荐组合

| 场景 | 推荐标签 |
| --- | --- |
| AI 辅助完成编码任务 | `AI Coding`, `Dev Productivity` |
| 总结团队引入 AI 的体验 | `Developer Experience`, `AI Collaboration` |
| 设计从 issue 到 PR 的流程 | `AI Workflow`, `AI Collaboration` |
| 记录提示词模板和复盘 | `Prompt Engineering`, `AI Coding` |
| 复盘效率变化 | `Developer Experience`, `Dev Productivity` |

## Frontmatter 示例

```yaml
---
title: "文章标题"
date: 2026-05-29
status: draft
tags:
  - AI Coding
  - Developer Experience
---
```
