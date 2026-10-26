# Sports Stack Exchange source snapshots

Collected 2026-10-26 UTC through the public Stack Exchange API:

- https://api.stackexchange.com/2.3/answers?site=sports&pagesize=100&page=1&order=desc&sort=creation&filter=withbody
- https://api.stackexchange.com/2.3/answers?site=sports&pagesize=100&page=2&order=desc&sort=creation&filter=withbody

The snapshots contain the 200 returned answer objects, including complete HTML, author, creation time, question ID, and content license. No answers were removed, shortened, or fabricated. This is a convenience sample ordered by creation time, not a representative random sample of all sports discussion. Later edits may appear in old answers.

[../sources.csv](../sources.csv) supplies row-level attribution and permanent post links. Original contributions retain their authors' CC BY-SA licenses (recorded per row). HTML-to-text formatting is an adaptation: complete prose, quotations, tables, link destinations, image descriptions/URLs and embedded video URLs are retained. Image pixels and video contents are not model inputs. Attribution metadata is not included in training text. Dataset adaptations are shared under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/.

[annotations.json](annotations.json) records the selected label and rationale for each answer. The current three-way annotation uses the main purpose of each complete answer: rulebook, game_analysis or fan_take. Every answer was reclassified under the new definitions, independently of its earlier citation label. The decision order and ambiguous cases are documented in the project notes.

The committed CSV is the canonical unsplit input. Local rebuilding helpers are optional and excluded from version control. The source snapshots and annotation records preserve the full inputs for independent reconstruction. The notebook alone performs the train/validation/test split.
