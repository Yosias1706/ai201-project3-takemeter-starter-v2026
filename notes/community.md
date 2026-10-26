# Milestone 1 — Sports Stack Exchange

Community: https://sports.stackexchange.com/ — public questions and answers about sports rules, history, tactics and equipment. The dataset uses **answers**, which contain claims and explanations, rather than mixing questions with answers. Reddit denied automated access; Sports Stack Exchange's public API returned complete posts without login.

Read the first 35 answers returned in descending creation order on 2026-10-26 UTC (2026-10-25 Chicago), answer IDs 30391 through 30290. This records the actual reading sample; no claim of a timed 20-minute human reading session is made.

Candidate distinctions grounded in that sample:

1. Explicit source support versus unsupported explanation: answer 30380 cites baseball Rule 7.03(a)(2); 30390 explains free-kick reasoning without an identifiable citation.
2. Concrete evidence versus generic advice: answer 30328 gives penalty conversion counts and a BBC source; 30361 gives bat-fitting advice from experience.
3. Qualified inference versus categorical claims: answer 30363 distinguishes documented medal history from speculation; 30350 states a wicketkeeper rule without identifying its source.
4. Rules interpretation versus historical examples: answer 30344 applies MCC Law 16.6.1; 30382 identifies Olympic sailing medalists.

Selection: distinguish source-supported from uncited claims. The community has few pure emotional reactions, so imposing analysis/hot_take/reaction would create a tiny reaction class. Two labels fit the observed material better. The classifier measures visible support, not truth or overall quality.

The API supplies author attribution, permanent answer IDs and content licenses; preserve these beside the dataset. Keep whole answer bodies and links, with HTML converted to readable text. Do not use votes or accepted-answer status as input features.
