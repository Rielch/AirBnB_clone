#!/usr/bin/python3
"""Unittest for the Review class"""
from models import review
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test for the review module"""

    def test_documentation(self):
        """Test for documentation in the module and the class"""
        self.assertTrue(len(review.__doc__) > 1)
        self.assertTrue(len(Review.__doc__) > 1)


if __name__ == "__main__":
    """Executes the test cases"""
    unittest.main()
