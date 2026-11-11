# ProofWork

> Turn any real job posting into a realistic simulated "first assignment" for that role.

**Status:** early development. Phase 0 (setup) done; Phase 1 (job posting parser) next.

## The problem

"Entry-level" jobs ask for experience. Tutorials don't feel like real work:
the data is clean, the task never changes, and no one reviews your work.
ProofWork gives you a realistic first assignment for the exact job you want,
plus honest feedback and a report you can share.

## How it works (planned)

1. Paste a job posting.
2. ProofWork extracts the role, skills, tools and seniority.
3. It creates a fictional company with realistic, messy datasets and a task list.
4. An AI "manager" assigns tasks over 1–2 weeks, answers questions, and changes requirements.
5. You submit work: code, SQL, dashboards, written answers.
6. An AI reviewer gives senior-colleague feedback and a rubric score per skill.
7. You get a shareable portfolio report.

First roles: **Data Analyst** and **Data Engineer**.

## Two modes

- **Skill mode (first):** an installable skill for Claude Code and Codex CLI.
  Runs on your own Claude or ChatGPT subscription. No API key needed.
- **Web app (later):** bring your own API key (Claude, OpenAI, Gemini) or use a free
  option (Gemini free tier / Ollama). It never logs in with your subscription.

## Demo

_Screenshots and a demo video will be added after Phase 1._

## Tech stack

- Python 3.12, [uv](https://docs.astral.sh/uv/) for environments, pytest for tests
- Claude Code / Codex CLI skills (`SKILL.md`)
- Later: FastAPI, SQLite/PostgreSQL, Streamlit (then React)

## Install and run (developers)

```bash
git clone https://github.com/SanketParab3004/ProofWork.git
cd ProofWork
uv sync
uv run pytest
```

Try the skill skeleton: open the folder in Claude Code and type `/proofwork`.

## Roadmap

- [x] Phase 0: Setup (repo, Python env, notes, skill skeleton)
- [ ] Phase 1: Job posting parser
- [ ] Phase 2: Simulation generator (company, messy data, tasks)
- [ ] Phase 3: AI manager (tasks over time, follow-ups, changing requirements, saved progress)
- [ ] Phase 4: Submissions + AI review (rubric per skill)
- [ ] Phase 5: Portfolio report (HTML/PDF)
- [ ] Phase 6: Polish skill mode (Claude Code + Codex CLI), install guide, first release
- [ ] Phase 7: Web app (provider layer, simple UI, free hosting)

## License

[MIT](LICENSE)
