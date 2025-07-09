import os
from pathlib import Path
import typer

app = typer.Typer(help="Recursively remove unwanted system or metadata files.")

DEFAULT_PATTERNS = [".DS_Store", "Thumbs.db", ".Spotlight-V100", "desktop.ini", "._*"]


def match_pattern(file: str, patterns: list[str]) -> bool:
    from fnmatch import fnmatch

    return any(fnmatch(file, pattern) for pattern in patterns)


@app.command("clean")
def clean(
    directory: Path = typer.Argument(
        ..., exists=True, file_okay=False, help="Target directory to clean."
    ),
    patterns: list[str] = typer.Option(
        DEFAULT_PATTERNS,
        "--pattern",
        "-p",
        help="File patterns to remove (can use wildcards).",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Preview what will be deleted without removing anything.",
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Print each matched file."
    ),
):
    """Clean unwanted files from the target directory."""
    deleted = 0
    matched_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if match_pattern(file, patterns):
                full_path = os.path.join(root, file)
                matched_files.append(full_path)
                if verbose or dry_run:
                    print(f"{'[DRY RUN] ' if dry_run else ''}Matched: {full_path}")
                if not dry_run:
                    try:
                        os.remove(full_path)
                        deleted += 1
                    except Exception as e:
                        typer.echo(f"Error deleting {full_path}: {e}", err=True)

    typer.echo(f"\nTotal matched files: {len(matched_files)}")
    if not dry_run:
        typer.echo(f"Total deleted: {deleted}")
