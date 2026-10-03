#!/usr/bin/env python3
"""Validate a CET4 Reading Section A Real Feedback record."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "【题型合规检查】",
    "【实验身份】",
    "【原始假设】",
    "【真实行为】",
    "【真实反馈】",
    "【答案拓扑】",
    "【能力诊断】",
    "【证伪】",
    "【最小干预】",
    "【下一实验】",
    "【可迁移经验】",
    "【证据边界】",
]

ALLOWED = {
    "scope_mode": {"isolated-section-a", "full-reading-block"},
    "phase": {"baseline", "diagnosis", "intervention", "validation", "capture"},
    "baseline_status": {"clean-baseline", "partial-baseline", "practice-only"},
    "answer_authority": {
        "official",
        "publisher",
        "teacher",
        "third-party",
        "agent-inferred",
        "disputed",
    },
    "next_experiment_type": {"delayed-retrieval", "near-transfer", "none"},
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


def require_int(meta: dict[str, str], key: str, errors: list[str]) -> int | None:
    value = meta.get(key)
    if value is None:
        errors.append(f"missing metadata: {key}")
        return None
    try:
        return int(value)
    except ValueError:
        errors.append(f"{key} must be an integer, got {value!r}")
        return None


def validate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    errors: list[str] = []
    warnings: list[str] = []

    required = (
        "experiment_id",
        "task_type",
        "format_match",
        "scope_mode",
        "item_range",
        "blank_count",
        "option_count",
        "single_use",
        "phase",
        "baseline_status",
        "evidence_frozen",
        "answer_authority",
        "raw_score",
        "primary_bottleneck_count",
        "intervention_count",
        "next_experiment_type",
    )
    for key in required:
        if key not in meta:
            errors.append(f"missing metadata: {key}")

    if meta.get("task_type") != "cet4-word-bank-cloze":
        errors.append("task_type must be 'cet4-word-bank-cloze'")
    if meta.get("format_match", "").lower() != "true":
        errors.append("format_match must be true; otherwise stop and handle FORMAT_DRIFT")
    if meta.get("single_use", "").lower() != "true":
        errors.append("single_use must be true for the current CET4 Section A format")

    for key, values in ALLOWED.items():
        if key in meta and meta[key] not in values:
            errors.append(f"invalid {key}: {meta[key]!r}; expected one of {sorted(values)}")

    blank_count = require_int(meta, "blank_count", errors)
    option_count = require_int(meta, "option_count", errors)
    raw_score = require_int(meta, "raw_score", errors)
    bottlenecks = require_int(meta, "primary_bottleneck_count", errors)
    interventions = require_int(meta, "intervention_count", errors)

    if blank_count is not None and blank_count != 10:
        errors.append("blank_count must be 10 under the current official format")
    if option_count is not None and option_count != 15:
        errors.append("option_count must be 15 under the current official format")
    if raw_score is not None and not 0 <= raw_score <= 10:
        errors.append("raw_score must be between 0 and 10")
    if bottlenecks is not None and not 1 <= bottlenecks <= 3:
        errors.append("primary_bottleneck_count must be between 1 and 3")
    if interventions is not None and not 1 <= interventions <= 2:
        errors.append("intervention_count must be between 1 and 2")

    if meta.get("item_range") != "26-35":
        warnings.append("item_range differs from the current recurring 26-35 pattern; check FORMAT_DRIFT")

    frozen = meta.get("evidence_frozen", "").lower()
    if meta.get("phase") in {"diagnosis", "intervention", "validation", "capture"} and frozen != "true":
        errors.append("evidence_frozen must be true after baseline phase")

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^#+\s*{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
            errors.append(f"missing heading: {heading}")

    if not any(label in text for label in ("OBSERVED", "REPORTED", "INFERRED", "UNVERIFIED")):
        warnings.append("no explicit evidence-level labels found")

    if re.search(r"每题\s*(7\.1|3\.55)|固定.{0,8}(710|报道分)", text):
        warnings.append("possible unsupported fixed conversion to CET reported score")

    if meta.get("scope_mode") == "isolated-section-a" and re.search(r"官方.{0,8}(限时|时间).{0,8}Section A", text, re.I):
        warnings.append("the official specification gives 40 minutes to the full reading component, not Section A alone")

    next_section = re.search(
        r"^#+\s*【下一实验】\s*$([\s\S]*?)(?=^#+\s*【|\Z)", text, flags=re.MULTILINE
    )
    if next_section:
        body = next_section.group(1)
        for term in ("假设", "材料", "执行", "指标", "支持", "证伪"):
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
