#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of State class."""

        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        state = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(state, k))
            self.assertEqual(type(getattr(state, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_state_class(self):
        """Test to check state class documentation
        """
        self.assertTrue(len(State.__doc__) > 0)

    def test_doc_state_methods(self):
        """Test to check state's methods documentation
        """
        for method in dir(State):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
