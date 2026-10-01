# Lab 01 — Create a grounded campaign brief

**C818 · Topic 1 · 45 minutes · Version 1.0**

## Goal

Produce a source-checked campaign brief for one bakery course.

## What you’ll build

campaign/brief.md, campaign/selected-course.json, campaign/claim-ledger.csv and campaign/unknowns.md. These define the facts used by every later asset.

## Prerequisites

A ChatGPT account with Work available, a browser and a text editor. Python 3 is needed only for the local website preview. Use the upload route if local folder access is unavailable.

## Steps

### 1. Prepare your working copy

Create a folder named C818-marketing on your computer. Copy assets/cnbacademy from this lab into it. Create a campaign folder beside cnbacademy. Do not work in the original reference folder.

### 2. Start the website

In a terminal opened inside C818-marketing/cnbacademy, run python3 -m http.server 8080. Keep it running and open http://localhost:8080 in a browser. Search the course catalogue for sourdough. Confirm BAK-101 is visible. If Python is unavailable, read data/courses.json directly and use the included site screenshot in the guide.

### 3. Inspect the sources

Open cnbacademy/brand.md, cnbacademy/market-brief.md and cnbacademy/data/courses.json. Locate BAK-101. Record the title, fee, weeks, when, campus, intakes, allergens and learning outcomes. These are fictional scenario facts, not real offers.

### 4. Choose the access route

On ChatGPT web, create a project named C818 Marketing and add the brand, market brief and catalogue through Sources. On desktop, open Projects, create or edit a local project and attach C818-marketing using Add folder. In a new task select ChatGPT and switch to Work. If Work is unavailable, continue with the supplied checkpoint files and record the feature limitation.

### 5. Set durable guidance

Add the text in assets/project-instructions.md to project instructions, or attach it as a source when the instruction editor is unavailable. Ask Work to list the sources it can actually read before continuing. A path alone does not prove access.

### 6. Request the brief

Copy prompts/task.txt into the Work task. Ask for the short plan first. Check that the plan uses only BAK-101, labels unknowns and returns the four named files. Reply: Proceed with this plan; keep all outputs as classroom drafts.

### 7. Review the ledger

Open claim-ledger.csv. Compare each fee, duration, schedule and location against the BAK-101 record. Add a row for remaining seats with status UNKNOWN. Confirm that class_size 12 was not treated as twelve available seats.

### 8. Save and checkpoint

Download the four artifacts into C818-marketing/campaign, or confirm them on disk in the local route. Open each file. Record any corrections in unknowns.md. Keep these files for Lab 2. If the task stalled, copy this lab’s checkpoints files into campaign and label them supplied sample drafts.

## Task prompt

Copy `prompts/task.txt` into the Work task. Review the plan before authorising production.

```text

Use the attached Cook & Bake Academy brand.md, market-brief.md and data/courses.json. Create a campaign brief for BAK-101 Artisan Sourdough Bread Baking aimed at weekend home bakers, with a secondary proposed cafe-business audience angle. Use no other fact sources. First propose a short plan; wait for my review before drafting.
After I approve the plan, return four files: brief.md (audience need, objective, message, CTA, scope and draft status), selected-course.json (the exact BAK-101 record), claim-ledger.csv (claim,value,source_field,status) and unknowns.md (unknown,impact,next_action). Copy source facts exactly. Record remaining seats, discounts, tax treatment, public booking link, campaign performance and sales target as UNKNOWN. A class capacity is not seats remaining. Do not add a cafe course. Do not publish, post or send anything.

```

## Test it

- The saved selected-course.json has code BAK-101, fee 680, weeks 4 and campus Orchard Road.

- The brief identifies one audience need and one primary CTA.

- Every offer fact has a source_field; missing details are UNKNOWN.

- All four files open and are labelled classroom draft.

## Troubleshooting

**Work cannot find local files:** Use the project Sources upload route; attach the exact three files, then ask for the visible source list again.

**The website is blank or courses do not load:** Serve from the cnbacademy folder, not its parent, and use http://localhost:8080 rather than file://. Use port 8081 if 8080 is occupied.

**Work invents an offer:** Name the unsupported sentence, request its removal and compare the regenerated ledger with the catalogue.

## Challenge

Repeat the brief for BAK-107, keeping a separate folder and ledger so its three-week duration cannot leak into the BAK-101 campaign.

## Reflection

Which facts came from the catalogue, and which parts of your brief are proposals?

## Checkpoint and rejoin

The `checkpoints/` folder contains supplied classroom sample files. Copy only the files needed into your working campaign, identify them as samples and verify them against the sources before continuing. The sample is a recovery route, not a substitute for reviewing your own work.

**C818 · Tertiary Infotech Academy Pte Ltd · Classroom drafts only.**
