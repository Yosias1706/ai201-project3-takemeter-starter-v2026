# Acceptance criteria — Sports TakeMeter

Recorded before training on the Sports Stack Exchange dataset. An earlier starter-practice run existed before this project; its scores were not used to set these targets. These targets apply to the sports dataset and its held-out evaluation, not to the unrelated staff taxonomy. Unit 6 will evaluate model criteria for each of seeds 42, 7 and 2024; a model criterion is met only if it holds for all three seeds.

1. **Overall accuracy: at least 0.75 on the held-out test set.**
   With two categories, 0.50 is the uniform-guessing baseline. Three correct answers out of four would make sorting sports explanations useful while leaving room for genuinely ambiguous attribution and late citations truncated by the model.

2. **Per-label F1: at least 0.65 for both sourced and uncited on the held-out test set.**
   Both finding citations and identifying their absence matter. This prevents a good overall score from hiding a model that mostly predicts the larger class; 0.65 allows mistakes among implicit rule references and concrete but unsupported statistics.

3. **Dataset balance: each label must occupy between 30% and 70%, inclusive, of at least 200 distinct nonempty answers.**
   A minimum of 60 examples per label gives the default split about nine test examples per category. This is still small, but makes class-level evaluation possible and enforces the course's majority cap.

4. **Sourced precision: at least 0.80 on the held-out test set; predicting no sourced answers fails.**
   A false sourced label incorrectly implies that supporting material is present. At least four in five of those predictions should be correct for a reader using the classifier to find attributed explanations.

5. **Confidence: accuracy in the most-confident test third must be at least 0.80 and at least 0.10 greater than accuracy in the least-confident third.**
   Confidence should help decide which predictions deserve checking first. The notebook ranks maximum softmax probability and uses floor(n_test/3) examples at each end; for 30 test examples this compares 10 against 10, so a ten-point difference is one additional correct prediction.

These cover overall accuracy, per-label performance, balance, and confidence. Targets are frozen rather than adjusted to the observed scores.

## Pre-training target review

| Criterion | Why it could be too easy | Why it could be too hard |
|---|---|---|
| 1 | Citation language is often explicit. | Long answers may place their evidence beyond 128 tokens. |
| 2 | Two labels avoid a sparse reaction category. | A rule reference can be very short or implicit. |
| 3 | This community regularly mixes cited and uncited answers. | Recent activity could be dominated by heavily sourced rule explanations. |
| 4 | Named documents and quotations give strong cues. | Detailed unsupported claims can sound authoritative. |
| 5 | Obvious links may produce easy, confident predictions. | With only ten examples per third, one error changes accuracy by ten points. |
