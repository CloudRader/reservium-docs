"""Check local Markdown links and asset references in the documentation."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import typer

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
app = typer.Typer(help="Check local Markdown links and asset references.")

INLINE_LINK = re.compile(
    r"(?P<image>!)?\[[^\]]*\]\(\s*(?:<(?P<bracketed>[^>]*)>|(?P<plain>[^)\s]*))"
)
REFERENCE_LINK = re.compile(
    r"^\s{0,3}\[[^\]]+\]:\s*(?:<(?P<bracketed>[^>]*)>|(?P<plain>\S+))"
)
HTML_REFERENCE = re.compile(r"\b(?:src|href)=(?P<quote>[\"'])(?P<target>.*?)(?P=quote)")
FENCE = re.compile(r"^\s*(```|~~~)")


def is_local_target(target: str) -> bool:
    """Return whether a target should be resolved within the repository."""
    parsed = urlsplit(target)
    return not parsed.scheme and not parsed.netloc and not target.startswith(("#", "/"))


def extract_targets(line: str) -> list[str]:
    """Extract local-reference candidates from one Markdown source line."""
    targets = [
        match.group("bracketed") or match.group("plain") or ""
        for match in INLINE_LINK.finditer(line)
    ]
    targets.extend(
        match.group("bracketed") or match.group("plain") or ""
        for match in REFERENCE_LINK.finditer(line)
    )
    targets.extend(match.group("target") for match in HTML_REFERENCE.finditer(line))
    return targets


def check_file(source: Path, root: Path) -> list[tuple[Path, int, str]]:
    """Return broken local references from one Markdown file."""
    broken: list[tuple[Path, int, str]] = []
    in_fence = False

    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for target in extract_targets(line):
            target = target.strip()
            if not target or not is_local_target(target):
                continue

            parsed = urlsplit(target)
            path = (source.parent / unquote(parsed.path)).resolve()
            if not path.exists():
                broken.append((source.relative_to(root), line_number, target))

    return broken


@app.command()
def check(
    docs_dir: Path = typer.Option(
        DOCS_DIR,
        exists=True,
        file_okay=False,
        dir_okay=True,
        help="Directory containing Markdown documentation.",
    ),
) -> None:
    """Check local links and asset references in Markdown files."""
    docs_dir = docs_dir.resolve()
    root = docs_dir.parent
    broken = [
        issue
        for source in sorted(docs_dir.rglob("*.md"))
        for issue in check_file(source, root)
    ]

    if not broken:
        print("Internal documentation links and assets are valid.")
        return

    print(f"Found {len(broken)} broken local documentation reference(s):")
    for source, line_number, target in broken:
        print(f"- {source}:{line_number}: {target}")
    raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
