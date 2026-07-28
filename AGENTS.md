# AGENTS.md

## Project Overview

`reservium-docs` contains the documentation site for Reservium, including user,
manager, hosting, contributor, API reference, and release-note sections. It is
a single-package Python project that uses Zensical for Markdown site generation.

Key paths:

- `docs/`: Markdown pages and static assets.
- `zensical.toml`: Site configuration, navigation, theme, and Markdown extensions.
- `scripts/fetch_releases.py`: Fetches Backend and Frontend changelogs from GitHub.
- `site/`: Generated site output. The GitHub Pages workflow rebuilds this directory.
- `.github/workflows/`: Release-note, release, and deployment automation.

## Setup

Prerequisites:

- `uv`.
- Python `3.14.3`, as pinned by `pyproject.toml` and Renovate configuration.

Install the locked dependencies from the repository root:

```bash
uv sync
```

Use `uv run ...` for project commands so the managed environment and lockfile
are respected. Do not commit `.venv` or generated cache files.

## Development Workflow

Build the documentation site locally:

```bash
uv run zensical build --clean
```

The generated files are written to `site/`. To preview the site with Zensical,
run:

```bash
uv run zensical serve
```

Edit Markdown under `docs/` and update the `nav` structure in `zensical.toml`
when adding or moving pages. Keep image and stylesheet assets near the
documentation tree in `docs/assets/` or the relevant section's `assets/`
directory.

Generate release-note pages from the current `main` branches of the Backend and
Frontend repositories with:

```bash
uv run scripts/fetch_releases.py
```

The script writes `docs/release-notes/backend.md` and
`docs/release-notes/frontend.md`. It requires network access to GitHub and
should be run deliberately because it replaces those generated files.

## Testing and Checks

There is no application test suite in this repository. Before submitting
documentation changes, run the build and repository hygiene hooks:

```bash
uv run zensical build --clean
pre-commit run --all-files
```

The pre-commit configuration checks trailing whitespace, final newlines, YAML,
TOML, and unusually large added files. If `pre-commit` is not installed, run
the checks through the project's configured environment or install it locally
before making a contribution.

## Code and Content Conventions

- Use ASCII for new source text unless the content or existing file requires
  another character set. Existing release-note headings may contain Unicode.
- Keep source documentation under `docs/` and site configuration in
  `zensical.toml`.
- Python code should remain type-annotated and formatted consistently with the
  existing `scripts/fetch_releases.py` style.

## Documentation Pages

For adding or updating documentation pages, use the repository-local skill
[`create-update-pages`](.agents/skills/create-update-pages/SKILL.md). It is the
source of truth for page structure, clarification questions, writing style,
icons, admonitions, screenshots, asset placement, relative links, and
navigation changes. Read and follow that skill before editing files under
`docs/`; keep this guide focused on repository-wide workflows and constraints.

## Release and Deployment

Commits follow Conventional Commits, for example:

```text
docs: clarify Docker installation
fix(api-reference): correct endpoint link
chore(deps): update zensical
```

Release Please uses the commit type to group entries in the changelog. Use
these recognized types when applicable: `feat`, `chore`, `fix`, `deps`,
`refactor`, `docs`, `test`, and `ci`. The configuration uses a simple release
type, does not include a component in tags, and always bumps the patch version
when a release is created. Keep commit subjects concise and describe the user-
visible or maintenance change accurately.

When a change is localized, include a specific scope in parentheses after the
commit type. Prefer the affected guide or subsystem name, for example
`docs(user-guide)`, `docs(manager-guide)`, `docs(hosting-guide)`,
`docs(contribute-guide)`, `feat(api-reference)`, `chore(hosting)`,
`fix(deps)`, or `ci(release-please)`. Choose the scope from the change's
context; do not use a broad scope when a more precise area is clear.

Release Please runs on pushes to `main`. After a successful release, the
release-note sync workflow updates the generated release-note pages, and the
build workflow runs `uv sync`, `uv run zensical build --clean`, and deploys
`site/` to GitHub Pages. Contributors generally should not edit generated
release-note files by hand.

## Security and Secrets

- Never commit tokens, credentials, private keys, or production `.env` files.
- The release-note fetch script currently uses public GitHub raw URLs; do not
  add credentials to source files or committed configuration.
- Documentation examples must use placeholders for external service secrets.

## Pull Requests

Use a descriptive branch name with a Conventional Commit type where practical,
such as `docs/update-hosting-guide`. Before opening a pull request, run the
Zensical build and `pre-commit run --all-files`, and include any generated
documentation updates that are intentionally part of the change.

## Troubleshooting

- If Zensical fails after navigation changes, check that every path in
  `zensical.toml` exists under `docs/`.
- If release-note generation fails, verify network access and that the source
  repositories expose `CHANGELOG.md` on the requested branch.
- Use `uv.lock` as the dependency source of truth; update it through `uv`, not
  by hand.
