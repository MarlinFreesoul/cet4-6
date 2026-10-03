---
name: run-cet4-word-bank-cloze
description: Run evidence-first baselines, answer checks, causal reviews, minimal interventions, and transfer tests for CET4 Part III Reading Comprehension Section A, officially described as vocabulary comprehension / word-bank cloze (大学英语四级阅读词汇理解、选词填空), normally a 200–250-word passage with 10 blanks and 15 one-use candidates. Use for any year or set that matches this exact CET4 question-type fingerprint, including items 26–35; do not use for Listening Section A, long matching reading, careful-reading multiple choice, CET6, IELTS, or generic cloze without an explicit adaptation.
---

# Run CET4 Word-Bank Cloze

Run the same evidence-first protocol on any CET4 Reading Section A passage that matches the official word-bank-cloze format. Preserve the attempt before teaching, diagnose the learner’s mapping process rather than merely explain the key, change no more than two behaviors, and verify transfer on unseen passages.

## Confirm the exact question type

Read [references/official-spec.md](references/official-spec.md) before the first use, whenever the year changes, or whenever the paper format is uncertain.

Apply this skill only when the material matches all stable features:

- CET4 written test, Part III Reading Comprehension, Section A;
- one vocabulary-comprehension passage;
- approximately 200–250 words under the current official specification;
- 10 blanks, normally numbered 26–35;
- 15 lettered candidates, normally A–O;
- each candidate may be used no more than once;
- the task is to restore the passage through contextual vocabulary understanding and use.

If a material violates a structural feature, mark `FORMAT_DRIFT`, stop automatic reuse, and verify the current official specification. Do not force this protocol onto a different task merely because it is called “Section A.”

## Separate official requirements from lab methods

Treat these as constraints stated in the published official syllabus and structure pages:

- task structure, passage length, item and option counts, overall weighting, shared reading time, and the stated construct;
- the broader CET reading abilities stated in the official syllabus.

Treat the one-use rule and recurring item labels as source-paper directions that must also pass material intake. Do not mislabel a recurring paper convention as a separately reported scoring rule.

Treat these as Real Feedback Lab operational methods, not official scoring rules:

- slot signatures;
- sentence reconstruction;
- answer-topology analysis;
- correct-answer stability classes;
- causal error codes;
- minimal-intervention experiments.

Never describe an operational method as a requirement of the examination committee.

## Select the experiment state

Identify one state before responding:

1. **MATERIAL_CHECK** — Verify the complete passage, 10 blanks, 15 candidates, and identity.
2. **BASELINE_ACTIVE** — The learner is independently answering.
3. **EVIDENCE_FREEZE** — The attempt is complete, but raw evidence is not fixed.
4. **DIAGNOSIS** — The original attempt and a reference key are available.
5. **INTERVENTION** — One to three bottlenecks are supported.
6. **VALIDATION** — Run delayed retrieval or unseen near transfer.
7. **CAPTURE** — Save the record, learner model, and next experiment.

Do not skip states. During `BASELINE_ACTIVE`, say “先留下真实反馈，做完再拆。” when the learner requests help that would contaminate the attempt.

## Run the protocol

### 1. Check and identify the material

Create:

`year-month / set and source / CET4-RC-Section-A / items / opening words`

Confirm that the passage and all 15 candidates are present. Record whether the key is official, publisher-provided, teacher-provided, community-derived, or agent-inferred. Use opening words and item range to resolve set-number ambiguity.

Read [references/evidence-and-gates.md](references/evidence-and-gates.md) for format, contamination, timing, and authority gates.

### 2. Protect the baseline

During `BASELINE_ACTIVE`:

- Do not define words, parse sentences, name tested structures, reveal difficulty, eliminate candidates, or disclose answers.
- Record only non-contaminating metadata and learner-supplied notes.
- Keep logging lightweight enough not to alter performance.
- Distinguish an isolated Section A attempt from a full 40-minute reading-block attempt.

The official specification assigns 40 minutes to the whole reading part, not a separate official limit to Section A. Do not invent an official Section A time limit.

### 3. Freeze the evidence before explanation

Save at least:

