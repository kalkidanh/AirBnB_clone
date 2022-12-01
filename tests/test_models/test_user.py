#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

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

    def test_is_instantiation(self):
        """Tests instantiation of User class."""

        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        user = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(user, k))
            self.assertEqual(type(getattr(user, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_user_class(self):
        """Test to check user class documentation
        """
        self.assertTrue(len(User.__doc__) > 0)

    def test_doc_user_methods(self):
        """Test to check user's methods documentation
        """
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
