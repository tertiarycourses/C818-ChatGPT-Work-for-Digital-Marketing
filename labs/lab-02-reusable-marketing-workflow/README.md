# Lab 02 — Build a reusable marketing workflow

**C818 · Topic 1 · 50 minutes · Version 1.0**

## Goal

Create and trial a source-grounded production playbook for the campaign.

## What you’ll build

campaign/workflow.md, campaign/brand-check.md and campaign/workflow-trial.md. The playbook carries the same rules into flyer, social and email production.

## Prerequisites

Lab 1 campaign files. This lab includes adapted brand-voice, flyer-design and social-post skill examples. They are reading resources until installed and enabled.

## Steps

### 1. Gather the current context

Open the Lab 1 brief and claim ledger. Copy assets/skills into C818-marketing/skills-examples so the brand and creative workflow examples remain together. Read brand-voice/SKILL.md before flyer-design/SKILL.md and social-post/SKILL.md.

### 2. Translate the reference workflow

Write the seven stages in campaign/workflow.md: goal, plan, create, preserve context, version, prepare distribution and verify. For each stage name an input, output and check. Do not copy terminal-specific Claude commands into the Work task.

### 3. Resolve the fact-source paths

In your working copy, resolve data/courses.json to cnbacademy/data/courses.json. The optional campaign/term-highlights.md is absent, so instruct Work to use the catalogue only. Do not create promotional facts just to satisfy a skill reference.

### 4. Draft the reusable playbook

Attach the example skill files, brief and ledger to Work. Paste prompts/task.txt. Review the returned workflow and brand checklist. Check the exact tagline Learn it. Make it. Take it further.

### 5. Choose a supported reuse route

The guaranteed classroom route is to add workflow.md to project Sources and cite it in each task. If skill creation is available, select @skill-creator in ChatGPT, ask it to package the reviewed workflow as a skill, then enable the resulting skill. Use its displayed name through an @ mention in a new task. Installation is optional; merely uploading SKILL.md does not enable automatic discovery.

### 6. Run a small trial

Ask Work: Using workflow.md and the BAK-101 source record, produce a 60-word course introduction and a claim ledger, then stop for review. Save the result as workflow-trial.md. No image generation or connected email tool is needed.

### 7. Inspect the trial

Check the trial for unsupported urgency, discounts, invented chef names and changed dates. Confirm the practical voice and exact course title. Record at least one specific improvement in brand-check.md, even if it is a wording choice.

### 8. Save the checkpoint

Keep workflow.md and brand-check.md with the Lab 1 campaign files. Record whether you used Sources or an enabled skill. If setup stalled, copy checkpoints/workflow.md and trial it using the source-upload route.

## Task prompt

Copy `prompts/task.txt` into the Work task. Review the plan before authorising production.

```text

Review the attached brand-voice, flyer-design and social-post workflow examples. Adapt them into one ChatGPT Work marketing playbook for the C818 classroom campaign. Use the BAK-101 brief and catalogue as the only offer facts. Return workflow.md with the seven-stage process, named inputs/outputs, fact checks, format rules and a stop-before-distribution boundary. Return brand-check.md covering the exact tagline, practical voice, palette, editable copy, alt text and unsupported claims. Explain how to reuse the file through project Sources; do not claim that a file is an enabled skill unless it was actually installed. Preserve UNKNOWN for absent campaign facts.

```

## Test it

- workflow.md has seven named stages with inputs, outputs and checks.

- The tagline and academy palette match the supplied brand examples.

- The trial has no invented discounts, chef names or seat availability.

- The reuse route is recorded accurately: uploaded source or installed skill.

## Troubleshooting

**The @ skill name does not appear:** Use workflow.md as an uploaded source; do not claim automatic skill invocation.

**A source path is broken:** Point the task to cnbacademy/data/courses.json and remove the absent term-highlights source.

**The trial sounds generic:** Ask for one practical learner benefit from the exact learning outcomes, and remove unsupported superlatives.

## Challenge

Create an email-only workflow extension that requires an audience rule, plain-text version, review log and a separate send approval.

## Reflection

What did the reusable workflow prevent that a one-off prompt might miss?

## Checkpoint and rejoin

The `checkpoints/` folder contains supplied classroom sample files. Copy only the files needed into your working campaign, identify them as samples and verify them against the sources before continuing. The sample is a recovery route, not a substitute for reviewing your own work.

**C818 · Tertiary Infotech Academy Pte Ltd · Classroom drafts only.**
