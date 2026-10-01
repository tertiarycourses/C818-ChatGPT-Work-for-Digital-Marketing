# Lab 07 — Prepare a segmented email campaign

**C818 · Topic 4 · 85 minutes · Version 1.0**

## Goal

Build an unsent three-email sequence for an explicitly eligible synthetic audience.

## What you’ll build

email/sequence.md, email/email-1.html, email/email-1.txt, email/segment.csv and email/send-checklist.md.

## Prerequisites

Labs 1–6 sources. A spreadsheet or Work data-analysis tools for the synthetic CSV; a browser for HTML preview. No real email platform or subscriber list is required.

## Steps

### 1. Prepare synthetic data

Create email inside C818-marketing. Copy assets/contacts.csv into email/contacts.csv. Open the CSV and confirm every address ends in example.com. These are invented contacts.

### 2. Define the eligibility rule

Write in send-checklist.md: consent = yes AND interest = bakery AND suppressed = no. Missing consent is excluded. This is a classroom rule; real production requirements need organisational review.

### 3. Filter and inspect

In a spreadsheet filter all three criteria, or ask Work to apply the rule to the CSV and return segment.csv. The expected IDs are C001, C004 and C006. Check each included and excluded row manually.

### 4. Plan the sequence

Attach the brief, course record and segment to Work. Paste prompts/task.txt. Review the introduction, clarification and reminder roles with proposed timing Day 1, Day 4 and Day 8. Do not invent an intake deadline or limited-seat claim.

### 5. Draft all three messages

After approving the plan, request sequence.md with a subject, preheader, body, one CTA and a neutral name fallback for each message. Keep a practical voice and scenario-only course facts.

### 6. Create a preview for Email 1

Ask Work to produce email-1.html as a simple single-column, 600 px maximum-width layout and email-1.txt with the same meaning. The HTML link uses https://example.com/courses/BAK-101 with utm_source=email, utm_medium=newsletter, utm_campaign=sourdough_oct_demo and utm_content=e1_a. Label the destination as a demo.

### 7. Review placeholders

Use a clearly labelled demo unsubscribe placeholder in the HTML and a provider-configuration note in send-checklist.md. Record production sender, physical address, live booking destination and unsubscribe setup as UNKNOWN. Do not substitute the academy’s fictional campus for an unverified sender address.

### 8. Preview and correct

Open email-1.html in a browser at desktop and 375 px width. Confirm the course facts are live text, the CTA is visible, the layout does not scroll horizontally and the plain-text version carries the same offer. This is a content preview, not a real inbox test.

### 9. Save the unsent checkpoint

Store all five deliverables. Mark send-checklist.md classroom draft — not sent. If the task stalled, use checkpoints/email-1.html and sequence.md, then verify the segment using the supplied CSV.

## Task prompt

Copy `prompts/task.txt` into the Work task. Review the plan before authorising production.

```text

Create an unsent three-email campaign for Cook & Bake Academy BAK-101 using only the reviewed campaign sources. First propose the sequence roles and relative timing for review. Apply consent=yes AND interest=bakery AND suppressed=no to contacts.csv and return segment.csv without adding anyone. After plan approval return sequence.md with introduction, clarification and reminder messages, each with subject, preheader, body, one CTA and a neutral name fallback. Return email-1.html and equivalent email-1.txt. Use a simple single-column layout, live text facts and an example.com demo CTA with the supplied UTM taxonomy. Use a labelled demo unsubscribe placeholder. Return send-checklist.md listing production sender, sender address, real booking link and provider unsubscribe setup as UNKNOWN. No actual upload, scheduling or send is authorised.

```

## Test it

- segment.csv contains exactly C001, C004 and C006, with all three rule fields satisfied.

- sequence.md has three distinct message roles and no invented urgency.

- Email 1 HTML and text versions carry the same source-checked facts.

- The HTML preview fits 375 px width and the checklist states not sent.

## Troubleshooting

**A suppressed contact is included:** Reapply all three criteria with AND, not OR, and inspect each row.

**A merge field appears literally:** Use the neutral fallback in the preview; configure real platform tags only during a separate production setup.

**A real email tool tries to send:** Stop the action and export the draft files only; no live send is part of this lab.

## Challenge

Create a subject-line B variant while keeping body, audience rule, CTA and timing fixed; document the hypothesis.

## Reflection

Why must recipient eligibility be checked before the copy is written?

## Checkpoint and rejoin

The `checkpoints/` folder contains supplied classroom sample files. Copy only the files needed into your working campaign, identify them as samples and verify them against the sources before continuing. The sample is a recovery route, not a substitute for reviewing your own work.

**C818 · Tertiary Infotech Academy Pte Ltd · Classroom drafts only.**
