"""Unit tests for main module."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import get_greeting


def test_get_greeting_world():
    """Test greeting with World."""
    assert get_greeting("World") == "Hello, World!"


def test_get_greeting_python():
    """Test greeting with Python."""
    assert get_greeting("Python") == "Hello, Python!"


if __name__ == "__main__":
    test_get_greeting_world()
    test_get_greeting_python()
    print("All tests passed!")
