#!/usr/bin/env python3
"""Validate repository navigation, plan coverage, and attribution (stdlib only).

Supports inline Markdown links/images and ATX headings used in this repository.
Does not fetch external URLs or verify the technical truth of study material.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def prose(text: str) -> str:
    """Exclude fenced examples so sample links/headings do not affect checks."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence is None:
            if match:
                fence = match.group(1)
            else:
                lines.append(line)
        elif match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence):
            fence = None
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    found: set[str] = set()
    for title in HEADING.findall(prose(text)):
        title = re.sub(r"!?(\[([^]]*)\])\([^)]*\)", r"\2", title)
        title = re.sub(r"<[^>]*>", "", title)
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in found:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        found.add(candidate)
    return found


def check_links(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    errors = []
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.relative_to(root).parts:
            continue
        for raw in LINK.findall(prose(source.read_text(encoding="utf-8"))):
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            label = str(source.relative_to(root))
            if not destination.is_relative_to(root):
                errors.append(f"{label}: link escapes repository: {target}")
            elif not destination.is_file():
                errors.append(f"{label}: missing link target: {target}")
            elif parsed.fragment and destination.suffix == ".md":
                fragment = unquote(parsed.fragment)
                if fragment not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{label}: missing heading anchor: {target}")
    return errors


def check_plan(root: Path = ROOT) -> list[str]:
    plan = root / "learning-paths/4-week-plan.md"
    if not plan.is_file():
        return ["Missing four-week plan"]
    targets = {urlsplit(link.strip("<>")).path for link in LINK.findall(prose(plan.read_text(encoding="utf-8")))}
    guides = sorted((root / "topic-guides").glob("[0-9][0-9]-*.md"))
    return [
        f"Study plan omits topic guide: {guide.name}"
        for guide in guides
        if not guide.name.startswith("00-") and f"../topic-guides/{guide.name}" not in targets
    ]


def check_attribution(root: Path = ROOT) -> list[str]:
    readme = (root / "README.md").read_text(encoding="utf-8")
    required = ("RonitSachdev", "https://github.com/RonitSachdev/aws-saa-c03-guides", "CC BY 4.0")
    return [f"README.md: missing attribution: {item}" for item in required if item not in readme]


def main() -> int:
    errors = check_links() + check_plan() + check_attribution()
    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository checks passed: link targets, heading anchors, plan coverage, attribution.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

