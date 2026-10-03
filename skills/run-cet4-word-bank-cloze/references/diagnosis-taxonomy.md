# Section A diagnostic taxonomy

## Causal chain

For each consequential blank, record:

1. result;
2. actual cue used;
3. required constraint;
4. break point;
5. mechanism;
6. transferable capability.

## Error codes

| Code | Mechanism | Distinguishing test |
|---|---|---|
| `V-UNK` | Candidate form or relevant sense unknown | Cannot recognize or explain it in the sentence after neutral prompting |
| `V-RET` | Known lexical knowledge not retrieved | Recognition returns promptly after a non-answer cue and prior knowledge is evidenced |
| `V-MIS` | Wrong contextual sense or synonym boundary | Form is known but mapped to an incompatible sense |
| `CHUNK` | Multiword unit unavailable | Words are known individually; the frame is not recognized |
| `MORPH` | Required inflection or derivation missed | Lemma fits but visible form does not |
| `SLOT` | Part of speech or syntactic role misidentified | Candidate fails the local slot signature |
| `VAL` | Valency, transitivity, complement, or preposition failure | Meaning seems plausible but the argument frame fails |
| `CLAUSE` | Clause boundary, reference, reduction, or ellipsis failure | Local words are known but proposition structure is wrong |
| `COH` | Lexical or grammatical cohesion failure | Local sentence works in isolation but not with adjacent context |
| `MODEL` | Passage topic, stance, chronology, or contrast model is wrong or late | Multiple local choices change after the passage model is corrected |
| `BANK` | One-use allocation, swap, or cascade interference | A viable word is misplaced or unavailable because of an earlier assignment |
| `CHECK` | Independent full-sentence validation omitted | A placed answer would fail a deliberate reread |
| `STRAT` | Procedure systematically loses usable evidence | The same step causes repeated errors across blanks |
| `TIME` | Time prevents an otherwise available process | Untimed reconstruction succeeds without teaching |
| `ATT` | Relevant evidence is not inspected despite available knowledge | Rule is retrievable but checkpoint is skipped |
| `CARE` | Pure marking or copying slip | Reasoning is correct and stable before the final mechanical action |
| `MATERIAL` | Paper, extraction, or key ambiguity | Version mismatch or conflicting keys explain the discrepancy |

Use only necessary codes. Separate the initiating cause from downstream cascade effects.

## Strict test for carelessness

Use `CARE` only when all are true:

1. the required knowledge was available and retrieved;
2. the intended candidate and reasoning were correct;
3. the final error was mechanical;
4. the conceptual error does not recur.

Otherwise use `ATT`, `CHECK`, `SLOT`, `VAL`, `BANK`, or another deeper mechanism.

## Correct-answer audit

| Class | Meaning |
|---|---|
| `STABLE` | Exact contextual sense, form, frame, cohesion, and reproducible reason |
| `STRUCTURE_HIT` | Structural fit found without accurate lexical understanding |
| `APPROXIMATE` | Directionally correct but semantically or logically imprecise |
| `ELIMINATION_HIT` | Mainly produced by remaining-bank logic |
| `LUCKY` | No reproducible basis |

Only `STABLE` is provisional mastery. Retest every other class.

## Bottleneck aggregation

Promote a mechanism only when it:

- recurs;
- explains a swap or cascade;
- affects the whole passage model;
- explains several surface errors; or
- is high-leverage and directly testable.

Keep one to three bottlenecks. Preserve lower-priority findings in the backlog.
