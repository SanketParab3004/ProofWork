# Progress

## Current phase
Phase 0: Setup (almost done; GitHub repo not created yet)

## Done
- 2026-11-10: Folder structure, notes files, AGENTS.md + CLAUDE.md, .gitignore, .env.example,
  MIT license, README draft, Python env (uv, Python 3.12, pytest, 1 smoke test passing),
  skill skeleton at `.claude/skills/proofwork/SKILL.md`, `git init` + first local commit.

## Next step (exact)
1. User runs `gh auth login` (GitHub account `SanketParab3004`) in a new terminal.
2. Get noreply email: `gh api user --jq '"\(.id)+\(.login)@users.noreply.github.com"'`,
   set it as local `user.email`, then `git commit --amend --reset-author --no-edit`.
3. With user's OK: `gh repo create SanketParab3004/ProofWork --public --source . --push`.
4. Test the skill skeleton in Codex CLI (see deadline below).
5. Tag `v0.0.1` (end of Phase 0), learning recap, then start Phase 1 (job posting parser).

## Deadlines
- **2026-11-24: Codex + ChatGPT Plus access ends.** Test the skill in Codex CLI
  BEFORE this date (copy/link skill to `.agents/skills/proofwork/` and check it loads).

## Open problems
- First commit uses placeholder noreply email `SanketParab3004@users.noreply.github.com`;
  replace with the ID-based one after `gh auth login` (step 2), before pushing.
- Codex skill folder path to confirm when testing (`.agents/skills/` expected).

## LinkedIn posts
| # | Milestone | Planned | Drafted | Posted |
|---|-----------|---------|---------|--------|
| 1 | After Phase 1 (problem + "no experience" story + screenshot) | | | |
| 2 | After Phase 3 (first full simulation, screen recording) | | | |
| 3 | After Phase 5 (sample report + one hard lesson) | | | |
| 4 | After Phase 6 (open-source release, ask for testers) | | | |
| 5 | After Phase 7 / real users | | | |
