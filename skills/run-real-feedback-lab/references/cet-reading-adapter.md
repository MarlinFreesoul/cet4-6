# CET reading adapter

Use this adapter only for CET reading. Current strong evidence comes from Section A constrained-choice cloze; treat Section B and Section C extensions as provisional until their own baselines exist.

## Section A workflow

### Before filling

- Build only a provisional topic and stance model.
- Mark each candidate’s likely part of speech and salient morphology without forcing a single meaning too early.

### For each blank

Create a slot signature:

`part of speech + required form + tense/voice + valency + complement/preposition + semantic role + discourse stance`

Require four checks:

1. grammar;
2. collocation or valency;
3. precise sentence meaning;
4. paragraph and passage logic.

Do not accept a candidate only because the broad meaning seems plausible or because other candidates have been used.

### When the passage model changes

If later paragraphs clarify the debate, stance, referent, or time sequence, rescan earlier provisional answers. Record whether the rescan happened; this is a process metric.

### After filling

- Read every completed sentence independently.
- Recheck paired swaps and cascades.
- Distinguish “candidate recognized” from “candidate mapped to the correct slot.”
- Preserve remaining uncertainty rather than converting elimination into confidence.

## Sentence reconstruction protocol

For an uncertain sentence:

1. circle finite verbs, auxiliaries, and copulas;
2. assign a subject to each predicate;
3. mark clause boundaries and connector roles;
4. resolve pronoun antecedents;
5. restore ellipsis or reduced relatives;
6. test verb valency and complement frames;
7. temporarily remove modifiers;
8. rebuild the proposition and reread it in discourse context.

## Diagnostic distinctions specific to Section A

- High word-pool overlap plus low slot accuracy: inspect `SLOT`, `VAL`, `MORPH`, `OPTION`, and validation strategy before concluding `V-UNK`.
- A correct choice with a wrong gloss: classify as `STRUCTURE_HIT` or `APPROXIMATE`, not stable mastery.
- A wrong choice forced by an earlier allocation: diagnose both the local constraint failure and the cascade mechanism.
- A word learned during review: test later retrieval separately from unseen transfer.

## Current personalized hypotheses

Treat these as hypotheses, not permanent traits:

- global passage understanding may emerge later than local decisions;
- viable candidates may be recognized but mapped to the wrong slots;
- sentence reconstruction, slot signatures, and independent rereading may be high-leverage interventions;
- precise contextual meaning, chunks, and valency may constrain performance more than raw vocabulary count.

Promote or retire each hypothesis only through unseen comparable samples.
