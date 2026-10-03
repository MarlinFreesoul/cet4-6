# Evidence and gates for CET4 Section A

## Evidence levels

| Label | Meaning |
|---|---|
| `OBSERVED` | Direct paper, answer sequence, annotation, timer, or artifact |
| `REPORTED` | Learner’s retrospective account |
| `INFERRED` | Best causal explanation supported by multiple observations |
| `UNVERIFIED` | Hypothesis awaiting delayed retrieval or unseen transfer |

Do not promote a reported memory into an observation or a one-passage inference into a stable trait.

## G0 — Format and identity

Pass only when:

- the task matches CET4 Reading Section A word-bank cloze;
- passage, 10 blanks, and 15 candidates are complete;
- year/month, set/source, item range, and opening words are recorded;
- any mismatch is marked `FORMAT_DRIFT`.

## G1 — Baseline integrity

Log contamination:

- answer or explanation exposure;
- word definition or translation;
- part-of-speech or structure hint;
- candidate elimination;
- difficulty framing;
- external lookup;
- repeated attempt;
- timing interruption;
- incomplete or wrong material.

Classify:

- `clean-baseline`;
- `partial-baseline`;
- `practice-only`.

## G2 — Evidence freeze

Pass when the original answer sequence, confidence/guess status, scope mode, active time, strategy order, and most important contemporaneous reasoning are saved.

## G3 — Answer-key authority

Label the key:

- `official`;
- `publisher`;
- `teacher`;
- `third-party`;
- `agent-inferred`;
- `disputed`.

Do not present a third-party compilation as the official committee key. If keys conflict, pause final diagnosis for the disputed blanks.

## G4 — Causal adequacy

Pass when each consequential item reaches a missed or misused constraint and a plausible cognitive mechanism. “Vocabulary problem,” “grammar problem,” and “carelessness” alone do not pass.

## G5 — Intervention eligibility

Pass when one to three bottlenecks explain the important topology and each proposed intervention maps to one of them. Select one or two interventions only.

## G6 — Transfer testability

Pass when the next experiment specifies:

- an unseen CET4 Section A passage matching the official fingerprint;
- comparable source and scope mode;
- controlled conditions;
- changed behavior;
- visible execution trace;
- process and outcome metrics;
- support and falsification criteria.

## Timing discipline

- Record active time for isolated Section A work.
- Record the full reading-block context when Section A is done inside the official 40-minute reading period.
- Do not compare isolated and full-block times as if conditions were equal.
- Do not invent an official Section A time limit.
- Treat message timestamps only as an observation window unless the learner confirms actual start and end times.