- original 26–35 answer sequence;
- certain / hesitant / guessed / blank status;
- active time, interruptions, and scope mode;
- answer order and revisions;
- first-pass passage model and when it changed;
- unknown words, uncertain senses, unparsed sentences, and forced choices;
- the learner’s “当时我以为……” reasoning.

If the learner wants the key immediately, capture the answer sequence, confidence, and overall approach first.

### 4. Score without pretending to report an official CET score

Report raw performance as `x/10`, plus guesses and blanks. State that Section A carries 5% of the test under the current official structure.

Do not convert each item into a fixed number of the 710 reported-score scale. CET reported scores are norm-referenced, and Section A has no separately reported official score.

### 5. Analyze the word-bank topology

Before teaching individual blanks, compare the learner’s selected word set with the reference set:

- correct candidates never selected;
- distractors selected;
- correct candidates placed in wrong blanks;
- pair swaps;
- cascades caused by an earlier allocation;
- candidates chosen only because other words were already used.

Calculate and report candidate-set overlap separately from positional accuracy. High overlap with low placement accuracy points first toward mapping and validation failures, not automatically toward raw vocabulary shortage.

### 6. Reconstruct each consequential decision

For every error and unstable correct answer, trace:

`result → actual cue used → required constraint → break point → mechanism → trainable capability`

Use this constraint order:

1. required part of speech;
2. inflection or morphological form;
3. sentence skeleton and clause role;
4. valency, complement, preposition, and collocation;
5. precise contextual meaning;
6. lexical or grammatical cohesion;
7. paragraph stance and passage model;
8. one-use bank allocation and independent rereading.

Read [references/section-a-protocol.md](references/section-a-protocol.md) for the exact blank-by-blank procedure and [references/diagnosis-taxonomy.md](references/diagnosis-taxonomy.md) for causal codes and correct-answer audits.

### 7. Audit correct answers

Classify every correct blank as:

- `STABLE` — reproducible lexical, grammatical, and discourse justification;
- `STRUCTURE_HIT` — structure works but exact meaning is unavailable;
- `APPROXIMATE` — direction is right but meaning or relation is imprecise;
- `ELIMINATION_HIT` — mainly obtained from remaining candidates;
- `LUCKY` — no reproducible basis.

Only `STABLE` counts as provisional mastery.

### 8. Aggregate and intervene minimally

Aggregate item mechanisms into one to three bottlenecks. Activate no more than two interventions. Express each as:

`trigger → action → visible trace → target mechanism`

Preserve all other findings in a backlog. Read [references/experiment-design.md](references/experiment-design.md) before selecting an intervention or comparison passage.

### 9. Validate on the right evidence

- Use the reviewed passage after a delay to test retrieval, not transfer.
- Use an unseen CET4 Section A passage matching the official fingerprint to test near transfer.
- Keep source quality, scope mode, and timing conditions comparable.
- Measure intervention execution separately from intervention efficacy.
- Prefer two unseen passages before promoting a pattern into a stable learner rule.

### 10. Capture and update

Read [references/output-templates.md](references/output-templates.md) and produce the formal record. Save vocabulary as contextual forms, chunks, valency frames, prior misreadings, and retrieval cues.

Read [references/learner-model.md](references/learner-model.md) before choosing the next experiment. Update that file only when new evidence confirms, weakens, or replaces a learner hypothesis.

Validate a saved Markdown record with:

```bash
python3 scripts/validate_section_a_record.py path/to/record.md
```

Fix validation errors before calling the experiment complete.

## Stop the review

Stop explaining and move to the next passage when:

- the answer topology is known;
- each consequential error and unstable correct answer has a supported cause or explicit unknown;
- one to three bottlenecks explain the important pattern;
- one or two interventions have visible execution traces;
- the next unseen Section A experiment can support or falsify the hypothesis;
- additional explanation would not change the intervention or experiment.

## Preserve epistemic discipline

- Do not treat one passage as a stable ability profile.
- Do not treat a learned old passage as transfer evidence.
- Do not label broad passage understanding as sufficient when local restoration fails.
- Do not call every unknown word the root cause; test whether the correct candidate was already in the learner’s pool.
- Do not call an answer mastered merely because it was correct.
- Do not apply this Skill to a changed future format without passing `MATERIAL_CHECK` again.
