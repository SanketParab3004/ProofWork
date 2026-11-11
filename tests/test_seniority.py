"""Tests for YOUR task: proofwork.parser.detect_seniority.

All postings here are synthetic (made up). Run: uv run pytest tests/test_seniority.py
"""

import pytest

from proofwork.parser import Seniority, detect_seniority


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Data Analyst Intern - summer 2027", Seniority.INTERN),
        ("Junior Data Analyst. 0-2 years of experience.", Seniority.JUNIOR),
        ("Entry-level analyst, recent graduates welcome", Seniority.JUNIOR),
        ("Senior Data Engineer, 5+ years building pipelines", Seniority.SENIOR),
        ("Lead Data Engineer to guide a team of four", Seniority.LEAD),
        ("Data Analyst. 3 years of SQL experience.", Seniority.MID),
        ("Data Analyst at a growing startup", Seniority.MID),  # no clues -> mid
    ],
)
def test_detect_seniority(text, expected):
    assert detect_seniority(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Data Analyst for our international team", Seniority.MID),
        ("Data Engineer working on internal tools", Seniority.MID),
        ("Data Engineer, leading tools in the market", Seniority.MID),
        ("Data Engineer Internship program", Seniority.INTERN),
        ("Tech Lead, Data Platform", Seniority.LEAD),
    ],
)
def test_whole_words_only(text, expected):
    assert detect_seniority(text) == expected


def test_case_does_not_matter():
    assert detect_seniority("SENIOR DATA ANALYST") == Seniority.SENIOR
