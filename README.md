# TakeMeter — Sports answers and visible evidence

## What This Does

This project classifies complete answers from [Sports Stack Exchange](https://sports.stackexchange.com/) into **sourced** and **uncited**. It distinguishes visible attribution from explanations or opinions that supply no identifiable supporting source. It does not decide whether an answer is true, whether the cited source is reliable, or whether a post is good overall. The community covers many sports, including football, cricket, baseball, basketball and tennis.

[Community reading notes](notes/community.md) record the initial 35-answer sample and candidate distinctions. [Acceptance criteria](criteria.md) were committed before training on this dataset. The repository for both units is [Yosias1706/ai201-project3-takemeter-starter-v2026](https://github.com/Yosias1706/ai201-project3-takemeter-starter-v2026).

## Label Taxonomy

### sourced

**Definition:** Supports at least one substantive sports claim with an identifiable external source: a relevant link, named publication or dataset, attributed quotation, or specific rule reference.

**Example 1 — Olympic sailing results**

> William Eastman Buchan (Star class) and William Carl Buchan (Flying Dutchman class) both won gold medals in separate sailing events in the 1984 Olympics (https://en.wikipedia.org/wiki/Sailing_at_the_1984_Summer_Olympics#Medal_summary).

— [user37911](https://sports.stackexchange.com/users/37911/user37911), [answer 30382](https://sports.stackexchange.com/a/30382), CC BY-SA 4.0.

**Example 2 — baseball forfeiture**

> The defending team, by refusing to tag the runner, would probably forfeit the game to the batting team under Rule 7.03(a)(2):
> 
> A game may be forfeited to the opposing team when a team ... [e]mploys tactics palpably designed to delay or shorten the game.
> 
> Here, the game is delayed by not taking the obvious step of tagging the runner out.
> 
> I don't know if there is any provision for both teams forfeiting, but I think it would be a judgment call by the umpire to determine which team is most guilty of delay. It is much easier for the defense to put out a runner that refuses to take their base than for a runner to perpetually avoid being tagged by an active defense.

— [chepner](https://sports.stackexchange.com/users/11180/chepner), [answer 30380](https://sports.stackexchange.com/a/30380), CC BY-SA 4.0.

### uncited

**Definition:** Offers sports claims, explanations, opinions or advice without an identifiable external source supporting a substantive claim.

**Example 1 — choosing a cricket bat**

> The best is to stand it up next to you, the top of the handle should be around your hip/waist. Or hang it down straight by your side and keep your arm relaxed. The toe should just about touch the ground. But height is secondary, weight matters more imo - grab a few and take some shadow shots, go with whatever feels balanced and not too toe-heavy. Kids are usually fit by bat number (0-6) and adults are fit SH or LH based on height.

— [Abhi raj](https://sports.stackexchange.com/users/37581/abhi-raj), [answer 30361](https://sports.stackexchange.com/a/30361), CC BY-SA 4.0.

**Example 2 — bowling speed**

> He did actually hit the 160 kmph mark vs New Zealand in an ODI in 2002 at Pakistan.

— [Guest](https://sports.stackexchange.com/users/37579/guest), [answer 30354](https://sports.stackexchange.com/a/30354), CC BY-SA 4.0.

### The hardest boundary

The hardest boundary is a concrete fact versus an attributed fact. A speed, date, score or athlete's name is not by itself a source. The bowling-speed example remains **uncited**, while the forfeiture example is **sourced** because it quotes Rule 7.03(a)(2), even without a URL.

Apply the rule to the whole answer: one substantive supported claim suffices even when another paragraph speculates. A named document with attributed content or a specific rule provision counts. Generic references to “the rules,” personal experience, unidentified coaches, quotations of the question alone, promotional links and unattributed illustrations do not. An identified documentary or linked report can count. Labels describe attribution, not correctness. [Taxonomy notes](notes/taxonomy.md) contain eight synthetic boundary tests, excluded from the dataset, and the competing interpretations of the bowling-speed example.

## The Dataset

**Source:** 200 public answers returned by the Sports Stack Exchange API in descending creation order, two pages of 100, collected on October 26, 2026 UTC. No login was required. These are whole answers, not excerpts, question titles, or generated posts. This is a convenience sample, not a representative sample of all sports fans or all sports posts.

**Preparation:** Collected first, assigned the two labels, then checked the full answer and its original HTML against the decision rule. The review corrected cases where a link was hidden behind ordinary words and cases where detailed statistics had no source. Each row's note contains its answer ID and a decision rationale. No row is marked as an unaided `cold` annotation. The dataset is kept as one unsplit [labels.csv](labels.csv); the notebook alone creates the splits.

| Label | Count | Share |
|---|---:|---:|
| sourced | 125 | 62.5% |
| uncited | 75 | 37.5% |
| **Total** | **200** | **100%** |

There are zero empty texts and zero exact duplicate texts. The larger label remains below the 70% limit. Original HTML, author attribution, timestamps and content licenses are retained in [source snapshots](data/source/); [sources.csv](data/sources.csv) maps every row to its public answer. HTML was converted to text without trimming prose: links, tables, quotations, image descriptions and embedded-media URLs remain. Image pixels and video frames are not model inputs. Text and dataset adaptations retain CC BY-SA attribution; see [source documentation](data/source/README.md).

**Three hard cases**

1. [Answer 30354](https://sports.stackexchange.com/a/30354) gives a specific 160 kmph claim, opponent and year. It could look sourced because it is checkable, but the chosen label is **uncited** because it identifies no report or record.
2. [Answer 30380](https://sports.stackexchange.com/a/30380) has no hyperlink and hedges its conclusion. The chosen label is **sourced** because the numbered, quoted baseball rule is identifiable support.
3. [Answer 30245](https://sports.stackexchange.com/a/30245) cites jump types in its first paragraph and speculates about physics later. The chosen label is **sourced** because at least one substantive claim is supported; the label does not certify all sentences.

**Limitations:** Some answers share a question and may repeat rules or events. Exact deduplication does not remove this topical dependence; the supplied row-level split is not a question-group holdout. Long posts remain complete in the CSV, but the model reads only their first 128 tokens, so late citations may be invisible. A URL detector would be a useful additional diagnostic, although numbered rules without links and irrelevant links mean it would not exactly implement this taxonomy.

## The Training Run

**Starting model:** `distilbert-base-uncased`, with a new two-class classification head.

| Setting | Value |
|---|---|
| Epochs | 3 |
| Learning rate | 0.00002 |
| Batch size | 16 |
| Maximum tokens | 128 |
| Seed | 42 |
| Hardware | Apple Silicon GPU, MPS |
| Python | 3.13.0 |
| PyTorch | 2.14.1 |

No training hyperparameters were changed from the starter defaults. The label map and input path were changed to this project's two labels and `labels.csv`. The earlier notebook execution used the starter's fictional practice dataset; the committed results here come from the real sports dataset.

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| sourced | 87 | 19 | 19 |
| uncited | 52 | 12 | 11 |
| **Total** | **139** | **31** | **30** |

The supplied 70/15/15 splitting code produces 139/31/30 because of rounding in the second split. Neither class has fewer than eight test examples. The environment check passed all ten checks, and notebook sections 1–5 completed successfully. [results.json](results.json) stores metrics, confidence summaries and device information; [test_split.csv](test_split.csv) stores the exact held-out rows for Unit 6. Both were committed after the dataset and criteria. The training run did not save a standalone model checkpoint; rerun the notebook to recreate the trained model in memory.

The run is recorded as obtained, without selecting a better seed or changing targets after seeing scores. Assessment against the criteria, three-seed comparison and baseline experiments belong to Unit 6; notebook sections 6–7 have not been run. Hardware can affect reproducibility even with the same seed.

## Reproducing the Project

Follow [RUNNING.md](RUNNING.md) to install the pinned requirements in `.venv`, run `python test.py`, select that environment as the notebook kernel, then run sections 1–5 of [takemeter.ipynb](takemeter.ipynb) in order. The committed CSV and notebook are sufficient; local collection/execution helpers are not required. The source snapshots and per-answer annotation records preserve the provenance needed to audit the data.

The five numerical targets are fixed in [criteria.md](criteria.md). No stretch features are claimed. Unit 6 work remains pending.
