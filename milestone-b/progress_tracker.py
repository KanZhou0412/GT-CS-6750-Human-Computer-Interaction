#!/usr/bin/env python3
"""Milestone B checklist progress tracker.

Reads a markdown checklist file and prints:
- overall progress
- per-section progress
- open tasks (optional)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SECTION_PATTERN = re.compile(r"^\s*##\s+(?P<title>.+?)\s*$")
TASK_PATTERN = re.compile(r"^\s*-\s*\[(?P<state>[ xX])\]\s+(?P<text>.+?)\s*$")


def _init_section() -> dict[str, object]:
    return {"total": 0, "done": 0, "open": []}


def parse_checklist(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"Checklist file not found: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()
    current_section = "Uncategorized"
    sections: dict[str, dict[str, object]] = {current_section: _init_section()}

    total = 0
    done = 0

    for line in lines:
        section_match = SECTION_PATTERN.match(line)
        if section_match:
            current_section = section_match.group("title").strip()
            sections.setdefault(current_section, _init_section())
            continue

        task_match = TASK_PATTERN.match(line)
        if not task_match:
            continue

        state = task_match.group("state").lower()
        text = task_match.group("text").strip()

        total += 1
        sections[current_section]["total"] = int(sections[current_section]["total"]) + 1

        if state == "x":
            done += 1
            sections[current_section]["done"] = int(sections[current_section]["done"]) + 1
        else:
            section_open = sections[current_section]["open"]
            assert isinstance(section_open, list)
            section_open.append(text)

    if total == 0:
        percent = 0.0
    else:
        percent = round((done / total) * 100, 1)

    return {
        "file": str(path),
        "total": total,
        "done": done,
        "open": total - done,
        "percent": percent,
        "sections": sections,
    }


def print_human(summary: dict[str, object], show_open: bool) -> None:
    total = int(summary["total"])
    done = int(summary["done"])
    percent = float(summary["percent"])
    sections = summary["sections"]
    assert isinstance(sections, dict)

    print(f"Checklist: {summary['file']}")
    print(f"Overall: {done}/{total} done ({percent}%)")
    print("")
    print("Section breakdown:")

    for section, details in sections.items():
        assert isinstance(details, dict)
        section_total = int(details["total"])
        section_done = int(details["done"])
        if section_total == 0:
            section_percent = 0.0
        else:
            section_percent = round((section_done / section_total) * 100, 1)
        print(f"- {section}: {section_done}/{section_total} ({section_percent}%)")

    if not show_open:
        return

    print("")
    print("Open tasks:")
    any_open = False
    for section, details in sections.items():
        assert isinstance(details, dict)
        open_items = details["open"]
        assert isinstance(open_items, list)
        if not open_items:
            continue
        any_open = True
        print(f"  [{section}]")
        for item in open_items:
            print(f"  - {item}")
    if not any_open:
        print("  None")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Track completion progress for a markdown checklist."
    )
    parser.add_argument(
        "checklist_path",
        nargs="?",
        default="milestone-b/checklist.md",
        help="Path to checklist markdown file (default: milestone-b/checklist.md)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print summary as JSON",
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Hide open task list in human-readable output",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checklist_path = Path(args.checklist_path)

    try:
        summary = parse_checklist(checklist_path)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print_human(summary, show_open=not args.no_open)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
