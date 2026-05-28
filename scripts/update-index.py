#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "INDEX.md"
START = "<!-- AUTO_INDEX_START -->"
END = "<!-- AUTO_INDEX_END -->"
EXCLUDED_DIRS = {".git"}
EXCLUDED_FILES = {"README.md", "INDEX.md"}


def title_for(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def group_for(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return "root" if len(rel.parts) == 1 else rel.parts[0]


def build_index() -> str:
    files = []
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in EXCLUDED_FILES and len(rel_parts) == 1:
            continue
        files.append(path)

    groups = {}
    for path in sorted(files, key=lambda p: p.relative_to(ROOT).as_posix()):
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


def main() -> None:
    current = INDEX.read_text(encoding="utf-8")
    before, rest = current.split(START, 1)
    _, after = rest.split(END, 1)
    updated = f"{before}{START}\n\n{build_index()}\n{END}{after}"
    INDEX.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
