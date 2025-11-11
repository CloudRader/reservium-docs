import requests
from pathlib import Path
import logging
from typing import Any
import typer

app = typer.Typer(help="Generate Markdown release notes from GitHub repositories.")

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

REPOS: dict[str, str] = {
    "Backend": "CloudRader/reservium-api",
    "Frontend": "CloudRader/reservium-ui",
}


def fetch_releases(repo_slug: str) -> list[dict[str, Any]]:
    """Fetch releases from a GitHub repository."""
    url = f"https://api.github.com/repos/{repo_slug}/releases"
    headers = {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def generate_markdown(releases: list[dict[str, Any]], title: str) -> str:
    """Generate Markdown content for releases."""
    md = "# %s Release Notes\n\n" % title
    if not releases:
        md += "_No releases found_\n"
        return md

    for release in releases:
        tag = release.get("tag_name", "_unknown_")
        body = release.get("body", "").strip() or "_No description_"
        md += "## %s\n\n%s\n\n---\n\n" % (tag, body)
    return md


@app.command()
def generate(
    output_dir: Path = typer.Option(Path("docs/release-notes"), help="Directory to save release notes"),
):
    """Fetch releases and generate Markdown files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for title, repo_slug in REPOS.items():
        logging.info("Fetching releases for %s...", repo_slug)
        releases = fetch_releases(repo_slug)
        md_content = generate_markdown(releases, title)
        output_file = output_dir / ("backend.md" if title == "Backend" else "frontend.md")
        output_file.write_text(md_content, encoding="utf-8")
        logging.info("✅ Generated %s", output_file)


if __name__ == "__main__":
    app()