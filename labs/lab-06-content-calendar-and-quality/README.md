# Lab 06 — Build a content calendar and editorial gate

**C818 · Topic 3 · 60 minutes · Version 1.0**

## Goal

Create a five-post calendar with sources, dependencies and review status.

## What you’ll build

content/calendar.csv, content/posts.md and content/content-review.csv.

## Prerequisites

Lab 5 article and caption packages. The supplied calendar template provides a recovery route.

## Steps

### 1. Load the calendar template

Copy assets/calendar-template.csv to content/calendar.csv. Use Day 1, Day 3, Day 5, Day 7 and Day 9 rather than real publication dates. The plan is hypothetical and unscheduled.

### 2. Select five angles

Choose three teaching angles, one practical question and one direct course invitation. Label the last one hard_sell = yes and the other four no. Keep the same BAK-101 campaign spine.

### 3. Request the calendar

Attach the article, platform packages and workflow to Work, then paste prompts/task.txt. Require asset names, source fields, audience, CTA, owner, dependency and status for every row.

### 4. Draft the five post packages

Ask Work to produce posts.md with the five rows expanded into full hook, caption, five hashtags, alt text and claim sources. Each caption stays under 120 words with one CTA.

### 5. Review the dependencies

Link each post to its article or flyer asset. Use owner = classroom marketer and status = draft for every item. If an image is missing, mark its dependency unresolved rather than claiming it is ready.

### 6. Check the promotional balance

Count hard_sell = yes rows; the expected count is one out of five. This is the academy’s reused brand rule. Check that the other four provide useful context and do not merely hide sales language.

### 7. Run the editorial gate

Fill content-review.csv from assets/content-review-template.csv. Check audience relevance, source fidelity, CTA count, hashtag count, alt text and draft status for all five posts. Record at least one substantive revision.

### 8. Save the checkpoint

Keep calendar.csv, posts.md and content-review.csv together. No post is scheduled or published. Use checkpoints/calendar.csv if planning stalled, then add your own reviewed assets and issue notes.

## Task prompt

Copy `prompts/task.txt` into the Work task. Review the plan before authorising production.

```text

Using the reviewed BAK-101 article and platform packages, create a hypothetical five-post content plan on Day 1, Day 3, Day 5, Day 7 and Day 9. Use three teaching posts, one practical question and one direct invitation, with at most one hard-sell post. Return calendar.csv with day,platform,pillar,audience,asset,source,cta,owner,dependency,status,hard_sell. Return posts.md containing five complete short-form packages using the same classroom caption rules. Use only verified catalogue facts. Label missing visual descriptions proposed alt text and keep all rows draft. Do not schedule or publish.

```

## Test it

- calendar.csv has five rows and one hard_sell = yes row.

- Every row has a source, asset, owner, dependency and draft status.

- Each post package has one CTA and five hashtags.

- The review log contains specific evidence and at least one substantive revision.

## Troubleshooting

**All five posts sell the course:** Rewrite four as useful teaching or preparation angles; retain only one direct invitation.

**Calendar paths do not exist:** Use the exact saved asset name or mark the dependency unresolved.

**Work schedules real dates:** Replace dates with relative Day labels and stop connected scheduling actions.

## Challenge

Add a sixth response post that answers a reader question while preserving the one-in-five promotional rule for the first five posts.

## Reflection

How does the calendar help another marketer continue the campaign?

## Checkpoint and rejoin

The `checkpoints/` folder contains supplied classroom sample files. Copy only the files needed into your working campaign, identify them as samples and verify them against the sources before continuing. The sample is a recovery route, not a substitute for reviewing your own work.

**C818 · Tertiary Infotech Academy Pte Ltd · Classroom drafts only.**
