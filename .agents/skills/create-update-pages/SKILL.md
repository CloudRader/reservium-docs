---
name: create-update-pages
description: Create or update pages in the Reservium documentation repository. Use this skill whenever the user asks to add a documentation page, edit an existing guide, document a feature, explain a setup flow, add screenshots, reorganize a guide, or make documentation look consistent. Always inspect neighboring pages and the configured navigation first, ask targeted questions when the requested behavior or facts are incomplete, and preserve the repository's existing structure, writing style, icons, assets, and Zensical rendering conventions.
---

# Reservium Documentation Pages

This is a repository-local skill. Apply it only to this `reservium-docs`
repository and its `docs/` tree. The goal is to produce pages that read and
look like the surrounding documentation, while avoiding invented product
behavior.

## Clarify Before Editing

Start by classifying the request as a new page, an edit, a move, or a removal.
Inspect the nearest pages in the same guide and the matching navigation block
in `zensical.toml` before asking questions.

Ask only the questions needed to remove ambiguity. At minimum, establish:

- Target guide and path: `user-guide`, `manager-guide`, `hosting-guide`,
  `contribute-guide`, `api-reference`, or `release-notes`.
- Intended audience, required role or permissions, and expected outcome.
- The factual source: implementation, issue, release, screenshot, API schema,
  or user-provided behavior. Treat missing facts as unknown.
- The user workflow or procedure, including prerequisites, inputs, states,
  errors, permissions, and what success looks like.
- Whether screenshots, diagrams, code blocks, external links, or cross-links
  are required, and which source assets are available.
- For an edit, which statements are outdated and whether existing links or
  assets must remain compatible.

Do not guess product behavior, UI labels, permissions, URLs, version numbers,
configuration values, or screenshots. Mark an unresolved fact for the user or
request the authoritative source before documenting it. Use placeholders in
examples for secrets and environment-specific values.

## Repository Structure

Use the existing section layout:

- `docs/user-guide/`: end-user workflows and features.
- `docs/manager-guide/`: manager and superuser workflows.
- `docs/hosting-guide/`: installation, configuration, update, and operations.
- `docs/contribute-guide/`: contribution and developer guidance.
- `docs/api-reference/`: API entry page and bundled API reference assets.
- `docs/release-notes/`: generated release notes; do not manually rewrite these
  unless the user explicitly requests a source or generated-note update.

Put page-specific images in an `assets/` directory beside the page or beside
its section, matching the nearest existing pattern. Use paths relative to the
Markdown file, for example `![Calendar view](assets/calendar-view.png)`.
Keep shared branding in `docs/assets/`, especially `logo.png` and
`assets/stylesheets/extra.css`; do not duplicate shared assets in guide folders.

When adding or moving a page, update the corresponding `nav` entry in
`zensical.toml`. Check that every navigation path exists and that relative
links still resolve from the page's directory. Do not add a page to navigation
without confirming its final path and title.

## House Style

Match the closest neighboring pages rather than introducing a new format.

- Use optional Zensical front matter for page metadata, normally an icon:

  ```yaml
  ---
  icon: lucide/circle-plus
  ---
  ```

- Use one H1 with a concise title and, where the surrounding section does so,
  a Font Awesome or Material icon followed by `{ .main-color }`, for example
  `# Create Reservation :material-plus-circle-outline:{ .main-color }`.
- Use `---` between major opening content and the first substantial section,
  and keep the hierarchy ordered: H1, H2 sections, H3 subsections.
- Prefer direct, task-oriented prose. State what the user can do, then explain
  prerequisites, steps, controls, results, and recovery paths.
- Use numbered steps for procedures, bullets for sets of facts or options, and
  tables only for compact comparisons such as permissions or error types.
- Bold UI labels and important values. Use backticks for commands, filenames,
  environment variables, paths, and literal API values.
- Use the configured Markdown extensions: admonitions such as `!!! info`,
  `!!! warning`, `!!! danger`, and `!!! tip`; fenced code blocks with an
  appropriate language; and Material grid cards only where neighboring index
  pages use them.
- Use icons sparingly and consistently with the subject. Reuse the existing
  Font Awesome and Material icon syntax; do not add custom inline SVGs for
  ordinary page decoration.
- Keep wording, capitalization, terminology, and role names consistent with
  nearby pages. Preserve existing terminology when editing an established
  page.

## Screenshots and Assets

Use screenshots when they show the actual UI state needed to complete a task.
Do not invent, crop away, or replace important controls in a screenshot.
Name files descriptively in lowercase kebab-case, such as
`calendar-view.png` or `reservation-successful.png`.

For each screenshot:

1. Confirm its source, UI state, and page-specific location.
2. Save it under the nearest relevant `assets/` directory.
3. Reference it with a relative Markdown image link and a useful alt text.
4. Explain the action or state shown immediately before or after the image.
5. Check that the asset exists and is readable before finishing.

The global stylesheet already gives article images a border, rounded corners,
shadow, and spacing. Do not add per-page image CSS unless the page has a
verified special requirement, such as the API iframe layout.

## Editing Workflow

1. Read the target page, two nearby pages when available, the relevant
   `zensical.toml` navigation block, and any referenced assets.
2. Ask focused clarification questions for missing facts. If the user answers
   partially, document only the confirmed behavior and list remaining gaps.
3. State a short content outline and identify whether navigation or assets will
   change.
4. Edit the smallest appropriate set of files. Preserve unrelated wording,
   links, generated release notes, and user changes.
5. Check headings, front matter, icons, admonitions, relative links, image
   references, code fences, and navigation ordering.
6. Build and run repository checks before reporting completion.

## Validation

From the repository root, run:

```bash
uv run zensical build --clean
pre-commit run --all-files
git diff --check
```

If a full pre-commit run reports unrelated existing files, run the relevant
hooks against the changed files and report the unrelated failure explicitly.
The Zensical build is required because it catches broken navigation, malformed
Markdown, and rendering configuration errors. Do not claim a page is complete
if the build fails; fix the issue or explain the blocker.

## Completion Report

Summarize the changed page(s), navigation entries, and assets. Mention any
facts that were intentionally left unresolved, then report the exact checks
run and their results.
