# AI Dev Experience Lab

Explore how AI improves developer experience, workflow design, and engineering collaboration.

![License](https://img.shields.io/badge/license-TBD-lightgrey.svg)
![Last Commit](https://img.shields.io/github/last-commit/fernayanascual726-rgb/ai-dev-experience-lab)
![Markdown](https://img.shields.io/badge/docs-Markdown-lightgrey.svg)
![AI Workflow](https://img.shields.io/badge/focus-AI%20Workflow-purple.svg)

这是一个面向 **AI Developer Experience（AI 开发者体验）** 的长期知识库，用于沉淀 AI 在研发流程、编码协作、工作流设计和团队实践中的真实经验。

这里关注的不是概念本身，而是 AI 如何进入日常开发：在哪些场景有效，如何设计提示词，怎样嵌入工作流，以及它对开发者效率和协作体验带来的具体变化。

## Core Focus

- **AI Developer Experience**：观察 AI 工具如何影响开发者的理解成本、反馈速度和工作节奏。
- **AI Workflow Design**：沉淀可执行的 AI 辅助研发流程，而不是停留在工具清单。
- **Prompt Collaboration**：记录提示词如何承载上下文、约束和协作意图。
- **AI Coding Practices**：复盘 AI 在代码理解、修改、测试和 Review 中的真实表现。
- **Developer Productivity**：关注效率提升背后的条件、边界和验证方式。
- **Human-AI Collaboration**：明确人和 AI 的分工，保留人工判断和工程责任边界。

## Repository Structure

```text
ai-dev-experience-lab/
├── README.md
├── INDEX.md
├── TAGS.md
├── ai-scene-case/
├── ai-workflow/
├── dev-prompt/
├── experience-summary/
├── lab/
├── tech-sharing/
└── templates/
```

## Navigation

- [Article Index](INDEX.md)
- [Tag Taxonomy](TAGS.md)
- [GitHub Project Intro](GITHUB_PROJECT_INTRO.md)
- [Markdown Templates](templates/README.md)
- [Workflow Demos](lab/README.md)

## Recent Updates

> Run `python3 scripts/update-index.py` after adding Markdown content to refresh this section and `INDEX.md`.

<!-- RECENT_UPDATES_START -->

- 2026-05-29 — [为什么很多开发者用了 AI，却没有真正提升效率？](experience-summary/why-ai-does-not-always-improve-efficiency.md) — Developer Experience / AI Workflow

<!-- RECENT_UPDATES_END -->

## Roadmap

- AI Debug Workflow：整理 AI 辅助排查问题的上下文组织和验证方式。
- Prompt Library：沉淀适合开发任务的提示词结构和使用边界。
- AI Collaboration Patterns：记录人机协作、团队协作和责任划分模式。
- Developer Experience Research：持续复盘 AI 对开发者体验的影响。

## Writing Principles

- 以真实开发场景为起点
- 优先记录可复用的方法，而不是一次性结论
- 保留背景、约束和失败经验
- 避免空泛判断，尽量说明适用条件
- Markdown 风格保持简洁、清晰、可长期维护

## Suggested Article Shape

每篇内容建议包含：

1. 背景
2. 问题或目标
3. 使用方式
4. 过程记录
5. 结果与限制
6. 可复用经验

## Maintenance

这个仓库适合作为持续迭代的知识库。内容可以先以草稿形式记录，再逐步整理为案例、模板或分享材料。重点是保留实践上下文，让未来的复盘和复用更容易。

新增内容后建议执行：

```bash
python3 scripts/update-index.py
```

该命令会刷新文章索引和 README 的 Recent Updates 区域。