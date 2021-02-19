#!/usr/bin/python3
"""Unittest for Amenity class"""
from models.amenity import Amenity
from models import amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Class to thest the class Amenity"""

    def test_documentation(self):
        """Test for documentation in the module and the class"""
        self.assertTrue(len(amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes"""
        instance = Amenity()
        self.assertIsInstance(instance.id, str)


if __name__ == "__main__":
    """Executes the test"""
    unittest.main()
