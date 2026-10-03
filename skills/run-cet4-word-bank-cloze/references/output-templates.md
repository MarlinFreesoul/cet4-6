# CET4 Section A record templates

## Lightweight pre-key capture

```markdown
## Baseline capture

- Paper ID:
- Opening words:
- Scope mode: isolated-section-a / full-reading-block
- Start / end / interruptions:
- Original 26–35 answers:
- Certain / hesitant / guessed / blank:
- Answer order and revisions:
- First-pass passage model and update point:
- Unknown words / uncertain senses:
- Unparsed sentences:
- Forced choices:
- Possible contamination:
```

Mark missing evidence instead of inventing it.

## Formal record metadata

```markdown
---
experiment_id: "YYYY-MM/set-source/cet4-rc-section-a/26-35/opening-words"
task_type: "cet4-word-bank-cloze"
format_match: true
scope_mode: "isolated-section-a"
item_range: "26-35"
blank_count: 10
option_count: 15
single_use: true
phase: "capture"
baseline_status: "clean-baseline"
evidence_frozen: true
answer_authority: "third-party"
raw_score: 0
primary_bottleneck_count: 1
intervention_count: 1
next_experiment_type: "near-transfer"
---
```

Allowed values:

- `scope_mode`: `isolated-section-a`, `full-reading-block`
- `phase`: `baseline`, `diagnosis`, `intervention`, `validation`, `capture`
- `baseline_status`: `clean-baseline`, `partial-baseline`, `practice-only`
- `answer_authority`: `official`, `publisher`, `teacher`, `third-party`, `agent-inferred`, `disputed`
- `next_experiment_type`: `delayed-retrieval`, `near-transfer`, `none`

## Formal report

```markdown
# CET4 Section A experiment

## 【题型合规检查】

## 【实验身份】

## 【原始假设】

## 【真实行为】

## 【真实反馈】

## 【答案拓扑】

## 【逐空因果诊断】

## 【正确答案审计】

## 【能力诊断】

## 【证伪】

## 【最小干预】

## 【下一实验】

## 【可迁移经验】

## 【证据边界】

## 【项目更新】
```

## Blank-level diagnosis table

| Blank | Original | Confidence | Actual cue | Slot signature | Correct constraint | Break point | Code | Evidence |
|---|---|---|---|---|---|---|---|---|

## Answer-topology table

| Measure | Result |
|---|---|
| Positional accuracy | /10 |
| Candidate-set overlap | /10 |
| Missed correct candidates | |
| Selected distractors | |
| Misplaced correct candidates | |
| Swaps / cascades | |

## Contextual vocabulary entry

```markdown
### Surface form

- Lemma:
- Part of speech / morphology:
- Original sentence and adjacent context:
- Contextual sense:
- Chunk / valency / complement frame:
- Original misreading:
- Retrieval cue:
- Status: unseen / explained / retrieved / transferred
```

Never mark an item mastered immediately after explanation.
