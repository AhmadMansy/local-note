"""
Basic tests to ensure CI passes
اختبارات أساسية لضمان مرور CI
"""

import pytest


def test_import():
    """Test that we can import the package"""
    from local_note import __version__
    assert __version__ is not None
    assert isinstance(__version__, str)


def test_version_format():
    """Test that version follows semantic versioning"""
    from local_note import __version__
    parts = __version__.split(".")
    assert len(parts) >= 2
    assert all(part.isdigit() for part in parts)
