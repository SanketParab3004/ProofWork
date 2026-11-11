"""Smoke test: proves the package installs and pytest runs."""

import proofwork


def test_package_has_version():
    assert proofwork.__version__ == "0.1.0"
