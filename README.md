# AI Dev Experience Lab

Explore how AI improves developer experience, workflow design, and engineering collaboration.

![License](https://img.shields.io/badge/license-TBD-lightgrey.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/fernayanascual726-rgb/ai-dev-experience-lab)
![Docs](https://img.shields.io/badge/docs-Markdown-lightgrey.svg)

这是一个面向 **AI Developer Experience（AI 开发者体验）** 的长期知识库，用于沉淀 AI 在研发流程、编码协作、工作流设计和团队实践中的真实经验。

这里关注的不是概念本身，而是 AI 如何进入日常开发：在哪些场景有效，如何设计提示词，怎样嵌入工作流，以及它对开发者效率和协作体验带来的具体变化。

## Why This Repository Exists

AI 工具正在进入日常开发流程，但工具可用不等于体验变好，也不等于团队效率自然提升。

这个仓库用于长期记录 AI 在真实研发场景中的使用方式：它如何帮助开发者理解代码、组织上下文、设计工作流、协作 Review，以及在哪些地方仍然需要人工判断。

重点不是展示工具能力，而是沉淀可复用、可复核、可持续维护的开发者体验实践。

## Current Focus

- **AI Debug Workflow**：整理 AI 辅助排查问题时的上下文准备、假设验证和复盘方式。
- **Prompt Collaboration**：记录 prompt 如何支持开发者表达意图、约束边界和协作检查点。
- **AI Coding Experience**：观察 AI 在代码理解、修改、测试和 Review 中带来的体验变化。
- **Human-in-the-loop Development**：保留开发者判断、验证和责任边界，让 AI 成为协作环节的一部分。

## Philosophy

- AI 不替代开发者思考，尤其不替代工程判断和责任承担。
- 好的 AI 工作流应该是可观察的：输入、过程、输出和假设都应尽量清楚。
- AI 输出需要可复核，特别是在代码、测试、Review 和发布相关场景中。
- 长期价值来自持续沉淀，而不是一次性的生成速度。
- 人机协作应该降低心智负担，而不是制造新的验证和沟通成本。

## Knowledge Map

### `experience-summary/`

用于记录 AI Developer Experience、效率变化和协作体验方面的阶段性总结。

- [为什么很多开发者用了 AI，却没有真正提升效率？](experience-summary/why-ai-does-not-always-improve-efficiency.md)
- [总结模板](experience-summary/example-template.md)
- [内容规范](experience-summary/content-guidelines.md)

### `ai-workflow/`

用于记录 AI 如何嵌入研发流程、团队协作和日常开发节奏。

- [工作流模板](ai-workflow/example-template.md)
- [内容规范](ai-workflow/content-guidelines.md)
- [目录说明](ai-workflow/README.md)

### `dev-prompt/`

用于沉淀面向开发任务的 AI 提示词模板、写法和复盘。

- [Prompt 模板](dev-prompt/example-template.md)
- [内容规范](dev-prompt/content-guidelines.md)
- [目录说明](dev-prompt/README.md)

### `tech-sharing/`

用于整理 AI 开发者体验相关的技术分享、内部交流材料和演讲草稿。

- [分享模板](tech-sharing/example-template.md)
- [内容规范](tech-sharing/content-guidelines.md)
- [目录说明](tech-sharing/README.md)

### `lab/`

用于保存轻量级 AI workflow demo。

- [AI Code Review Demo](lab/ai-code-review-demo.py)
- [目录说明](lab/README.md)

## Workflow Demos

- [AI Code Review Demo](lab/ai-code-review-demo.py)
- [Workflow Diagram](lab/ai-code-review-workflow.md)

## Recent Updates

> Run `python3 scripts/update-index.py` after adding Markdown content to refresh this section and `INDEX.md`.

<!-- RECENT_UPDATES_START -->

- {{ YYYY-MM-DD }} — [{{ 文章标题 }}](experience-summary/ai-developer-experience-worldview.md) — Developer Experience / AI Workflow
- 2026-05-29 — [为什么很多开发者用了 AI，却没有真正提升效率？](experience-summary/why-ai-does-not-always-improve-efficiency.md) — Developer Experience / AI Workflow
- 2026-05-29 — [AI Workflow 的核心已经不是生成，而是状态管理](experience-summary/series/ai-engineering-reflection/04-workflow-state/article.md) — AI Workflow / Agent System
- 2026-05-29 — [Prompt：当代开发者的临时架构文档](experience-summary/series/ai-engineering-reflection/03-prompt-architecture/article.md) — Prompt Engineering / AI Coding
- 2026-05-29 — [AI Coding 正在让 Code Review 变得越来越重要](experience-summary/series/ai-engineering-reflection/02-code-review/article.md) — AI Coding / Code Review
- 2026-05-29 — [上下文正在变成新的技术债](experience-summary/series/ai-engineering-reflection/01-context-debt/article.md) — Developer Experience / AI Workflow

<!-- RECENT_UPDATES_END -->

## Roadmap

- AI Debug Workflow
- Prompt Library
- Human-AI Collaboration Patterns

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

## Maintenance

这个仓库适合作为持续迭代的知识库。内容可以先以草稿形式记录，再逐步整理为案例、模板或分享材料。重点是保留实践上下文，让未来的复盘和复用更容易。

新增内容后建议执行：

```bash
python3 scripts/update-index.py
```

该命令会刷新文章索引和 README 的 Recent Updates 区域。
