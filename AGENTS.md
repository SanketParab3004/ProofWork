# ProofWork: instructions for AI coding agents

Read by Codex CLI (AGENTS.md) and Claude Code (via CLAUDE.md, which imports this file).

## Session routine (always)

- **Start of session:** read `NOTES/PROGRESS.md`, `NOTES/LEARNING_LOG.md`,
  `NOTES/DECISIONS.md`. Give the user a 3-line recap (phase, last done, next
  step), then continue from "Next step".
- **End of session:** update all three notes files:
  - `PROGRESS.md`: current phase, done, exact next step, open problems, LinkedIn post dates.
  - `LEARNING_LOG.md`: concepts learned in simple words + what to practice.
  - `DECISIONS.md`: technical choices and why.

## How to work with the user

- Short, simple replies. Elaborate only when asked.
- Teach as you build: before a new concept or tool, explain what it is and why (2-3 lines).
- Let the user write key code: give small tasks, then review their code.
- Small steps. One working piece at a time. Test before moving on.
- Prefer simple, popular, free tools. Say so BEFORE suggesting anything that costs money.

## Architecture rules

- Core logic in `src/proofwork/` (parser, simulation generator, manager,
  reviewer, report builder) must not depend on any AI provider.
- Skill mode (`.claude/skills/proofwork/`) and the later web app share that core.
- The web app must never log in with a user's Claude/ChatGPT subscription.
  Only bring-your-own API key or free options (Gemini free tier, Ollama).
- Write pytest tests for core logic. Run: `uv run pytest`.

## Privacy and Git (hard rules)

- No API keys or secrets in code or Git. Use `.env` (gitignored); `.env.example` has empty names only.
- No personal data in the repo: profiles, resumes, real job postings and real
  submissions go in `private/` or `workspace/` (both gitignored). Tests use synthetic data only.
- Commit identity for this repo is local: GitHub user `SanketParab3004` with its
  GitHub noreply email. Never use a personal email.
- Check `git status` and `git diff --staged` before every commit.
- Commit at each working milestone with a clear message.
- **Ask the user before every `git push`.**
- End of each phase: learning recap, Git tag/release, README update.

## LinkedIn

- Draft posts only at milestones (after Phases 1, 3, 5, 6, 7). Short, honest, no hype:
  hook, what was built, what was learned, visual idea, 3-5 hashtags.
- Never post. Track dates in `NOTES/PROGRESS.md`.
