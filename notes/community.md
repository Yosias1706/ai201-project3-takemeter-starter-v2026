# Milestone 1 — A three-way sports conversation classifier

Community: [Sports Stack Exchange](https://sports.stackexchange.com/), a public multi-sport discussion community. The unit of text is a complete answer, not a question title.

This restarts the project with a new objective: distinguish **officiating and rules**, **sports facts and explanations**, and **personal takes and recommendations**. The old citation-presence experiment is superseded; its commits remain in history, and its scores are not evidence about this classifier.

The initial reading sample is the first 35 answers in the frozen public API collection (30391 through 30290). Re-reading that sample for conversational purpose shows:

1. Officiating decisions explain what counts as legal: 30391 on forward passes, 30380 on forfeiture, 30344 on when a cricket match ends.
2. Sports explanations reconstruct what happened or why: 30382 on Olympic medalists, 30331 on speed comparisons, 30328 on penalty conversion rates.
3. Personal recommendations and conjecture make a different kind of contribution: 30361 recommends how to choose a cricket bat; 30360 offers solo practice drills; 30326 speculates about a ranking-list error.

A broader scan reveals more personal takes: 30214 attributes a player's shooting decline to reduced possession; 30088 predicts singles players will dominate doubles specialists; 29949 assesses someone's chances of a basketball career; 29938 jokes about duct tape for hockey sticks.

The original sample has useful real variation for these three categories. Retain the 200 complete answer bodies and their attribution, but re-annotate every answer from scratch under the new definitions. Citation presence, popularity and answer acceptance are not label rules. Reddit direct access and an alternate public archive were unavailable, so the public Sports Stack Exchange collection remains the usable sports source.
