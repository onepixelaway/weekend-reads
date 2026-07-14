# Quality Checklist

Run this checklist on a complete draft before delivery. Fix the problems it
finds; do not merely report them.

## 1. Promise and structure

- Does the title, standfirst, and opening make a promise the guide fulfills?
- Can the central question be stated in one sentence after reading the draft?
- Does each chapter perform its approved contract?
- Is the total length near the agreed range? If not, is the difference earned?
- Does the sequence deepen rather than merely accumulate information?
- Does the ending synthesize the major threads and change the opening picture?
- Are any chapters redundant, disproportionately long, or starved of evidence?

## 2. Evidence integrity

- Trace every quotation, statistic, named attribution, historical claim, and
  scene-like detail to a source that was actually inspected.
- Check that citations support the exact nearby claim, not only the general
  subject.
- Recheck dates, units, denominators, comparisons, and whether figures are
  nominal, adjusted, estimated, or measured.
- Prefer primary sources and label estimates, uncertainty, and inference.
- Verify that links lead to the intended source and that titles and authors are
  accurate.
- Remove any plausible detail that cannot be verified.
- Represent serious disagreement fairly and avoid citation laundering through
  weak summaries.

## 3. Reader experience

- Is there an early concrete foothold?
- Does the prose move regularly between explanation and tangible examples?
- Are difficult sections followed by enough synthesis or relief?
- Do headings help a reader resume after setting the piece down?
- Does curiosity or consequence carry the reader from one chapter to the next?
- Are there long stretches of summary, jargon, quotations, or identical
  paragraph shapes?
- Does the piece preserve complexity without becoming shapeless?

## 4. Voice and line quality

- Compare several paragraphs from the beginning, middle, and end with the
  calibration paragraph.
- Remove blog cadence, self-help language, academic fog, sales language, and
  generic AI phrasing.
- Replace vague abstractions with plain, exact words.
- Identify people, institutions, tools, and specialized terms on first mention.
- Cut throat-clearing, filler intensifiers, hollow importance claims, and
  administrative previews.
- Break the reflexive use of em dashes, false antitheses, three-item lists,
  “from X to Y,” and repeated one-line dramatic paragraphs.
- Read representative pages aloud and repair sentences that are hard to parse.

## 5. Useful automated scans

Use `rg` when available; fall back to `grep`. Let `$FILE` point to the draft.
Treat matches as review prompts, not automatic errors.

Count words and inspect chapter balance:

```bash
wc -w "$FILE"
rg -n '^#{1,3} ' "$FILE"
```

Find repeated machine-prose patterns:

```bash
rg -ni "it'?s not .{1,100},? it'?s|it is not .{1,100},? it is|it'?s worth noting|at the end of the day|in today'?s world|\b(genuinely|truly|incredibly|really|simply)\b|from .{1,80} to .{1,80}" "$FILE"
rg -n '—' "$FILE"
```

Find administrative signposting:

```bash
rg -ni "in this (chapter|section)|as we (saw|discussed|noted)|we will (see|explore|cover)|the next (chapter|section)" "$FILE"
```

For text-to-speech or EPUB, inspect visually dependent constructs:

```bash
rg -n "\[\^[0-9]+\]|^\|.*\||[<>~^]" "$FILE"
```

## 6. Delivery and privacy

- Remove drafting notes, placeholders, unresolved source flags, and private
  instructions.
- Confirm that the notes or source section uses a consistent format.
- For external publication, remove personal and company context that was not
  meant for readers.
- For text-to-speech, EPUB, or audio, apply the matching output rules in
  `voice-and-style.md`.
- Deliver the requested artifact only, plus a concise note about material
  assumptions or limitations.
