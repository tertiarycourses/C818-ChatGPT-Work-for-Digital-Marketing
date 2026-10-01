# Lab 08 — Measure and hand off the campaign

**C818 · Topic 4 · 50 minutes · Version 1.0**

## Goal

Interpret synthetic results and package a source-checked, reviewable campaign handoff.

## What you’ll build

campaign/metrics.csv, campaign/recommendation.md, campaign/manifest.csv and campaign/handoff.md.

## Prerequisites

Labs 1–7 current assets. Synthetic assets/campaign-results.csv is supplied; no live campaign analytics or real business results are required.

## Steps

### 1. Load the synthetic results

Copy assets/campaign-results.csv into campaign/campaign-results.csv. Read the definitions in assets/metric-definitions.md. Counts are invented teaching data and are not academy performance.

### 2. Calculate clearly defined rates

Ask Work or a spreadsheet to calculate delivery_rate = delivered/sent, click_rate = unique_clicks/delivered and click_to_booking = bookings/unique_clicks. Save campaign/metrics.csv with numerator, denominator and rate. If a denominator is zero, use UNKNOWN rather than dividing by zero.

### 3. Verify the arithmetic

Variant A has 1000 sent, 980 delivered, 49 unique clicks and 7 bookings. Confirm 98.0 percent delivery, 5.0 percent click rate and 14.3 percent click-to-booking conversion. Variant B has 1000 sent, 975 delivered, 58 unique clicks and 8 bookings; confirm 97.5 percent, about 5.95 percent and about 13.79 percent.

### 4. Request a bounded recommendation

Attach metrics.csv and the campaign brief to Work and paste prompts/task.txt. Separate observation, limitation and proposed next test. A higher rate in this sample does not establish a reliable lift.

### 5. Inventory current files

Copy assets/manifest-template.csv to campaign/manifest.csv. Add the current flyer sources and proofs, article, platform packages, calendar, sequence, segment and metrics. Record path, purpose, version, source, status and unresolved issue for each.

### 6. Cross-check the campaign

Open one flyer proof, article and email beside selected-course.json. Check BAK-101, four weeks, S$680 and the same academy identity. Check calendar and email status remain draft. Record specific evidence in handoff.md.

### 7. Resolve or assign holds

List missing production sender, public booking link, unsubscribe configuration and launch target as UNKNOWN with an owner and next action. Do not label the campaign production-ready while these holds remain.

### 8. Package and explain

Save the four deliverables and explain your recommendation to a partner using the metrics and manifest. Keep the package as a classroom draft. If previous labs stalled, use their checkpoint files, record sample provenance and continue the handoff without claiming you generated them.

## Task prompt

Copy `prompts/task.txt` into the Work task. Review the plan before authorising production.

```text

Analyze campaign-results.csv as synthetic teaching data. Calculate delivery rate, unique click rate and click-to-booking conversion with explicit numerators and denominators. Return metrics.csv and recommendation.md with observations, limitations and one proposed controlled next test. Do not claim statistically reliable uplift, revenue or real academy results. Build manifest.csv and handoff.md for the current campaign files, recording versions, source facts, review evidence and unresolved production holds. Keep sender, real booking link, unsubscribe configuration and launch target UNKNOWN unless supplied. Confirm that no campaign message was sent or scheduled.

```

## Test it

- A rates are 98.0%, 5.0% and approximately 14.3%; B rates are 97.5%, approximately 5.95% and 13.79%.

- The recommendation distinguishes synthetic observation from a proposed test.

- Every manifest path points to a current file or is explicitly unresolved.

- The handoff records facts checked, remaining UNKNOWNs and draft/not-sent status.

## Troubleshooting

**The click rate uses sent as denominator:** Use delivered for this exercise’s unique click rate and show the denominator column.

**Work claims a reliable winner:** Ask for the sample limitation and a proposed next test; remove unsupported causal or statistical claims.

**The manifest lists missing files:** Correct the paths or label unresolved; use the supplied checkpoint only with its provenance recorded.

## Challenge

Add a zero-delivery row and prove the rate is UNKNOWN; propose what operational investigation would be needed before interpreting it.

## Reflection

What evidence would be needed before using this recommendation for a real launch?

## Checkpoint and rejoin

The `checkpoints/` folder contains supplied classroom sample files. Copy only the files needed into your working campaign, identify them as samples and verify them against the sources before continuing. The sample is a recovery route, not a substitute for reviewing your own work.

**C818 · Tertiary Infotech Academy Pte Ltd · Classroom drafts only.**
