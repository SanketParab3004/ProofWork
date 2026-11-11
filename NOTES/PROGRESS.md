# Progress

## Current phase
Phase 1: Job posting parser (not started). Phase 0 done, tagged v0.0.1.

## Done
- 2026-11-10: Folder structure, notes files, AGENTS.md + CLAUDE.md, .gitignore, .env.example,
  MIT license, README draft, Python env (uv, Python 3.12, pytest, 1 smoke test passing),
  skill skeleton at `.claude/skills/proofwork/SKILL.md`, `git init` + first local commit.
- 2026-11-10: `gh auth login` done; local `user.email` = GitHub noreply
  (`133170529+SanketParab3004@...`); public repo created and pushed:
  https://github.com/SanketParab3004/ProofWork
- 2026-11-10: User ran `/proofwork` in Claude Code themselves: works. Tagged `v0.0.1`
  (Phase 0 done, Codex test carried over).

## Next step (exact)
1. Start Phase 1: job posting parser (plan the data shape first: role, skills, tools, seniority).
2. Carry-over from Phase 0: test the skill in Codex CLI on/after 2026-11-12 (no Codex
   access until then) and before 2026-11-24.

## Deadlines
- **2026-11-24: Codex + ChatGPT Plus access ends.** Test the skill in Codex CLI
  BEFORE this date (copy/link skill to `.agents/skills/proofwork/` and check it loads).

## Open problems
- `gh` may not be on PATH in old shells; use "C:\Program Files\GitHub CLI\gh.exe".
- Codex skill folder path to confirm when testing (`.agents/skills/` expected).

## LinkedIn posts
| # | Milestone | Planned | Drafted | Posted |
|---|-----------|---------|---------|--------|
| 1 | After Phase 1 (problem + "no experience" story + screenshot) | | | |
| 2 | After Phase 3 (first full simulation, screen recording) | | | |
| 3 | After Phase 5 (sample report + one hard lesson) | | | |
| 4 | After Phase 6 (open-source release, ask for testers) | | | |
| 5 | After Phase 7 / real users | | | |
