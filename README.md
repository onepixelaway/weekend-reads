# Weekend Reads

![An open book becoming a quiet landscape](assets/headers/weekend-reads-banner.webp)

**Turn a big question into a great 10,000-word read.**

Some topics deserve more than a thread and less than a book. Weekend Reads is
an Agent Skill that helps you explore one of those topics properly, then turn
what you find into something people will actually enjoy reading.

Bring a subject, a half-formed idea, or a question you cannot stop thinking
about. Weekend Reads helps you find the real story, choose a shape for it,
research it carefully, and write it one chapter at a time. The usual destination
is an 8,000–12,000-word guide: deep enough to be useful, relaxed enough for a
Saturday afternoon.

## How it works

1. **Find the real question.** A broad topic becomes a clear promise to the
   reader.
2. **Pick a route.** The guide can lean on reporting, first-principles thinking,
   or a useful mix of both.
3. **Make a map.** Weekend Reads suggests three different structures, recommends
   one, and builds the chosen route into a chapter-by-chapter outline.
4. **Write without rushing.** It sets the voice, drafts in manageable passes,
   and keeps the outline from quietly wandering off.
5. **Give it a proper edit.** Facts get checked, repetition gets cut, and stiff
   or suspiciously AI-sounding prose gets another pass.

You stay in control along the way. Ask for the whole guide, or stop after the
brief, research, outline, sample chapter, or edit.

Weekend Reads defaults to clean Markdown, but it can also prepare versions for
text-to-speech, EPUB, or audio.

## Where it works

Weekend Reads uses the open [Agent Skills
format](https://agentskills.io/specification), so the same folder works across
the major AI writing tools.

| Platform | How to start |
| --- | --- |
| ChatGPT | Select or mention **Weekend Reads**, then tell it what you want to explore. |
| Codex app, CLI, and IDE extension | Invoke `$weekend-reads`, or simply ask for a deep guide. |
| Claude | Enable the skill and ask naturally. |
| Claude Cowork | Use the enabled skill in a Cowork task. |
| Claude Code | Invoke `/weekend-reads`, or ask for a matching task. |

Availability can vary by plan and workspace settings. The official setup guides
for [OpenAI Skills](https://learn.chatgpt.com/docs/build-skills), [Claude
Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude),
and [Claude Code Skills](https://code.claude.com/docs/en/skills) have the latest
details.

## Install it

### ChatGPT

Open the custom Skill creation or import flow in a workspace with Skills
enabled, then provide this folder or its ZIP archive. The included
`agents/openai.yaml` gives ChatGPT the display name and starter prompt.

### Codex

Install it for your user account:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git \
  ~/.agents/skills/weekend-reads
```

Or add it to one repository:

```text
<repository>/.agents/skills/weekend-reads/
```

Codex should find it automatically. If it does not show up, restart Codex.

### Claude and Claude Cowork

Clone the repo and zip the skill folder:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git
zip -r weekend-reads.zip weekend-reads \
  -x 'weekend-reads/.git/*' 'weekend-reads/.DS_Store'
```

In Claude, open **Customize → Skills**, add a skill, and upload
`weekend-reads.zip`. Once it is enabled, you can use it in Claude and Cowork
where your plan supports Skills.

### Claude Code

Install it for all your projects:

```bash
git clone https://github.com/onepixelaway/weekend-reads.git \
  ~/.claude/skills/weekend-reads
```

Or add it to one project:

```text
<project>/.claude/skills/weekend-reads/
```

## Give it a spin

You do not need a perfect brief. Start messy:

```text
Use Weekend Reads to help me write a deep guide to how cities manage water.
It is for curious general readers, and I want it grounded in current research.
Help me find the real question first.
```

Or jump straight to one part of the process:

```text
Use Weekend Reads to suggest three ways to structure a 10,000-word guide to
personal archives. Stop after the outline so I can choose the direction.
```

The skill asks for the missing bits without handing you a giant questionnaire.
It also knows when to stop, so asking for an outline will not mysteriously turn
into ten thousand words of surprise homework.

## What's in the box

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

`SKILL.md` holds the main workflow. The extra guides come off the shelf only
when they are useful, keeping the skill light on its feet.
