# Decisions

## 2026-11-10
- **Python 3.12 + uv** – already installed, fast, free, one tool for env + packages + lockfile.
- **src/ layout (`src/proofwork/`)** – keeps core logic a clean package, provider-free, shared
  by skill mode and the web app.
- **pytest** – the standard, simplest Python test tool.
- **MIT license** – simplest, most popular permissive license; good for a portfolio project
  others may reuse. (Apache-2.0 is the alternative if patent protection matters later.)
- **Skill at `.claude/skills/proofwork/SKILL.md`** – Claude Code auto-loads project skills from
  there. Codex CLI reads skills from `.agents/skills/`; we'll add/sync it when testing Codex
  (before 2026-11-24) instead of keeping two copies now.
- **AGENTS.md canonical, CLAUDE.md imports it (`@AGENTS.md`)** – one set of rules for both agents.
- **Privacy** – `private/` and `workspace/` gitignored for real postings, resumes, submissions.
  Local git identity = `SanketParab3004` + GitHub noreply email, never a personal email.
- **Copyright holder in LICENSE = GitHub username** – avoids putting a real name in the repo.
