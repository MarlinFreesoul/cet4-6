# Evidence model and phase gates

## Evidence labels

Tag important claims with one of four levels:

| Label | Meaning | Example |
|---|---|---|
| `OBSERVED` | Direct artifact or recorded event | Original answer sequence in a photo |
| `REPORTED` | Learner’s retrospective account | “I understood the theme in paragraph three” |
| `INFERRED` | Best explanation supported by multiple facts | Correct candidates were recognized but locally misplaced |
| `UNVERIFIED` | Plausible hypothesis awaiting a new test | Slot-signature marking will improve transfer accuracy |

Do not convert `REPORTED` into `OBSERVED`. Do not convert `INFERRED` into a stable trait. Preserve conflicting evidence instead of resolving it rhetorically.

## Minimum experiment identity

Use:

`date / source and set / task type / part or section / item range / fingerprint`

The fingerprint can be opening words, file hash, screenshot, URL, or another unique marker. Labels such as “the first reading” are insufficient.

## Contamination ledger

Record any event that could alter independent performance:

- answer exposure;
- word definition;
- strategy hint;
- difficulty framing;
- repeated attempt;
- external lookup;
- interrupted timing;
- wrong or ambiguous material identity.

Classify the attempt:

- `clean-baseline`: no material contamination known;
- `partial-baseline`: some components remain independent;
- `practice-only`: useful for learning, invalid for baseline inference.

Contamination does not make work worthless; it changes which claims are allowed.

## Gate checks

### G0 — Material identity

Pass only when source, scope, and fingerprint agree. If they do not, stop scoring and resolve the identity.

### G1 — Baseline integrity

Pass when contamination is absent or explicitly bounded. Never silently downgrade a clean-baseline requirement.

### G2 — Evidence freeze

Pass when the original output and the most decision-relevant process evidence are saved. If the learner requests answers immediately, first capture at least the answer sequence, confidence or guesses, and overall approach.

### G3 — Causal adequacy

Pass when the explanation identifies a decision point and missing or misused constraint. “Did not know the answer” does not pass.

### G4 — Intervention eligibility

Pass when one to three bottlenecks explain the important pattern and each proposed intervention maps to one of them.

### G5 — Testability

Pass when the next experiment names:

- material;
- invariant conditions;
- changed behavior;
- observable trace;
- metrics;
- support threshold;
- falsification or revision condition.

## Timing discipline

- Prefer user-recorded start and end times.
- Treat platform message timestamps only as an observation window.
- If interrupted, record active time and wall time separately when possible.
- Never fabricate seconds-level precision.

## Answer authority

Record whether an answer is official, publisher-provided, teacher-provided, community-derived, or agent-inferred. When authority is uncertain, say so and avoid overstating the diagnosis.
