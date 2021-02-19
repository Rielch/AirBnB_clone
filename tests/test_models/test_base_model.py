#!/usr/bin/python3
"""Unittest to test the BaseModel class"""
from models.base_model import BaseModel
from models import base_model
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """Class with tests for BaseModel class"""


    def test_documentation(self):
        """Test for documentation in the module, class and methods"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(base_model.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes of the BaseModel class"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        #Test id
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertIsInstance(instance1.id, str)
        #Test created_at
        self.assertIsInstance(instance1.created_at, datetime.datetime)
        #Test updated_at
        self.assertIsInstance(instance1.updated_at, datetime.datetime)

    def test___init__(self):
        """Test the __init__ method"""
        inst_dict = {"updated_at": "2021-02-19T03:57:16.114023",
                     "__class__": "BaseModel",
                     "id": "39690735-03ae-41ff-a42d-88e08510a07c",
                     "created_at": "2021-02-19T03:57:16.113987"}
        instance1 = BaseModel(**inst_dict)
        self.assertEqual(instance1.id, "39690735-03ae-41ff-a42d-88e08510a07c")

    def test_save(self):
        """Test the save method"""
        instance1 = BaseModel()
        update1 = instance1.updated_at
        instance1.save()
        update2 = instance1.updated_at
        self.assertNotEqual(update1, update2)

    def test_to_dict(self):
        """Test the to_dict method"""
        instance1 = BaseModel()
        inst_dict = instance1.to_dict()
        self.assertIsInstance(inst_dict, dict)

    def test___str__(self):
        """Test the __str__ method"""
        instance1 = BaseModel()
        inst_str = instance1.__str__()
        self.assertIsInstance(inst_str, str)


if __name__ == "__main__":
    """Executes test cases"""
    unittest.main()
