import requests
from pathlib import Path
import logging
import typer
from typing import Dict

app = typer.Typer(help="Generate Markdown release notes from GitHub CHANGELOG.md files.")

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Map title -> repo slug
REPOS: Dict[str, str] = {
    "Backend": "CloudRader/reservium-api",
    "Frontend": "CloudRader/reservium-ui",
}


def fetch_changelog(repo_slug: str, branch: str = "main") -> str:
    """
    Fetch the raw CHANGELOG.md from the repository.

    :param repo_slug: GitHub repo in the format 'owner/repo'
    :param branch: branch name to fetch CHANGELOG from (default: main)
    :return: changelog content as string
    """
    url = f"https://raw.githubusercontent.com/{repo_slug}/{branch}/CHANGELOG.md"
    headers = {}  # optional: {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        logging.warning("CHANGELOG.md not found for %s on branch '%s'", repo_slug, branch)
        return "_No changelog found_"
    response.raise_for_status()
    return response.text


@app.command()
def generate(
    output_dir: Path = typer.Option(Path("docs/release-notes"), help="Directory to save release notes"),
    branch: str = typer.Option("main", help="Branch to fetch CHANGELOG.md from"),
):
    """
    Fetch CHANGELOG.md files from repositories and generate Markdown files for MkDocs.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    for title, repo_slug in REPOS.items():
        logging.info("Fetching CHANGELOG.md for %s...", repo_slug)
        changelog = fetch_changelog(repo_slug, branch)
        output_file = output_dir / ("backend.md" if title == "Backend" else "frontend.md")
        output_file.write_text(changelog, encoding="utf-8")
        logging.info("✅ Generated %s", output_file)


if __name__ == "__main__":
    app()
