# Output and record templates

## Lightweight baseline capture

Use before revealing answers:

```markdown
## Baseline capture

- Experiment ID:
- Material fingerprint:
- Start / end / interruption:
- Original response:
- Certain / hesitant / guessed / blank:
- Revisions:
- Unknown words or components:
- Unparsed sentences or task states:
- Strategy and order used:
- Possible contamination:
```

Do not force every field when logging would disrupt the task. Mark missing fields rather than inventing them.

## Formal experiment record

Start with machine-checkable metadata:

```markdown
---
experiment_id: "YYYY-MM-DD/source/task/items/fingerprint"
phase: "capture"
baseline_status: "clean-baseline"
evidence_frozen: true
answer_authority: "third-party"
primary_bottleneck_count: 1
intervention_count: 1
next_experiment_type: "near-transfer"
---
```

Allowed values:

- `phase`: `baseline`, `diagnosis`, `intervention`, `validation`, `capture`
- `baseline_status`: `clean-baseline`, `partial-baseline`, `practice-only`
- `next_experiment_type`: `delayed-retrieval`, `near-transfer`, `far-transfer`, `none`

Then use:

```markdown
# Experiment title

## 【实验身份】

## 【原始假设】

## 【真实行为】

## 【真实反馈】

## 【逐项因果诊断】

## 【正确答案审计】

## 【能力诊断】

## 【证伪】

## 【最小干预】

For each intervention include: trigger, action, visible trace, target mechanism.

## 【下一实验】

Include: hypothesis, material, invariants, changed action, execution metric, outcome metric, support criterion, falsification criterion.

## 【可迁移经验】

## 【证据边界】

Distinguish OBSERVED, REPORTED, INFERRED, and UNVERIFIED claims.

## 【项目更新】
```

## Item-level diagnosis table

| Item | Original response | Confidence | Actual cue used | Correct constraint | Break point | Error code | Evidence level |
|---|---|---|---|---|---|---|---|

## Correct-answer audit table

| Item | Result | Reason used | Audit class | Missing understanding | Retest needed |
|---|---|---|---|---|---|

## Vocabulary and chunk entry

```markdown
### Surface form

- Lemma:
- Part of speech / morphological environment:
- Original sentence fragment:
- Meaning in this context:
- Chunk or valency frame:
- Original misreading:
- Retrieval cue:
- Status: unseen / explained / retrieved / transferred
```

Never mark an entry “mastered” immediately after explanation.
