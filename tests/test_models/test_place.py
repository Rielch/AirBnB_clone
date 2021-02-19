#!/usr/bin/python3
"""Unittest for Place class"""
from models.place import Place
from models import place
import unittest


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_documentation(self):
        """Test the documentation of the module and the class"""
        self.assertTrue(len(place.__doc__) > 1)
        self.assertTrue(len(Place.__doc__) > 1)


if __name__ == "__main__":
    """Executes the test cases"""
    unittest.main()
