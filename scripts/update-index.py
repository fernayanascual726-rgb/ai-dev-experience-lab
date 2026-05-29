#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "INDEX.md"
README = ROOT / "README.md"
START = "<!-- AUTO_INDEX_START -->"
END = "<!-- AUTO_INDEX_END -->"
RECENT_START = "<!-- RECENT_UPDATES_START -->"
RECENT_END = "<!-- RECENT_UPDATES_END -->"
EXCLUDED_DIRS = {".git"}
EXCLUDED_FILES = {"README.md", "INDEX.md"}
RECENT_LIMIT = 8


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def frontmatter(path: Path) -> dict[str, object]:
    lines = read_lines(path)
    if not lines or lines[0] != "---":
        return {}

    data: dict[str, object] = {}
    key = ""
    values: list[str] = []
    for line in lines[1:]:
        if line == "---":
            if key and values:
                data[key] = values
            return data
        if line.startswith("  - ") and key:
            values.append(line[4:].strip().strip('"'))
            continue
        if ":" in line:
            if key and values:
                data[key] = values
            key, raw = line.split(":", 1)
            key = key.strip()
            raw = raw.strip().strip('"')
            values = []
            if raw:
                data[key] = raw
                key = ""
    return data


def title_for(path: Path) -> str:
    meta = frontmatter(path)
    if isinstance(meta.get("title"), str):
        title = str(meta["title"])
        if "{{" not in title:
            return title
    if path.name != "README.md" and group_for(path) == "templates":
        return path.stem.replace("-", " ").title()
    for line in read_lines(path):
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def date_for(path: Path) -> str:
    meta = frontmatter(path)
    if isinstance(meta.get("date"), str):
        date = str(meta["date"])
        return "" if date == "YYYY-MM-DD" or "{{" in date else date
    return ""


def tags_for(path: Path) -> list[str]:
    meta = frontmatter(path)
    tags = meta.get("tags")
    return tags if isinstance(tags, list) else []


def summary_for(path: Path) -> str:
    meta = frontmatter(path)
    if isinstance(meta.get("summary"), str):
        return str(meta["summary"])
    return ""


def group_for(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return "root" if len(rel.parts) == 1 else rel.parts[0]


def markdown_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in EXCLUDED_FILES and len(rel_parts) == 1:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def build_index(files: list[Path]) -> str:
    groups: dict[str, list[Path]] = {}
    for path in files:
        groups.setdefault(group_for(path), []).append(path)

    sections = []
    for group in sorted(groups):
        sections.append(f"## {group}")
        sections.append("")
        for path in groups[group]:
            rel = path.relative_to(ROOT).as_posix()
            sections.append(f"- [{title_for(path)}]({rel})")
        sections.append("")
    return "\n".join(sections).rstrip() + "\n"


def build_recent_updates(files: list[Path]) -> str:
    candidates = [
        path
        for path in files
        if path.name != "content-guidelines.md" and date_for(path)
    ]
    candidates.sort(key=lambda path: (date_for(path), path.relative_to(ROOT).as_posix()), reverse=True)

    lines = []
    for path in candidates[:RECENT_LIMIT]:
        rel = path.relative_to(ROOT).as_posix()
        title = title_for(path)
        date = date_for(path)
        tags = tags_for(path)
        summary = summary_for(path)
        note = " / ".join(tags[:2]) if tags else summary
        suffix = f" — {note}" if note else ""
        lines.append(f"- {date} — [{title}]({rel}){suffix}")
    return "\n".join(lines) + "\n"


def replace_block(path: Path, start: str, end: str, content: str) -> None:
    current = path.read_text(encoding="utf-8")
    before, rest = current.split(start, 1)
    _, after = rest.split(end, 1)
    updated = f"{before}{start}\n\n{content}\n{end}{after}"
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    files = markdown_files()
    replace_block(INDEX, START, END, build_index(files))
    replace_block(README, RECENT_START, RECENT_END, build_recent_updates(files))


if __name__ == "__main__":
    main()
