"""Job posting parser: the data shape (JobProfile) and simple rule-based helpers.

No AI provider here. In skill mode, Claude/Codex reads the posting and fills a
JobProfile as JSON; this module validates and cleans it. The rule-based helpers
give a free, testable baseline and a cross-check for the AI's answer.
"""
import re
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class RoleFamily(str, Enum):
    DATA_ANALYST = "data_analyst"
    DATA_ENGINEER = "data_engineer"
    OTHER = "other"


class Seniority(str, Enum):
    INTERN = "intern"
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"
    LEAD = "lead"


class JobProfile(BaseModel):
    """What ProofWork needs to know about a job to build a simulation."""

    title: str = Field(min_length=1)
    role_family: RoleFamily
    seniority: Seniority
    skills: list[str] = Field(default_factory=list)  # e.g. "data cleaning", "a/b testing"
    tools: list[str] = Field(default_factory=list)  # e.g. "sql", "python", "tableau"
    responsibilities: list[str] = Field(default_factory=list)
    domain: str | None = None  # industry, e.g. "e-commerce"

    @field_validator("skills", "tools")
    @classmethod
    def clean_list(cls, items: list[str]) -> list[str]:
        """Lowercase, trim, drop blanks and duplicates, keep original order."""
        seen: list[str] = []
        for item in items:
            item = item.strip().lower()
            if item and item not in seen:
                seen.append(item)
        return seen


def detect_seniority(text: str) -> Seniority:
    """Guess seniority from a job posting's text, using simple rules.
    """
    text = text.lower()
    
    if "intern" in text:
        return Seniority.INTERN
    if "lead" in text:
        return Seniority.LEAD
    if "senior" in text:
        return Seniority.SENIOR
    if "junior" in text or "entry-level" in text:
        return Seniority.JUNIOR

    match = re.search(r"(\d+)\+?\s*years", text)
    if match:
        years = int(match.group(1))
        if years <= 2:
            return Seniority.JUNIOR
        if years >= 5:
            return Seniority.SENIOR
    
    return Seniority.MID