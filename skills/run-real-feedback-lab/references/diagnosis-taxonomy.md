# Diagnostic taxonomy and causal tests

## Atomic causal chain

For each consequential item, fill five layers:

1. **Result:** What observable answer or behavior occurred?
2. **Decision:** What did the learner choose or skip?
3. **Constraint:** What lexical, grammatical, logical, strategic, temporal, or attentional constraint was missed or misused?
4. **Mechanism:** Why was that constraint unavailable or ignored at that moment?
5. **Capability:** What repeatable capability would prevent recurrence?

If the chain stops at “did not know,” “was careless,” or “grammar was weak,” continue downward.

## Core error codes

| Code | Mechanism | Distinguishing test |
|---|---|---|
| `V-UNK` | Form or lemma unknown | Cannot recognize or explain after seeing it in context |
| `V-RET` | Known knowledge not retrieved | Recognizes promptly after cue and can explain prior learning |
| `V-MIS` | Wrong sense or near-synonym selected | Knows the form but maps it to an incompatible context meaning |
| `CHUNK` | Multiword frame unavailable | Individual words are known; the unit is not parsed as a chunk |
| `MORPH` | Form, agreement, tense, voice, or participle failure | Lemma fits semantically but required form does not |
| `SLOT` | Part of speech or syntactic slot mismatch | Candidate fails the local structural signature |
| `VAL` | Valency, transitivity, complement, or preposition failure | Verb meaning seems plausible but its argument frame fails |
| `CLAUSE` | Clause boundary, reference, nesting, or ellipsis failure | Local words are known but proposition structure is wrong |
| `LOGIC` | Stance, contrast, cause, sequence, or reference failure | Sentence-level parse works; discourse relation does not |
| `OPTION` | Candidate-set interference or cascade | A prior placement removes or biases a later viable option |
| `STRAT` | Chosen procedure causes systematic loss | The process repeatedly discards usable evidence |
| `TIME` | Time constraint blocks an otherwise available process | Untimed reconstruction succeeds without teaching |
| `ATT` | Attention lapse at a known checkpoint | Rule is known and retrievable, but evidence was not inspected |
| `CARE` | Pure execution slip | Knowledge and checking process are stable; mistake is copying, marking, or accidental omission |
| `MATERIAL` | Source or answer ambiguity | Competing keys or mismatched versions explain the discrepancy |

Use multiple codes only when each represents a necessary link. Avoid decorating every item with all plausible labels.

## Strict carelessness test

Use `CARE` only if all are true:

1. The learner knew and could retrieve the rule at the time.
2. The intended reasoning was correct before the final action.
3. The error came from copying, marking, skipping, or another execution fault.
4. The same conceptual error does not recur across items.

Otherwise prefer the deeper mechanism, such as `ATT`, `SLOT`, `VAL`, or `STRAT`.

## Answer topology

Inspect the relationship between the learner’s candidate set and the reference set before item teaching:

- correct candidate absent from the learner’s set;
- correct candidate present but misplaced;
- direct pair swap;
- multi-item cascade caused by one early allocation;
- extra distractor replacing one missing candidate;
- errors clustered by paragraph, structure, or decision order.

High candidate-set overlap with low positional accuracy suggests mapping or validation failure rather than simple non-recognition.

## Correct-answer audit

Classify every correct response:

- `STABLE`: accurate meaning, structure, relation, and reproducible reason;
- `STRUCTURE_HIT`: selected through form or syntax without accurate meaning;
- `APPROXIMATE`: directionally reasonable but conceptually imprecise;
- `ELIMINATION_HIT`: obtained mainly from remaining choices;
- `LUCKY`: no reproducible basis.

Only `STABLE` counts as provisional mastery. The other classes remain in the evidence set and may influence the bottleneck diagnosis.

## Aggregation rules

Promote an item-level mechanism into a bottleneck only if it:

- recurs across multiple items;
- explains a cascade or large share of the score;
- affects construction of the whole task model; or
- is high-leverage and directly testable.

Keep the final bottleneck set between one and three. Place lower-priority findings in a backlog.
