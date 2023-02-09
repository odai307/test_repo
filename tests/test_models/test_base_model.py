#!/usr/bin/python3

"""Model for testing the BaseModel class
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """For testing most/all possible scenarios"""

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(BaseModel.__doc__), 0)

    def test_init_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def test_initialization(self):
        """testing for the object initialization"""
        self.assertEqual(print(BaseModel), None)

    def test_str_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(BaseModel.__doc__), 0)
