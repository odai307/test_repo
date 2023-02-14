#!/usr/bin/python3

"""
Model for testing the user model
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class for testing user object"""

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(User.__doc__), 0)
