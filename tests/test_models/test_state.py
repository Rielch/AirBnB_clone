#!/usr/bin/python3
"""Unittest for the State class"""
from models import state
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_documentation(self):
        """Test for documentation in module and class"""
        self.assertTrue(len(state.__doc__) > 1)
        self.assertTrue(len(State.__doc__) > 1)


if __name__ == "__name__":
    """Executes the test cases"""
    unittest.main()
