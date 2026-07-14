# Weekend Reads

![An open book becoming a quiet landscape](assets/headers/weekend-reads-banner.webp)

Weekend Reads is an open Agent Skill for creating an absorbing, deeply
researched guide of roughly 10,000 words: something substantial enough to teach
a subject properly, but paced and written to be enjoyed over a weekend.

Instead of responding to a broad topic with one very long first draft, the skill
walks the writer through the decisions that make long-form work succeed. It
frames the reader's journey, chooses the right balance of research and
first-principles reasoning, compares several possible structures, builds and
pressure-tests an outline, establishes the voice, drafts in controlled passes,
and finishes with structural, evidentiary, and line-level revision.

## What it does

- Turns a topic into a clear reader promise and governing question.
- Targets an 8,000–12,000-word guide while narrowing subjects that cannot be
  handled honestly at that length.
- Chooses between research-led, reasoning-led, and blended approaches.
- Offers three meaningfully different structures before committing to an
  outline.
- Builds a six-to-nine-chapter reading arc with chapter contracts and word
  budgets.
- Maintains a source ledger and evidence map for factual work.
- Calibrates a composed, documentary voice before drafting.
- Drafts chapter by chapter and preserves user approval points.
- Checks source integrity, pacing, privacy, readability, and common AI-writing
  habits before delivery.
- Supports clean Markdown, text-to-speech, EPUB, and pure-audio variants.

The skill can help with the complete process or stop after framing, research,
outlining, a sample chapter, or revision.

## Supported platforms

Weekend Reads follows the open [Agent Skills
specification](https://agentskills.io/specification) and uses a portable
`SKILL.md` with progressively loaded references.

| Platform | Support | Invocation |
| --- | --- | --- |
| ChatGPT | Custom and workspace Skills | Select or mention **Weekend Reads**, then describe the guide. |
| Codex app, CLI, and IDE extension | Filesystem Skills | Invoke `$weekend-reads` or make a matching request. |
| Claude | Custom Skills | Enable the skill and ask naturally or select it explicitly. |
| Claude Cowork | Custom Skills shared with Claude | Use the enabled skill in a Cowork task. |
| Claude Code | Filesystem Skills | Invoke `/weekend-reads` or make a matching request. |

Platform availability can depend on plan, workspace settings, and whether
Skills or code execution are enabled. See the official guides for [OpenAI
Skills](https://learn.chatgpt.com/docs/build-skills), [Claude
Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude),
and [Claude Code Skills](https://code.claude.com/docs/en/skills).

## Install

### ChatGPT

Use the custom Skill creation or import flow in a ChatGPT workspace with Skills
enabled, and provide this skill folder or its ZIP archive when prompted. The
included `agents/openai.yaml` supplies the OpenAI display name, description,
and starter prompt.

### Codex

Install for your user account:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git \
  ~/.agents/skills/weekend-reads
```

For one repository, clone or copy it to:

```text
<repository>/.agents/skills/weekend-reads/
```

Codex discovers `SKILL.md` automatically. If it does not appear immediately,
restart Codex.

### Claude and Claude Cowork

Clone the repository and create an uploadable ZIP whose root is the
`weekend-reads` folder:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git
zip -r weekend-reads.zip weekend-reads \
  -x 'weekend-reads/.git/*' 'weekend-reads/.DS_Store'
```

In Claude, open **Customize → Skills**, create or add a skill, and upload
`weekend-reads.zip`. Once enabled, the skill is also available in Cowork where
your plan and workspace settings support Skills.

### Claude Code

Install for all projects:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git \
  ~/.claude/skills/weekend-reads
```

For one project, clone or copy it to:

```text
<project>/.claude/skills/weekend-reads/
```

## Use it

Start with as much or as little context as you have:

```text
Use Weekend Reads to help me write a deep guide to how cities manage water.
It should be useful to a curious general reader and grounded in current
research. Start by helping me frame the real question.
```

Or ask for a specific phase:

```text
Use Weekend Reads to propose three structures for a 10,000-word guide to
personal archives. Do not draft the guide yet.
```

The skill asks only for missing, high-leverage information. It will not bury a
useful outline beneath a premature long draft.

## Structure

```text
weekend-reads/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── outline-methodology.md
    ├── quality-checklist.md
    ├── research-method.md
    └── voice-and-style.md
```

The main skill stays compact. It loads the research, outlining, voice, and
quality references only when the relevant phase requires them.
