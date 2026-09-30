#!/usr/bin/env python3
"""Validate a Real Feedback Lab Markdown experiment record."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "【实验身份】",
    "【原始假设】",
    "【真实行为】",
    "【真实反馈】",
    "【能力诊断】",
    "【证伪】",
    "【最小干预】",
    "【下一实验】",
    "【可迁移经验】",
    "【证据边界】",
]

ALLOWED = {
    "phase": {"baseline", "diagnosis", "intervention", "validation", "capture"},
    "baseline_status": {"clean-baseline", "partial-baseline", "practice-only"},
    "next_experiment_type": {"delayed-retrieval", "near-transfer", "far-transfer", "none"},
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def as_int(meta: dict[str, str], key: str, errors: list[str]) -> int | None:
    raw = meta.get(key)
    if raw is None:
        errors.append(f"missing metadata: {key}")
        return None
    try:
        return int(raw)
    except ValueError:
        errors.append(f"{key} must be an integer, got {raw!r}")
        return None


def validate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    errors: list[str] = []
    warnings: list[str] = []

    for key in (
        "experiment_id",
        "phase",
        "baseline_status",
        "evidence_frozen",
        "answer_authority",
        "primary_bottleneck_count",
        "intervention_count",
        "next_experiment_type",
    ):
        if key not in meta:
            errors.append(f"missing metadata: {key}")

    for key, values in ALLOWED.items():
        if key in meta and meta[key] not in values:
            errors.append(f"invalid {key}: {meta[key]!r}; expected one of {sorted(values)}")

    frozen = meta.get("evidence_frozen", "").lower()
    if meta.get("phase") in {"diagnosis", "intervention", "validation", "capture"} and frozen != "true":
        errors.append("evidence_frozen must be true after baseline phase")

    bottlenecks = as_int(meta, "primary_bottleneck_count", errors)
    interventions = as_int(meta, "intervention_count", errors)
    if bottlenecks is not None and not 1 <= bottlenecks <= 3:
        errors.append("primary_bottleneck_count must be between 1 and 3")
    if interventions is not None and not 1 <= interventions <= 2:
        errors.append("intervention_count must be between 1 and 2")

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^#+\s*{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
            errors.append(f"missing heading: {heading}")

    if not any(label in text for label in ("OBSERVED", "REPORTED", "INFERRED", "UNVERIFIED")):
        warnings.append("no explicit evidence-level labels found")

    next_section = re.search(
        r"^#+\s*【下一实验】\s*$([\s\S]*?)(?=^#+\s*【|\Z)", text, flags=re.MULTILINE
    )
    if next_section:
        body = next_section.group(1)
        for term in ("假设", "材料", "指标", "支持", "证伪"):
            if term not in body:
                warnings.append(f"next experiment may be underspecified: missing {term}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()

    if not args.record.is_file():
        print(f"ERROR: record not found: {args.record}", file=sys.stderr)
        return 2

    errors, warnings = validate(args.record)
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
