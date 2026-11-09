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

The environment check passed all ten checks. The notebook's data check accepted this dataset and warned about the small fan_take test set during splitting. Notebook sections 6–7 remain unexecuted. Baseline comparison, three-seed evaluation and criterion verdicts belong to Unit 6.

## Reproducing the Project

Follow [RUNNING.md](RUNNING.md), install the requirements in `.venv`, run `python test.py`, select that kernel, and execute sections 1–5 of [takemeter.ipynb](takemeter.ipynb). The committed CSV and notebook are sufficient to run training.

The new milestone commits document the reading, definitions, criteria, relabeling, training and final write-up in that order. No stretch features are claimed, and Unit 6 is still pending.

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
