# CLAUDE.md

Guidance for Claude Code and other AI coding agents working in this repository.

Translate is a Python command-line translation tool with support for multiple providers (MyMemory, Microsoft, DeepL, LibreTranslate, Yandex).

Repo conventions live in `.cursor/rules/`:
- **basic-development.mdc** — Nix environment, test commands, test practices
- **issue.mdc** — workflow for fixing GitHub issues
- **translate-rule.mdc** — how to add or modify translation providers

Run repo tooling with `nix develop -c …` unless you are already inside `nix develop`. **Git commands do not need the Nix prefix** — run `git` directly.

## Development Environment

This project uses Nix for environment management. Run `nix develop` once per terminal session, then install dependencies:

```bash
pip install --user -r requirements-dev.txt
```

## Common Commands

| Task | Command |
|------|---------|
| Run all tests | `nix develop -c pytest` |
| Run tests via Makefile | `nix develop -c make test` |
| Lint / format checks | `nix develop -c make lint` |
| Build package | `nix develop -c make build` |

Always run the full test suite, not a single file, before finishing a task.

## Architecture

### Tech Stack

- **CLI:** Python, Click
- **HTTP:** requests (via provider classes)
- **Testing:** pytest, VCR.py (cassettes in `tests/fixtures/cassettes/`)
- **Dev Environment:** Nix (`flake.nix`)

### Directory Structure

```
translate-python/
├── translate/                 # Main package
│   ├── __main__.py            # CLI entry point (translate-cli)
│   ├── main.py                # Click commands and config
│   ├── translate.py           # Translator class and provider registry
│   ├── providers/             # Translation provider implementations
│   │   ├── base.py            # BaseProvider ABC
│   │   ├── mymemory_translated.py
│   │   ├── microsoft.py
│   │   ├── deepl.py
│   │   ├── libre.py
│   │   └── yandex.py
│   ├── constants.py
│   └── exceptions.py
├── tests/                     # pytest tests
│   ├── test_main.py           # CLI tests
│   ├── test_translate.py      # Translator integration (VCR)
│   └── test_provider.py       # Provider unit tests
├── docs/                      # Sphinx documentation
├── flake.nix                  # Nix dev environment
└── pytest.ini                 # pytest config (--cov=translate)
```

## Code Conventions

- Test observable behavior: CLI output, translated text, error messages
- Use VCR cassettes for HTTP provider tests instead of live API calls
- Raise `TranslationError` from providers on API failures
- Register new providers in `PROVIDERS_CLASS` and `translate/providers/__init__.py`

## Skills

- **post-change-refactor** (`.cursor/skills/post-change-refactor/SKILL.md`) — clean up uncommitted changes before commit
