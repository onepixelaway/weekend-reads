---
name: weekend-reads
description: Guide a user from idea to an engaging, deeply researched 8,000–12,000-word weekend read. Use for deep guides, field guides, long-form explainers, or roughly 10,000-word narrative reports.
---

# Weekend Reads

Help the user make a deep guide that rewards a long, unhurried sitting. Aim for
about 10,000 words unless the material wants a different length. Treat the work
as a collaboration with decision points, not a one-shot request for a very long
answer.

## Core outcome

Produce a guide that:

- gives a curious non-specialist a reliable working understanding of the topic;
- has a clear reader promise and a deliberate beginning, middle, and landing;
- earns authority through research, reasoning, or a declared blend of both;
- remains pleasurable to read through concrete detail, variation, and momentum;
- uses familiar words whenever they are as accurate as more formal ones;
- contains no invented facts, scenes, quotations, statistics, or sources.

## Run the workflow

### 1. Frame the reading journey

Establish the following before designing the piece:

- the topic and the deeper question beneath it;
- the reader and what they likely know already;
- what the reader should understand, feel, or be able to do by the end;
- whether the guide is mainly researched, reasoned from first principles, or a
  blend;
- whether the subject is current enough to require fresh web research;
- any required examples, voices, regions, periods, exclusions, or sources;
- the output format and whether the work may be published externally.

If the prompt already answers these, do not ask again. If it does not, ask one
high-leverage question at a time rather than presenting a questionnaire. When
enough is known, state a compact working brief and invite corrections.

Treat 8,000–12,000 words as the default range, not a quota. Narrow a subject
that cannot be handled honestly at that length. Expand the target only when the
user explicitly wants a broader book-length treatment.

### 2. Choose how the guide earns trust

Classify the grounding:

- **Research-led:** Use for landscapes, histories, reported topics, changing
  fields, and claims about the world. Research before outlining in detail.
- **Reasoning-led:** Use for craft, conceptual frameworks, and first-principles
  explanations. Define assumptions and reason openly; do not decorate the piece
  with unnecessary citations.
- **Blended:** Use sourced material for empirical claims and first-principles
  reasoning for interpretation. Make the boundary visible in the prose.

For research-led and blended guides, read
`references/research-method.md` and follow it. Browse whenever facts may have
changed or when the user asks for current information. Never use a source that
was not actually opened or inspected.

### 3. Design the structure with the user

Read `references/outline-methodology.md`. Offer three genuinely different
structures, explain what each makes possible, and recommend one. A hybrid is
often strongest, but do not present cosmetic variants of the same table of
contents.

After the user chooses a direction, produce a complete outline with:

- a title direction and one-sentence reader promise;
- six to nine substantial chapters or sections in a purposeful order;
- a one-line contract for each chapter;
- the central questions, evidence, examples, and tensions each chapter carries;
- rough word budgets that total near the agreed length;
- an ending that delivers synthesis rather than merely stopping.

Pressure-test the outline for gaps, overlap, imbalance, and loss of momentum.
Apply the fixes and briefly explain the important changes.

Do not draft the full guide until the user approves the outline, unless the user
explicitly asks for an autonomous end-to-end run. If the user asked only for an
outline, deliver only the outline.

### 4. Establish the voice

Before drafting, read `references/voice-and-style.md` in full. Write one
calibration paragraph on the actual topic. Use it as a tuning fork: later prose
should feel as though it belongs beside it.

The default register is composed, curious, concrete, and lightly authoritative.
Do not imitate a named living writer. If the user supplies a sample, infer its
high-level traits without copying distinctive phrasing.

### 5. Draft in controlled passes

Draft chapter by chapter against the approved outline. Maintain a small working
ledger containing the chapter contract, word budget, claims still needing
support, and threads that must return later.

For each chapter:

1. State the chapter's job privately before writing.
2. Gather or verify the evidence needed for that job.
3. Write the chapter as continuous prose, using subheads only when they aid a
   tired reader returning to the piece.
4. Check every factual claim, quotation, number, and scene against the source
   ledger.
5. End with an earned turn or implication, not a preview of the next chapter.

Keep momentum across the full guide:

- alternate explanation with concrete cases, mechanisms, history, or observed
  detail;
- introduce tension before resolving it;
- vary paragraph and sentence length without turning style into performance;
- give the reader periodic moments of synthesis and rest;
- make abstractions tangible, but never fabricate a narrative scene;
- preserve useful complexity instead of forcing every issue into a neat thesis.

Write the introduction after the body when that will produce a more accurate
promise. Write the ending last. The ending should change the reader's view of
the opening question, gather the major threads, and leave one durable idea.

### 6. Revise at three levels

Revise in this order:

1. **Structural:** Does the guide fulfill its promise? Cut repetition, fill
   gaps, reorder only with the user's approval if the outline was locked, and
   rebalance word counts.
2. **Evidentiary:** Verify claims and citations. Represent disagreement fairly.
   Remove details that are merely plausible.
3. **Line-level:** Improve clarity, rhythm, transitions, headings, and concrete
   language. Run a plain-language pass that replaces needlessly formal words
   with familiar ones while keeping necessary technical terms accurate. Remove
   AI-writing tics and administrative signposting.

Run `references/quality-checklist.md` before delivery and fix what it finds.

### 7. Deliver cleanly

Default to clean Markdown with a title, optional subtitle or standfirst,
content-bearing headings, and a restrained notes or sources section. Keep the
main text readable; do not let citation machinery take over the page.

When files can be created, keep the working brief, approved outline, source
ledger, and final draft as separate artifacts. When they cannot, label each
artifact clearly in the conversation. Do not expose private chain-of-thought;
share decisions, assumptions, evidence, and concise rationales instead.

If the guide is for text-to-speech, EPUB, or audio, follow the relevant rules in
`references/voice-and-style.md`. If it will be published externally, remove
private company or personal context unless the user explicitly wants a byline
or disclosed point of view.

## Respect scope and stopping points

The user may request only framing, research, an outline, a sample chapter, a
revision, or the complete guide. Complete the requested phase and stop at its
natural decision point. Do not bury a useful intermediate artifact beneath a
premature 10,000-word draft.

## References

- `references/outline-methodology.md`: read when choosing and pressure-testing
  the structure.
- `references/research-method.md`: read for research-led or blended guides.
- `references/voice-and-style.md`: read in full before drafting prose.
- `references/quality-checklist.md`: run before delivering any full draft.
