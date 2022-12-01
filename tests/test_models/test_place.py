#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

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

    def test_is_instance(self):
        """Tests instantiation of Place class."""

        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        place = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(place, k))
            self.assertEqual(type(getattr(place, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_place_class(self):
        """Test to check place class documentation
        """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_doc_place_methods(self):
        """Test to check place's methods documentation
        """
        for method in dir(Place):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
