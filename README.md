# Reservium Documentation

Official documentation repository for **Reservium**.

This repository contains the complete documentation website, including:

- 📖 User Guide
- 👨‍💼 Manager Guide
- 🏗️ Hosting Guide
- 🤝 Contributor Guide
- 🔌 API Reference
- 📝 Release Notes

The documentation is built with **Zensical** and automatically deployed to **GitHub Pages**.

---

## Features

- Markdown-based documentation
- Automatic site generation with Zensical
- Versioned release notes generated from Backend and Frontend repositories
- Automated GitHub Pages deployment
- Conventional Commit and Release Please integration
- Pre-commit hooks for repository consistency

---

## Project Structure

```text
.
├── docs/                  # Documentation pages and assets
├── scripts/
│   └── fetch_releases.py  # Generates release notes
├── site/                  # Generated static site
├── .github/workflows/     # CI/CD and deployment workflows
├── Makefile               # Common local development commands
├── zensical.toml          # Site configuration
├── pyproject.toml
└── uv.lock
```

---

## Requirements

- Python **3.14.3**
- [uv](https://github.com/astral-sh/uv)

---

## Installation

Clone the repository and install the project dependencies:

```bash
make install
```

The Makefile uses `uv` and provides the standard local workflow. Use `uv run`
directly for commands without a Make target.

---

## Development

### Build the documentation

```bash
make build
```

The generated website is written to:

```text
site/
```

### Run a local development server

```bash
make serve
```

The server automatically rebuilds the site when documentation changes.

---

## Writing Documentation

Documentation pages live under:

```text
docs/
```

When adding or moving pages:

- update the navigation in `zensical.toml`
- keep related images inside `docs/assets/` or the corresponding section's `assets/` directory
- prefer keeping assets close to the pages that use them

---

## Release Notes

Release notes are generated from the Backend and Frontend repositories.

To regenerate them:

```bash
make fetch-release-notes
```

This updates:

```text
docs/release-notes/backend.md
docs/release-notes/frontend.md
```

> **Note**
>
> The script downloads changelogs from GitHub and replaces the generated files.

---

## Quality Checks

Before opening a pull request, run:

```bash
make check
```

To run only the pre-commit hooks, use `make pre-commit`. To install them as a
Git hook, use `make pre-commit-install`. The whitespace-only check is available
as `make diff-check`.

The configured pre-commit hooks validate:

- trailing whitespace
- final newlines
- YAML formatting
- TOML formatting
- large added files

---

## Release Process

This repository follows **Conventional Commits**.

Examples:

```text
docs: improve installation guide
docs(user-guide): update reservation workflow
fix(api-reference): correct endpoint example
chore(deps): update zensical
```

Release Please automatically:

1. Creates releases from commits.
2. Generates changelog entries.
3. Publishes a new release.
4. Synchronizes release notes.
5. Builds the documentation.
6. Deploys the site to GitHub Pages.

Generated release-note files should generally **not** be edited manually.

---

## CI/CD

GitHub Actions automatically:

- install dependencies with `uv`
- build the documentation
- synchronize generated release notes
- deploy the generated site to GitHub Pages

---

## Security

Please do not commit:

- API tokens
- credentials
- private keys
- production `.env` files

Documentation examples should always use placeholder values instead of real secrets.

---

## Contributing

When contributing:

1. Create a descriptive branch.
2. Follow Conventional Commits.
3. Build the documentation locally.
4. Run pre-commit checks.
5. Open a Pull Request.

Example branch names:

```text
docs/update-user-guide
docs/improve-hosting-guide
fix/api-reference-links
```

---

## Troubleshooting

### Zensical build fails

Verify that every page referenced in `zensical.toml` exists under `docs/`.

### Release notes cannot be generated

Ensure:

- network access is available
- the Backend and Frontend repositories expose `CHANGELOG.md`

### Dependency issues

Use `uv` to update dependencies.

Do not edit `uv.lock` manually.

---

## License

See the repository license for details.
