---
name: proofwork
description: Turn a real job posting into a simulated "first assignment" for that role (fictional company, messy data, AI manager, AI review, portfolio report). Use when the user wants to practice a job, run a ProofWork simulation, or says "proofwork". Data Analyst and Data Engineer roles first.
---

# ProofWork (skeleton, Phase 0)

You are running the ProofWork skill. It is still a skeleton: only the welcome
step works. Do not invent features that are not built yet.

## What to do now

1. Greet the user in one line and say ProofWork is in early development.
2. Explain the planned flow in 5 short bullets:
   - Paste a job posting.
   - ProofWork extracts role, skills, tools, seniority.
   - It builds a fictional company with realistic messy data and tasks.
   - An AI manager assigns tasks over 1-2 weeks; you submit work.
   - An AI reviewer scores each skill and builds a portfolio report.
3. Say: "The job posting parser arrives in Phase 1."
4. Stop. Do not start a simulation.

## Rules (apply in every future phase)

- Never save the user's job postings or submissions inside the repo except
  under `workspace/` or `private/` (both gitignored).
- Fictional company only. Never pretend to be a real company.
