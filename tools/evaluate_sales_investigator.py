#!/usr/bin/env python3
"""Deterministic rubric for the sales-investigator autoresearch run."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


PROTECTED_SECTIONS = [
    "Core Behavior",
    "Investigation Process",
    "Real Estate Segmentation",
    "Legal and Transaction Risk Screening",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (.+?)\s*$", text, flags=re.MULTILINE))
    out: dict[str, str] = {}
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        out[match.group(1)] = text[start:end].strip()
    return out


def main_branch_text(path: Path) -> str:
    rel = path.as_posix()
    return subprocess.check_output(
        ["git", "show", f"main:{rel}"],
        cwd=Path.cwd(),
        text=True,
        stderr=subprocess.DEVNULL,
    )


def contains_all(text: str, phrases: list[str]) -> int:
    lower = text.lower()
    return sum(1 for phrase in phrases if phrase.lower() in lower)


def regex_count(text: str, patterns: list[str]) -> int:
    return sum(1 for pattern in patterns if re.search(pattern, text, flags=re.I | re.M))


def score_skill(text: str) -> tuple[int, dict[str, int], list[str]]:
    lower = text.lower()
    found_sections = sections(text)
    breakdown: dict[str, int] = {}
    notes: list[str] = []

    variant_phrases = [
        "hard requirement",
        "deal-breaker",
        "must be rejected",
        "best-fit",
        "fit score",
        "weighted fit",
        "penalty",
        "rank",
        "tie-breaker",
        "missing evidence",
        "source date",
        "stale listing",
        "comparable",
        "walk-away",
        "threshold",
        "requirement coverage",
    ]
    variant_patterns = [
        r"0\s*[-/]\s*100",
        r"weights?\s+sum\s+to\s+100",
        r"reject(?:ion)?\s+reason",
        r"scorecard|scoring table|ranked shortlist",
    ]
    variant_score = min(20, contains_all(text, variant_phrases) + regex_count(text, variant_patterns))
    breakdown["variant_fit"] = variant_score
    if variant_score < 16:
        notes.append("variant ranking is not explicit enough")

    formula_phrases = [
        "expected value",
        "probability-weighted",
        "real price growth",
        "nominal price growth",
        "inflation",
        "rent yield",
        "net rent",
        "transaction cost",
        "maintenance",
        "reserve",
        "mortgage payment",
        "interest cost",
        "opportunity cost",
        "downside case",
        "upside case",
        "base case",
        "sensitivity",
        "confidence interval",
        "error band",
        "break-even",
        "liquidity",
    ]
    formula_patterns = [
        r"EV|expected_value",
        r"MAE|MAPE|RMSE",
        r"p_base|p_downside|p_upside|probabilit",
        r"monthly_payment|annuity|loan",
        r"future_value|FV|discount",
    ]
    formula_score = min(25, contains_all(text, formula_phrases) + regex_count(text, formula_patterns))
    breakdown["forecast_formula"] = formula_score
    if formula_score < 20:
        notes.append("forecast formula lacks economic calibration details")

    backtest_phrases = [
        "backtest",
        "historical",
        "past",
        "actual",
        "compare",
        "calibrate",
        "forecast horizon",
        "publication date",
        "realized price",
        "prediction error",
        "do not tune",
        "out-of-sample",
        "forecast",
        "error",
        "precision",
    ]
    backtest_patterns = [
        r"MAE|MAPE|RMSE",
        r"predicted.*actual|actual.*predicted",
        r"\d+\s*[-/]\s*\d+\s*months?",
        r"holdout|out[- ]of[- ]sample",
    ]
    backtest_score = min(20, contains_all(text, backtest_phrases) + regex_count(text, backtest_patterns))
    breakdown["backtesting"] = backtest_score
    if backtest_score < 16:
        notes.append("historical formula validation is under-specified")

    overview_phrases = [
        "current market overview",
        "current snapshot",
        "inventory",
        "active listings",
        "price band",
        "median",
        "interquartile",
        "days on market",
        "liquidity",
        "rental",
        "mortgage",
        "central bank",
        "exchange rate",
        "construction",
        "supply",
        "demand",
        "source recency",
        "as of",
        "confidence",
        "data freshness",
    ]
    overview_score = min(15, contains_all(text, overview_phrases))
    breakdown["current_overview"] = overview_score
    if overview_score < 12:
        notes.append("current-market overview requirements are incomplete")

    output_phrases = [
        "ranked shortlist",
        "best-fit variants",
        "prediction audit",
        "backtest",
        "current market",
        "trigger thresholds",
        "recommendation",
        "confidence",
        "source",
        "date",
    ]
    output_score = min(10, contains_all(found_sections.get("Output Style", ""), output_phrases))
    breakdown["output_style"] = output_score

    completion_phrases = [
        "best-fit",
        "ranked",
        "backtest",
        "historical actual",
        "current market overview",
        "precision",
        "formula",
        "threshold",
        "recommendation",
        "confidence",
    ]
    completion_score = min(10, contains_all(found_sections.get("Completion Criteria", ""), completion_phrases))
    breakdown["completion_criteria"] = completion_score

    total = sum(breakdown.values())
    if len(text.split()) > 2200:
        total -= 3
        notes.append("skill is becoming too long")
    if "legal conclusion" not in lower and "professional legal verification" not in lower:
        total -= 10
        notes.append("legal caution appears weakened")

    return max(0, total), breakdown, notes


def protected_unchanged(path: Path) -> tuple[bool, list[str]]:
    current = sections(read_text(path))
    base = sections(main_branch_text(path))
    changed = [name for name in PROTECTED_SECTIONS if current.get(name) != base.get(name)]
    return not changed, changed


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: evaluate_sales_investigator.py <skill-path>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = read_text(path)
    ok, changed = protected_unchanged(path)
    score, breakdown, notes = score_skill(text)
    status = "pass" if ok else "fail"
    if not ok:
        score = 0
        notes.append("protected sections changed: " + ", ".join(changed))

    print("---")
    print(f"target_metric:       {score}")
    print("comparison_rule:     higher_is_better")
    print(f"status:              {status}")
    print(
        "score_breakdown:     "
        + ";".join(f"{name}={value}" for name, value in breakdown.items())
    )
    print("notes:               " + ("; ".join(notes) if notes else "none"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
