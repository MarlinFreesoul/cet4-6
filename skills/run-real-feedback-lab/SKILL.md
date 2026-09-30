---
name: run-real-feedback-lab
description: Run evidence-first learning experiments from untouched baseline through causal diagnosis, minimal intervention, transfer testing, and method capture. Use when a learner wants to do a real task before receiving help; review CET4/CET6/IELTS or another complex-skill attempt; distinguish knowledge gaps from retrieval, parsing, strategy, time, or attention failures; turn mistakes and unstable correct answers into a small next experiment; or maintain a versioned Real Feedback learning system.
---

# Run Real Feedback Lab

Treat each attempt as an experiment, not as an excuse to deliver a lesson. Preserve the baseline, reconstruct what actually happened, identify the smallest causal bottleneck, change no more than two factors, and demand new evidence before declaring improvement.

## Select the current state

Identify one state before responding:

1. **BASELINE_ACTIVE** — The learner is still doing the task.
2. **EVIDENCE_FREEZE** — The learner has finished, but raw evidence is not fixed.
3. **DIAGNOSIS** — Answers and raw evidence are available.
4. **INTERVENTION** — The causal diagnosis is sufficient.
5. **VALIDATION** — A delayed-retrieval or unseen-transfer attempt is being run.
6. **CAPTURE** — Results and method changes are being saved.

Do not skip forward merely because the learner asks for advice. If the baseline is active, say “先留下真实反馈，做完再拆。” and only record non-contaminating metadata.

## Enforce the gates

Pass these gates in order:

- **G0 Material identity:** Fix date/source, part or task type, item range, and opening words or another unique fingerprint.
- **G1 Baseline integrity:** Confirm no answers, hints, word definitions, or strategy coaching were introduced during the attempt. Record contamination if it occurred; do not conceal it.
- **G2 Evidence freeze:** Preserve the original response, confidence, guesses, blanks, timing, sequence, revisions, confusing words or passages, and the learner’s contemporaneous reasoning before explanation.
- **G3 Causal adequacy:** Explain the important errors and unstable correct answers through a causal chain, not a label such as “careless” or “weak vocabulary.”
- **G4 Intervention eligibility:** Aggregate findings into one to three bottlenecks and select only one or two observable behavior changes.
- **G5 Testability:** Specify new material, controlled conditions, changed behavior, metrics, support criteria, and falsification criteria.

Read [references/evidence-and-gates.md](references/evidence-and-gates.md) whenever evidence is incomplete, contaminated, disputed, or being converted into a formal record.

## Run the experiment

### 1. Protect the baseline

During `BASELINE_ACTIVE`:

- Confirm the task identity and record times or answers without interpreting them.
- Do not reveal difficulty, tested concepts, vocabulary, sentence structure, solution methods, or answers.
- Keep logging optional and lightweight; never damage task performance to collect perfect data.
- If the learner asks for help that belongs inside the task, preserve the request as evidence and defer teaching.

### 2. Freeze raw evidence

During `EVIDENCE_FREEZE`:

- Ask only for missing evidence that could materially change the diagnosis.
- Prefer the learner’s “当时我以为……” account over a polished retrospective explanation.
- Separate exact facts from recalled reports, agent inferences, and unverified hypotheses.
- Never invent precise timing from message timestamps.
- Record the authority of answer keys and source materials.

Use the capture block in [references/output-templates.md](references/output-templates.md).

### 3. Diagnose causes

During `DIAGNOSIS`:

1. Score the outcome without teaching yet.
2. Inspect the **answer topology**: missing candidates, extra distractors, misplaced correct candidates, swaps, cascades, and clustering.
3. Reconstruct behavior chronologically: first pass, model-formation point, item order, local decisions, revisions, and stopping rule.
4. For each consequential item, trace:

   `observable result → decision made → constraint missed or misused → cognitive mechanism → trainable capability`

5. Audit correct answers as stable, structure-hit, approximate inference, elimination-hit, or lucky.
6. Assign an evidence level to every diagnosis.

Read [references/diagnosis-taxonomy.md](references/diagnosis-taxonomy.md) for error codes, causal tests, answer-topology analysis, and the strict test for “carelessness.”

For CET reading, also read [references/cet-reading-adapter.md](references/cet-reading-adapter.md). Do not generalize its Section A rules to other sections without new evidence.

### 4. Choose the minimum intervention

During `INTERVENTION`:

- Cluster item-level mechanisms; do not turn every discovery into homework.
- Rank possible interventions by recurrence, explanatory reach, observability, transfer value, and cost.
- Select one or two actions that occur at a precise decision point.
- Express each intervention as `trigger → action → visible trace`.
- Preserve other findings in the backlog without activating them.

Example:

`When a sentence remains uncertain → mark finite verbs and match each to a subject → leave the marks visible before selecting an option.`

Read [references/experiment-design.md](references/experiment-design.md) before prescribing an intervention or next experiment.

### 5. Validate rather than celebrate

During `VALIDATION`:

- Use delayed retrieval to test retention of the current material.
- Use unseen, comparable material to test transfer.
- Keep conditions stable except for the selected intervention.
- Measure both outcome and process: accuracy, time, invalid answers, misplaced candidates, guesses, intervention execution, and error recurrence.
- Treat one improved sample as encouraging evidence, not proof. Prefer two unseen samples before promoting a pattern into a stable personal rule.
- If the intervention was not executed, do not infer that it failed; test execution separately from efficacy.

### 6. Capture and version

During `CAPTURE`:

- Produce the fixed Real Feedback report from [references/output-templates.md](references/output-templates.md).
- Preserve raw evidence separately from later interpretation.
- Save vocabulary as contextual forms, chunks, valency frames, prior misreadings, and retrieval prompts rather than isolated translations.
- Update the SOP only when new evidence changes the procedure.
- Mark personal rules as provisional until repeated transfer evidence supports them.
- If a Markdown experiment record exists, run:

```bash
python3 scripts/validate_experiment_record.py path/to/record.md
```

Fix errors before calling the record complete. Warnings may remain only when the missing evidence is explicitly documented.

## Stop the review

Stop explaining and move to the next experiment when:

- the major behavior chain is reconstructed;
- each consequential error and unstable correct answer has a supported cause or an explicit unknown;
- one to three bottlenecks explain most of the result;
- one or two interventions are operationalized;
- the next experiment can confirm or falsify the hypothesis;
- further explanation would add knowledge but would not change the intervention or test.

## Preserve epistemic discipline

- Never equate score with diagnosis.
- Never equate recognition with recall, recall with fluent use, or one correct answer with mastery.
- Never use “vocabulary,” “grammar,” “strategy,” or “carelessness” as terminal causes.
- Never rewrite a contaminated attempt as a clean baseline.
- Never claim transfer from reviewing the same material.
- Never create a large study plan when the evidence supports only a small next test.
