# Independent C818 courseware QA

Scope: requested C818 repository only. Read-only audit; no course files changed. Reviewed current PPTX/PDF, LP/LG DOCX/PDF and LG Markdown; eight separate lab folders, prompts, recovery packs and assets. Rendered slide contact sheet and reference-theme evidence, LP/LG selected pages, all 24 lab PDF pages, and all flyer variants were inspected.

## Findings

No remaining blocking defects after current-file recheck.

- **Low / wording resolved:** the reused flyer workflow now names the catalogue as its single offer-fact source.
- **Low / operational:** `SOURCE-NOTES.md` acknowledges official page09:30–17:30 versus LP09:30–18:30. Course package arithmetic is internally correct for15 instructional hours. Confirm trainer scheduling outside this artifact audit.

## Defects found and resolved during audit

- LG TOC initially one page behind actual headings; rebuilt current LG has 78 matching TOC entries, LP has 15 matching entries. Cleared.
- Lab 4 square proof initially overlapped campus and CTA; corrected PDF visually inspected and clear. Cleared.
- Lab 4 story proof initially placed academy identity outside its required top 10% safe band. Corrected essential text now within y90.7–816.4 points of 907.1-point page; visually inspected. Cleared.

- Reused flyer/social skill source paths now correctly resolve to `cnbacademy/data/courses.json`; absent term-highlights dependency removed. Cleared.
- Added Lab4 `design-review.csv` and Lab6 `content-review.csv` recovery files. Cleared.
- Updated A5/square/story text proofs match all actual visible shape text, including motif and draft footer. Cleared.

## Verified checks

- 76 deck slides, 48 concept slides: 12 concepts per topic before its related lab overviews. PPT has no terminal/menu lab procedures, and lab slides identify outcome, artifact and evidence only.
- Theme matches reference cream, charcoal, terracotta and teal design; PPT runs use Cambria headings and Calibri body. Editable shapes/cards/tables plus authentic academy capture support visual teaching.
- Topic-to-lab mapping consistent: Topic1 Labs1–2; Topic2 Labs3–4; Topic3 Labs5–6; Topic4 Labs7–8. Titles, numbering, C818 identity, v1.0 and outputs align across data, deck, LG, LP and folders.
- Both LP days total exactly480 minutes excluding lunch;30 tea minutes and450 instructional minutes each. Total900 instructional minutes /15 hours. Lab durations45,50,75,55,70,60,85,50 minutes agree across artifacts.
- Current deck PDF76 pages, LP PDF9 pages, LG PDF46 pages; eight lab PDFs3 pages each. No blank document pages or text outside page bounds detected; inspected pages and all lab contact-sheet pages readable without clipping.
- All eight labs contain Goal, Build, Prerequisites, numbered executable Steps, Test it, Troubleshooting, Challenge, Reflection and Checkpoint/rejoin. Connected campaign spine retains BAK-101 throughout; other campaign extension explicitly isolated.
- Website catalogue20 synthetic records /10 Bakery10 Cooking; BAK-101 four weeks,S$680,Saturday9:30–12:30,Orchard Road agree across source and sample proofs. No cafe/barista course invented. Source unknowns and classroom-draft status maintained.
- Eligible contact checkpoint C001,C004,C006 meets consent/bakery/non-suppressed rule. Metrics definitions and sample values use explicit denominators. Sample article615 words meets500–700 brief.
- No Claude Cowork procedures or unrelated course identifiers found in learner artifacts. Explicit reference-history mention is explanatory, not a learner setup dependency.
- Automated prohibited scan passed:34 actual artifacts,zero prohibited-content hits.

Disposition: **PASS**. No blocking artifact defects remain. Publication and external system verification are outside this read-only review.


## Additional runtime checks

- Catalogue preview: 20 rendered cards; BAK-101 source-only lookup returns the exact record; no JavaScript errors.
- Mobile site and email preview: scroll width equals client width at 375 px.
- Sample social article: 615 words; synthetic eligible segment C001, C004, C006.
- Current LP/LG static TOCs remapped from final PDFs; second verification required zero corrections.
- Publication verification is recorded separately in RELEASE-REPORT.md.

- Final calendar recovery sample reviewed again: workspace-root asset/dependency paths and field-level sources match the lab instructions and sample claims. Independent reviewer confirmed PASS.
