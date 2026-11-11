# Learning log

## 2026-11-10 (Phase 0)

- **uv**: one fast tool that creates the Python virtual environment (`.venv`) and installs
  packages. `uv sync` = install everything from `uv.lock`. `uv run pytest` = run inside the env.
- **Virtual environment (.venv)**: a private Python folder per project so packages don't clash.
  Never committed to Git.
- **pyproject.toml**: the project's ID card (name, version, dependencies, tool settings).
- **uv.lock**: exact versions of every package, so everyone gets the same setup. Commit it.
- **src/ layout**: code lives in `src/proofwork/`; tests import it like a real user would.
- **pytest**: runs every `test_*.py` function; `assert` checks a result.
- **.gitignore**: list of files Git must never track (secrets, `.venv`, `private/`).
- **.env / .env.example**: `.env` holds real secrets (ignored); `.env.example` shows names only.
- **Skill (SKILL.md)**: a markdown file with a name + description at the top. Claude Code reads
  the description to know when to use it; `/proofwork` runs it directly.
- **AGENTS.md / CLAUDE.md**: standing instructions for AI agents. Codex reads AGENTS.md;
  CLAUDE.md imports it, so one file serves both.
- **Git basics**: `git init` (start tracking), `git add` (stage), `git commit` (save a snapshot),
  `git status` / `git diff --staged` (check before saving).
- **MIT license**: lets anyone use, change and share the code, as long as they keep the notice.
  No warranty.

- **GitHub + gh**: `gh repo create --source . --push` made the online repo and uploaded commits.
  `origin` = nickname for the GitHub copy. "ahead 1" = a local commit not yet pushed.
- **Noreply email**: GitHub gives each account a private address so commits never show your real email.
- **Tag (v0.0.1)**: a permanent name for one commit, used to mark milestones/releases.

### Phase 0 recap
Project skeleton, tests, notes, privacy-safe Git, public repo, and a skill that runs in Claude Code.

## Practice
- Run `git status`, `git log --oneline` and `uv run pytest` yourself.
- Add a second test to `tests/test_smoke.py` and make it pass.
- Next to learn: branch, push, pull request (when we create the GitHub repo).
