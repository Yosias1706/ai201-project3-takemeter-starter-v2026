# Acceptance criteria — three-way Sports TakeMeter

These targets supersede the earlier citation-classifier targets. They are committed before the first training run using rulebook, game_analysis and fan_take. Earlier two-class scores are not results for this task. In Unit 6, each model criterion must hold for all three prescribed seeds (42, 7 and 2024), not only the best one.

1. **Overall held-out accuracy must be at least 0.70.**
   Three equally likely guesses achieve about 0.33. Seven correct routing decisions in ten would make the classifier useful for separating officiating debates, sports explanations and personal takes, despite overlap between the latter two.

2. **Held-out F1 must be at least 0.60 for each of the three labels.**
   The smaller fan_take class should not disappear behind strong rulebook performance. A 0.60 floor allows some boundary mistakes but requires both retrieval and precision for every category.

3. **The unsplit dataset must have at least 200 distinct, nonempty posts, at least 25 examples per label, and no label above 60%.**
   Rule discussions are common in this community. A stricter majority cap than the course's 70% keeps them from swallowing the task, while the per-class floor guarantees some personal takes remain. Twenty-five still leaves only about four test examples, so report small-class uncertainty explicitly.

4. **Held-out precision for rulebook must be at least 0.80; zero rulebook predictions fails.**
   Readers searching for how a rule applies should not mostly receive commentary about whether that rule is fair. Four correct rulebook assignments out of five is a defensible bar for that use.

5. **The most-confident held-out third must have accuracy at least 0.80 and exceed the least-confident third by at least 0.10.**
   Confidence should help triage the analysis/take boundary. Use the notebook's maximum-softmax ranking and floor(n_test/3) examples at each end; with 30 test rows, each third has 10 and a ten-point difference is one additional correct answer.

These cover accuracy, per-label performance, balance and confidence. The targets will not be revised to fit the results.

## Pre-training stress review

| Criterion | Why it might be too easy | Why it might be too hard |
|---|---|---|
| 1 | Rulebook vocabulary is often distinctive. | Tactical explanation and recommendation share sports language. |
| 2 | The main-purpose rule resolves mixed posts. | The smaller fan_take test sample makes one mistake costly. |
| 3 | The community includes factual answers and personal advice. | Its question-and-answer format naturally favors rules and factual explanations. |
| 4 | Explicit legal outcomes are recognizable. | A complaint about referees can resemble a rule interpretation. |
| 5 | Clear rules may produce strong confidence signals. | A small held-out set can reverse the apparent confidence advantage. |
