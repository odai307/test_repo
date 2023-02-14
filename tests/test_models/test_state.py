#!/usr/bin/python3

"""
Model testing functionality and features of the state model
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Testing functionalities and features
    of the state class/object
    """
    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(State.__doc__), 0)
