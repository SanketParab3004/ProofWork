import pytest
from pydantic import ValidationError

from proofwork.parser import JobProfile, RoleFamily, Seniority


def make(**overrides):
    data = {
        "title": "Junior Data Analyst",
        "role_family": "data_analyst",
        "seniority": "junior",
    }
    data.update(overrides)
    return JobProfile(**data)


def test_valid_profile_from_plain_strings():
    profile = make()
    assert profile.role_family is RoleFamily.DATA_ANALYST
    assert profile.seniority is Seniority.JUNIOR
    assert profile.tools == []


def test_tools_are_cleaned_and_deduplicated():
    profile = make(tools=[" SQL", "Python", "sql", "", "Tableau "])
    assert profile.tools == ["sql", "python", "tableau"]


def test_unknown_seniority_is_rejected():
    with pytest.raises(ValidationError):
        make(seniority="wizard")


def test_empty_title_is_rejected():
    with pytest.raises(ValidationError):
        make(title="")


def test_round_trip_json():
    profile = make(tools=["sql"], domain="e-commerce")
    again = JobProfile.model_validate_json(profile.model_dump_json())
    assert again == profile
