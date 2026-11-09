# TakeMeter — Rulebook, Game Analysis, Fan Take

## What This Does

Sports conversations jump between “what's the call?”, “what happened?”, and “here's my take.” TakeMeter sorts complete answers from [Sports Stack Exchange](https://sports.stackexchange.com/) into **rulebook**, **game_analysis**, and **fan_take**. The distinction is what the writer is doing, not whether they pasted a link. It covers sports including basketball, football, cricket, baseball, tennis and hockey, and it does not certify that a post is correct.

The criteria were committed before training the three-class model. [Community notes](notes/community.md) record the reading sample and the distinctions observed in real posts.

Repository for both units: [Yosias1706/ai201-project3-takemeter-starter-v2026](https://github.com/Yosias1706/ai201-project3-takemeter-starter-v2026).

## Label Taxonomy

### rulebook — “What's the call?”

**Definition:** The main point explains or applies a sports rule, officiating decision, eligibility requirement, scoring convention, or competition procedure.

**Example 1 — wicketkeeper position**

> The wicketkeeper must remain wholly behind the wicket until the ball passes the wicket or hits the bat or batter.If the umpire deemed the keepers gloves were in front of the wicket a no-ball should be given.

— [Graham](https://sports.stackexchange.com/users/37525/graham), [answer 30350](https://sports.stackexchange.com/a/30350), CC BY-SA 4.0.

**Example 2 — continuing a pool turn**

> Basically, yes. You don't even need to call "combo". As long as the cue ball strikes your group first and the ball you call goes in, you get the next shot.

— [kesarling](https://sports.stackexchange.com/users/36019/kesarling), [answer 30173](https://sports.stackexchange.com/a/30173), CC BY-SA 4.0.

### game_analysis — “Break it down.”

**Definition:** The main point reports or explains sports events, records, tactics, equipment, or performance through concrete observations, examples, or mechanisms, without primarily prescribing a rule or personal recommendation.

**Example 1 — Olympic medalists**

> William Eastman Buchan (Star class) and William Carl Buchan (Flying Dutchman class) both won gold medals in separate sailing events in the 1984 Olympics (https://en.wikipedia.org/wiki/Sailing_at_the_1984_Summer_Olympics#Medal_summary).

— [user37911](https://sports.stackexchange.com/users/37911/user37911), [answer 30382](https://sports.stackexchange.com/a/30382), CC BY-SA 4.0.

**Example 2 — bowling speed**

> He did actually hit the 160 kmph mark vs New Zealand in an ODI in 2002 at Pakistan.

— [Guest](https://sports.stackexchange.com/users/37579/guest), [answer 30354](https://sports.stackexchange.com/a/30354), CC BY-SA 4.0.

### fan_take — “Here's my take.”

**Definition:** The main point is a personal judgment, prediction, recommendation, anecdote, joke, or speculative explanation rather than a rule decision or concrete factual account.

**Example 1 — cricket-bat advice**

> The best is to stand it up next to you, the top of the handle should be around your hip/waist. Or hang it down straight by your side and keep your arm relaxed. The toe should just about touch the ground. But height is secondary, weight matters more imo - grab a few and take some shadow shots, go with whatever feels balanced and not too toe-heavy. Kids are usually fit by bat number (0-6) and adults are fit SH or LH based on height.

— [Abhi raj](https://sports.stackexchange.com/users/37581/abhi-raj), [answer 30361](https://sports.stackexchange.com/a/30361), CC BY-SA 4.0.

**Example 2 — hockey-tape recommendation**

> Athletic Tape is a great alternative as it’s similar in texture and adhesive strength to hockey tape. It’s often cheaper and can be found at most sports stores or online.

— [Malik Junaid](https://sports.stackexchange.com/users/31798/malik-junaid), [answer 29927](https://sports.stackexchange.com/a/29927), CC BY-SA 4.0.

### The hardest boundary and decision rule

The hardest boundary is **game_analysis versus fan_take**: both can explain their reasoning and cite sources. Read the whole answer and classify its main conclusion:

1. If it decides what is permitted, penalized, awarded, eligible or officially counted, use **rulebook**. Merely mentioning a rule does not qualify.
2. Otherwise, if its main conclusion recommends, evaluates, predicts, recounts personal experience, jokes or proposes an unestablished explanation, use **fan_take**.
3. Otherwise, a concrete event account, record, comparison, mechanism or tactical explanation is **game_analysis**.

A quoted athlete's recommended drill is still a fan take; an uncited factual claim is still game analysis. An emotional aside does not outweigh an answer's operative rule decision. Labels describe conversational purpose, not factual truth, writing quality or source reliability. [Taxonomy notes](notes/taxonomy.md) contain eight synthetic stress tests, excluded from training, and the competing cases for the difficult boundary.

## The Dataset

**Source:** 200 complete public Sports Stack Exchange answers, retrieved from two pages of the public API in descending creation order on October 26, 2026 UTC. No login was required. Each complete answer was classified using the three label definitions.

**Annotation:** Read each complete answer for its main purpose, assign one label, then review mixed cases with the decision order. The note column records the public answer ID and rationale. This is not an unaided cold-labeling set. The single unsplit [labels.csv](labels.csv) is the notebook input; no split was performed during collection or labeling.

| Label | Count | Share |
|---|---:|---:|
| rulebook | 99 | 49.5% |
| game_analysis | 71 | 35.5% |
| fan_take | 30 | 15.0% |
| **Total** | **200** | **100%** |

There are zero blank texts and zero exact duplicate texts. No label exceeds the course's 70% cap or the project's 60% target. Fan takes are less common in this question-and-answer community than rules and factual explanations; their small evaluation sample is a real limitation.

**Three hard cases**

1. [30360 — solo goalball drills](https://sports.stackexchange.com/a/30360): the quoted athlete routine could look like game_analysis, but the answer concludes with training recommendations. **fan_take** wins because the purpose is advice.
2. [30183 — impossible cricket situation](https://sports.stackexchange.com/a/30183): the opening complaint sounds like a fan_take, but the actual answer uses Law 29 to decide not out. **rulebook** wins because the rule decision is the operative conclusion.
3. [30149 — swinging-gate formation](https://sports.stackexchange.com/a/30149): the low-risk assessment could sound like a fan_take, but the answer chiefly explains the tactical sequence and defense's response. **game_analysis** wins because this is an explanation rather than a recommendation to the reader.

[Additional decisions](notes/hard-cases.md) include numeric arguments that are still opinions and specific game incidents that are analysis rather than general rule interpretations.

**Provenance and limitations:** [sources.csv](data/sources.csv) links every answer to its author and license. [Frozen source snapshots](data/source/) retain the full HTML. Conversion preserves all prose, quotations, tables, link destinations, image descriptions/URLs and embedded-media URLs. Image pixels and video frames are not model inputs. Contributions retain their authors' CC BY-SA licenses; adaptations and attribution are described in [source documentation](data/source/README.md).

This is a recent-answer convenience sample, not a random sample of sports fans. Multiple answers may share a question, so the supplied row-level split is not a question-group holdout. No exact duplicate crosses splits, but related questions can create topical dependence. Posts remain whole in the CSV; the model sees at most 128 tokens, which can omit a late conclusion crucial to the main-purpose rule.

## The Training Run

**Starting model:** `distilbert-base-uncased` with a newly initialized three-class head.

| Setting | Value |
|---|---|
| Labels, in ID order | rulebook, game_analysis, fan_take |
| Epochs | 3 |
| Learning rate | 0.00002 |
| Batch size | 16 |
| Maximum tokens | 128 |
| Seed | 42 |
| Device | Apple Silicon GPU, MPS |
| Python | 3.13.0 |
| PyTorch | 2.14.1 |

Training hyperparameters remain at the starter defaults. The model was initialized from the base checkpoint with a new three-class head.

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| rulebook | 69 | 15 | 15 |
| game_analysis | 49 | 11 | 11 |
| fan_take | 21 | 5 | 4 |
| **Total** | **139** | **31** | **30** |

The supplied 70/15/15 procedure produces 139/31/30 due to rounding in its second split. **fan_take has only four test examples:** one error changes its recall by 25 percentage points. Its per-label metrics will be especially unstable across seeds; this is recorded now for Unit 6.

Notebook sections 1–5 completed. [results.json](results.json) contains the new three-class metrics and device information; [test_split.csv](test_split.csv) contains the matching held-out posts. The new [criteria.md](criteria.md) and re-labeled dataset were committed first. The results are kept as obtained, without adjusting criteria or picking a better seed afterward. The run does not save a standalone checkpoint; re-executing the notebook recreates the model in memory.

The environment check passed all ten checks. The notebook's data check accepted this dataset and warned about the small fan_take test set during splitting. At the end of Unit 5, notebook sections 6–7 had not been run. Unit 6 results are in the sections below.

## Reproducing the Project

Follow [RUNNING.md](RUNNING.md), install the requirements in `.venv`, run `python test.py`, select that kernel, and execute sections 1–5 of [takemeter.ipynb](takemeter.ipynb). The committed CSV and notebook are sufficient to run training.

The new milestone commits document the reading, definitions, criteria, relabeling, training and final write-up in that order. No stretch features are claimed in either unit. **Note for reproducing:** the notebook now has `EPOCHS = 10` (the Unit 6 improvement). Set it back to 3 and `RUN_LABEL = "before"` to reproduce the before-run; leave it at 10 with `RUN_LABEL = "after"` to reproduce the after-run.

---

## Baseline vs. Trained

**Expectation recorded before running the baseline:** The zero-shot model may distinguish factual explanations and personal recommendations better than the small fine-tuned model, whose Unit 5 run predicted only rulebook. Rule-related language should be the easiest category for both. This expectation was written before baseline evaluation, but after the Unit 5 scores had already been viewed; it is not a blind prediction of those known scores.

**Prediction (one sentence):** The trained model will beat the baseline only on `rulebook`, because rule vocabulary is the one signal 139 training posts can teach it, while the zero-shot model will do better on `game_analysis` because it can read the definition rather than needing examples.

Both models were scored on the same 30 held-out posts in [test_split.csv](test_split.csv) (seed 42 split from Unit 5). The baseline is `facebook/bart-large-mnli`, zero-shot, prompted with the three definitions in [label_definitions.txt](label_definitions.txt). Results: [baseline_results.json](baseline_results.json).

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.467 | 0.500 | +0.033 |
| Macro F1 | 0.300 | 0.222 | -0.078 |
| F1 — `fan_take` | 0.000 | 0.000 | +0.000 |
| F1 — `game_analysis` | 0.286 | 0.000 | -0.286 |
| F1 — `rulebook` | 0.615 | 0.667 | +0.051 |

**What the definitions were worth.** I also ran the baseline with no definitions file, so it saw only the bare label names ([baseline_results_bare_names.json](baseline_results_bare_names.json)). The reported baseline above is the definitions run.

| Measure | Bare names | With definitions | Gain from definitions |
|---|---|---|---|
| Overall accuracy | 0.167 | 0.467 | +0.300 |
| Macro F1 | 0.128 | 0.300 | +0.172 |

**Reading it.** The prediction held: the trained model's whole edge (+0.033 accuracy, one post) comes from `rulebook`, and the baseline wins on `game_analysis`. But the edge is hollow. The Unit 5 trained model predicted `rulebook` for all 30 posts, so its 0.500 accuracy is exactly the majority-class rate (15/30). A model that always guesses the commonest label ties a general model that has never seen a training example. Macro F1, which punishes ignoring labels, favours the baseline. Neither model found a single `fan_take`. The baseline took several seconds per post on MPS, against a fraction of a second for the trained model.

## Run Log — Before

**Device:** Apple Silicon GPU (MPS), PyTorch 2.14.1, Python 3.13.0, `distilbert-base-uncased`, 3 epochs, learning rate 2e-5, batch 16, 128 tokens. Seeds 42, 7 and 2024, each a fresh stratified 70/15/15 split (139 / 31 / 30) and a fresh model. Raw output: [results_three_seeds_before.json](results_three_seeds_before.json).

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.500 | 0.500 | 0.500 | 0.000 |
| Macro F1 | 0.222 | 0.222 | 0.222 | 0.000 |
| F1 — `rulebook` | 0.667 | 0.667 | 0.667 | 0.000 |
| F1 — `game_analysis` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `fan_take` | 0.000 | 0.000 | 0.000 | 0.000 |
| Precision — `rulebook` | 0.500 | 0.500 | 0.500 | 0.000 |
| Most-confident third accuracy | 0.900 | 0.900 | 1.000 | 0.100 |
| Least-confident third accuracy | 0.100 | 0.100 | 0.100 | 0.000 |

Seed 42 reproduced the Unit 5 `results.json` to the digit on the same device.

**The zero spread is not stability.** The notebook's note says "stable enough to trust", but every seed produced the same degenerate model: it predicts `rulebook` for every test post. Each stratified test split holds 15 / 11 / 4 posts, so a constant guess scores exactly 15/30 every time. The three trials do measure something real, though: the collapse is not a bad draw. It happens on every split.

### Confusion matrix (seed 42; seeds 7 and 2024 are identical)

| true \ predicted | rulebook | game_analysis | fan_take |
|---|---|---|---|
| **rulebook** | 15 | 0 | 0 |
| **game_analysis** | 11 | 0 | 0 |
| **fan_take** | 4 | 0 | 0 |

**Biggest confusion:** all 11 real `game_analysis` posts were called `rulebook` and none went the other way. The model never learned the game_analysis/rulebook boundary, or any boundary: it learned the class prior and nothing else.

## Agreement Report

**Rate: 30 / 30 = 100%** against the staff labels in [data/staff_labels.csv](data/staff_labels.csv), applying the definitions in [data/staff_taxonomy.md](data/staff_taxonomy.md). My labels, committed before the staff file was opened: [my_staff_labels.csv](my_staff_labels.csv). Output: [agreement_results.json](agreement_results.json).

**Disagreements: none**, so there is nothing to sort into the loose / gap / ambiguous piles. Instead, these are the five posts where I thought a disagreement was most likely, and why the written rules settled each one:

| Post | Both said | The competing label | Why the rule settles it |
|---|---|---|---|
| sp_014 "Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story…" | hot_take | analysis | Rule 1's own example. The 3% decorates a conclusion already reached ("obviously"); no reasoning connects the number to the cause. |
| sp_005 "My times dropped 2% in the shoes and another 2% the following year in the same pair…" | analysis | hot_take / reaction | The second 2%, with shoes held constant, is the whole argument against "carbon plates are the whole story". The fact carries it, so rule 1 says analysis. It's about the writer, but rule 3 says evidence outranks personal framing. |
| sp_007 "Ran the same loop in 4C and in 24C… 90 seconds slower in the heat" | analysis | reaction | Personal and recent, but it's a controlled comparison used to rebut a general claim ("heat costs you a bit"). Rule 3: a load-bearing fact beats immediacy. |
| sp_021 "Four minutes off. FOUR. … grinning at nothing." | reaction | analysis | It contains a number, but the number argues nothing; it's what just happened to the writer. Rule 2 says reaction. |
| sp_017 "Road racing peaked in about 2015 and everything since has been marketing." | hot_take | analysis | A date is not evidence. Nothing checkable supports "peaked", so it's a confident, general, unsupported claim. |

**What 100% does and doesn't mean.** The staff set is close to separable once the rules are applied literally: each post has either a load-bearing number, a general claim with no support, or a first-person account of the last few hours. Every "ambiguous" post was ambiguous in a way a decision rule had already named. That means the staff rules are tight. It does not mean my sports taxonomy was applied as consistently. **Disclosure:** the 30 staff labels were drafted by Claude under the staff taxonomy, and I accepted them without changes. So this rate measures how a careful reader applies these written rules, not my own consistency as an annotator. As Milestone 4 evidence, it can't show a labelling problem in [labels.csv](labels.csv). It shows only that a three-rule decision procedure, applied in order, can produce full agreement, and my sports taxonomy uses the same kind of ordered procedure.

## Verdicts and Diagnoses

Targets from [criteria.md](criteria.md), committed before any training. As that file says, a model criterion must hold on **all three** seeds.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.70 | 0.500 | 0.500 | 0.500 | MISSED |
| 2. Every label F1 (min shown) | ≥ 0.60 each | 0.000 | 0.000 | 0.000 | MISSED |
| 3. Dataset: ≥200 distinct posts, ≥25 per label, no label >60% | all three | 200 / 30 min / 49.5% | same | same | MET |
| 4. Precision on `rulebook` (and >0 predictions) | ≥ 0.80 | 0.500 | 0.500 | 0.500 | MISSED |
| 5. Most-confident third accuracy ≥0.80 **and** ≥0.10 above least-confident | both | 0.90 vs 0.10 | 0.90 vs 0.10 | 1.00 vs 0.10 | MET |

**How each was decided.**

1. **MISSED.** 0.500 on every seed, 20 points under target. No generous reading is possible.
2. **MISSED.** `rulebook` F1 is 0.667, but `game_analysis` and `fan_take` are 0.000 on every seed.
3. **MET.** A property of [labels.csv](labels.csv), not of a split, so it is identical across seeds: 200 distinct nonempty posts, `fan_take` is the smallest label with 30, and `rulebook` is the largest at 49.5%.
4. **MISSED.** The model made 30 `rulebook` predictions (so it doesn't trip the zero-prediction clause), but only 15 were right: 0.500, the base rate.
5. **MET, as written.** Both conditions hold on all three seeds. I checked the argument against it: with a model that always says `rulebook`, "confidence" only ranks how rulebook-like a post looks, so the confident third is right because the obviously-about-rules posts really are `rulebook`. That is real signal (the model's confidence does separate rulebook posts from the rest), but it isn't triage across all three labels, which was the intent. I'm keeping MET because the criterion is measurable and the numbers clear it. Its weakness is that it doesn't guard against a degenerate model. That's a gap in the criterion's coverage, not a reason to rewrite it, so criteria.md is unchanged.

**Diagnosis: one cause behind all three misses. The model never trained past the class prior.**

- **What I see:** on all three seeds and splits the model outputs `rulebook` for 30/30 posts (confusion matrix above). Validation accuracy was flat at the majority rate after epochs 1, 2 and 3.
- **How I know it's training and not the task:** the final training loss was about 0.97 and validation loss about 0.88–0.99. The entropy of my label distribution (49.5 / 35.5 / 15) is 1.00. A model that has learned *only* how common each label is scores exactly that. With 139 training posts, batch 16 and 3 epochs, the model got 27 optimizer steps at learning rate 2e-5, which is not enough to move a freshly initialised classification head off the prior. The zero-shot baseline reaches 0.467 accuracy and nonzero `game_analysis` F1 from the definitions alone, so the distinctions are learnable from text. The trained model simply hasn't started.
- **Why I don't think it's my labels (yet):** inconsistent labelling on a boundary shows up as errors running both ways across that pair. Here nothing is predicted as `game_analysis` or `fan_take` at all, which is an optimisation symptom, not a boundary symptom. The agreement check can't confirm this either way. It came out 30/30, and (see the disclosure above) it measures the staff rules more than my own annotation habits. Once the model trains properly, the game_analysis/fan_take boundary is where I'd expect labelling inconsistency to appear, because that is the boundary I flagged as hardest in Unit 5.
- **Contributing, for criterion 2 specifically:** `fan_take` has 21 training and 4 test examples per split. Even a working model will have a jumpy `fan_take` F1, since one test post moves recall by 25 points.

**Improvement this points at:** a training setting. The diagnosis names undertraining, so I'll change one thing, the number of epochs, and leave labels, taxonomy and criteria as they are.

## The Improvement

**What I changed:** `EPOCHS` from 3 to 10 in notebook section 2. Nothing else: same [labels.csv](labels.csv), same taxonomy, same criteria, same seeds (42, 7, 2024), same learning rate, batch size, token limit and device (MPS).

**Why:** the diagnosis above found the model stuck at the class prior. Training loss was about 0.97 against a prior entropy of 1.00, after only 27 optimizer steps. More epochs is the most direct test of "undertrained": 10 epochs gives about 90 steps. I picked 10 once, before running, and didn't try other values, so the test set wasn't used to tune it. Final training loss fell to 0.61 / 0.68 / 0.62.

Raw output: [results_three_seeds_after.json](results_three_seeds_after.json).

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.70 | 0.833 | 0.867 | 0.767 | MET |
| 2. Every label F1 (min shown) | ≥ 0.60 each | 0.000 (`fan_take`) | 0.400 (`fan_take`) | 0.400 (`fan_take`) | MISSED |
| 3. Dataset: ≥200 distinct posts, ≥25 per label, no label >60% | all three | 200 / 30 min / 49.5% | same | same | MET |
| 4. Precision on `rulebook` (and >0 predictions) | ≥ 0.80 | 0.833 | 0.833 | 0.867 | MET |
| 5. Most-confident third accuracy ≥0.80 **and** ≥0.10 above least-confident | both | 1.00 vs 0.80 | 0.90 vs 0.80 | 1.00 vs 0.60 | MET |

Seed 7 meets criterion 5 by exactly the margin: 9/10 against 8/10, one post. One more confident mistake and it fails. I'm calling it MET because the target says "at least 0.10", but it's the narrowest pass in the table.

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.833 | 0.867 | 0.767 | 0.100 |
| Macro F1 | 0.593 | 0.739 | 0.662 | 0.147 |
| F1 — `rulebook` | 0.909 | 0.909 | 0.867 | 0.042 |
| F1 — `game_analysis` | 0.870 | 0.909 | 0.720 | 0.189 |
| F1 — `fan_take` | 0.000 | 0.400 | 0.400 | 0.400 |

### Before and after, side by side

| Criterion | Before (seeds 42 / 7 / 2024) | Verdict | After (seeds 42 / 7 / 2024) | Verdict |
|---|---|---|---|---|
| 1. Accuracy ≥ 0.70 | 0.500 / 0.500 / 0.500 | MISSED | 0.833 / 0.867 / 0.767 | MET |
| 2. Every label F1 ≥ 0.60 | 0.000 / 0.000 / 0.000 | MISSED | 0.000 / 0.400 / 0.400 | MISSED |
| 3. Dataset balance | met | MET | met | MET |
| 4. `rulebook` precision ≥ 0.80 | 0.500 / 0.500 / 0.500 | MISSED | 0.833 / 0.833 / 0.867 | MET |
| 5. Confidence separation | 0.90–0.10 / 0.90–0.10 / 1.00–0.10 | MET | 1.00–0.80 / 0.90–0.80 / 1.00–0.60 | MET |

### Confusion matrices — After

| Seed 42 | rulebook | game_analysis | fan_take |
|---|---|---|---|
| **rulebook** | 15 | 0 | 0 |
| **game_analysis** | 1 | 10 | 0 |
| **fan_take** | 2 | 2 | 0 |

| Seed 7 | rulebook | game_analysis | fan_take |
|---|---|---|---|
| **rulebook** | 15 | 0 | 0 |
| **game_analysis** | 1 | 10 | 0 |
| **fan_take** | 2 | 1 | 1 |

| Seed 2024 | rulebook | game_analysis | fan_take |
|---|---|---|---|
| **rulebook** | 13 | 2 | 0 |
| **game_analysis** | 2 | 9 | 0 |
| **fan_take** | 0 | 3 | 1 |

(Rows are true labels, columns are predictions.)

**Did it help? Yes.** One change moved two criteria from MISSED to MET, and the trained model now clearly beats the zero-shot baseline. On the seed-42 split, the same 30 posts in [test_split.csv](test_split.csv), it scores 0.833 accuracy against 0.467 and 0.593 macro F1 against 0.300. That confirms the diagnosis: the before-model was undertrained, not unable to learn the task.

**What it didn't fix:** `fan_take`. Across the three seeds the model predicted `fan_take` only 0, 1 and 1 times. When it does, it's right (precision 1.00), but it finds at most 1 of the 4 real ones. The real `fan_take` posts leak in both directions, 4 to `rulebook` and 6 to `game_analysis` summed over the seeds. Accuracy also now swings exactly 10 points across seeds (0.767–0.867), right at the notebook's instability line, driven by `game_analysis` (F1 spread 0.19) and `fan_take` (0.40).

## What's Still Broken

**Criterion 2 (every label F1 ≥ 0.60) is still missed, because of `fan_take`** (F1 0.000 / 0.400 / 0.400).

- **What I'd do next:** add examples to the thinnest label, about 30 more `fan_take` answers labelled under the same decision rule. That's the second improvement the course lists, and the evidence points at it. `fan_take` has 21 training examples per split against 69 `rulebook`, and the 10-epoch model almost never predicts it, which is what a model does with a label it has seen too little of to risk guessing. Once that's done, I'd re-check the `game_analysis`/`fan_take` boundary: 6 of the 10 `fan_take` misses went to `game_analysis`, and that's the boundary I named as hardest in Unit 5. If more data doesn't fix it, my own labels on that boundary are the next suspect. Advice that cites a mechanism (a cricket-bat sizing tip, a training routine) is exactly the kind of answer I may have labelled both ways.
- **Why I stopped:** the unit allows exactly one change, and I used it on epochs because the diagnosis pointed at training first. Changing the data as well would have mixed two effects into one before/after comparison.
- **Measurement problem I can't fix by training:** each test split has only 4 `fan_take` posts, so its F1 can take only a handful of values and one post moves recall by 25 points. Even a model that really reached 0.60 could miss on a given seed. A larger `fan_take` pool would fix the measurement as well as the model.

**Criterion 5 passes, but narrowly** (seed 7 by exactly one post), and as written it can't tell a degenerate model from a useful one (it was MET before the fix too). I'd keep it and add a companion, for example "and the model predicts every label at least once", in a future unit. I'm not revising it here, because it was measurable and wasn't missed.

**The gap between what I meant and what the model learned.** I meant `fan_take` to capture the writer's *purpose* (recommending, judging, predicting), but the after-run matrices show the model learned something closer to *surface register*. Posts that sound technical go to `game_analysis` and posts that mention rules go to `rulebook`, even when their main conclusion is advice. The model sorts `rulebook` and `game_analysis` almost perfectly by vocabulary. The purpose-based distinction that defines `fan_take` is the part it didn't learn, which is unsurprising, since that distinction lives in the conclusion and not in the words, and my 128-token limit can cut the conclusion off.

## How I Used AI

- **Unit 6 execution:** Claude (in VS Code) ran `baseline.py` (with definitions, and with bare label names), ran notebook sections 6–7 headless from the notebook's own cell code, made the single `EPOCHS` edit and `RUN_LABEL` change, and drafted these README sections from the JSON outputs. I reviewed the numbers against the committed JSON files.
- **Staff labels:** Claude drafted all 30 labels in [my_staff_labels.csv](my_staff_labels.csv) under the staff taxonomy, and I accepted them unchanged. They were committed before the staff labels were opened. This is disclosed in the Agreement Report because it limits what the 100% rate says about my own annotation consistency.
- **Spotting error patterns:** Claude pointed out that the before-model's final training loss (about 0.97) sat on the entropy of my label distribution (1.00). That turned "the model is bad" into the specific diagnosis "the model only learned the class prior", which chose the improvement. It also flagged that the before-run's zero seed spread was a constant predictor, not stability, and that criterion 5 passes even for a degenerate model.
- **Decisions that stayed mine:** the labels, taxonomy and criteria from Unit 5 are unchanged. The verdicts follow the "must hold on all three seeds" rule committed in [criteria.md](criteria.md) before training.
