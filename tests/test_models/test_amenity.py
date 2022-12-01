#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

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
        """Tests instantiation of Amenity class."""

        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        amenity = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(amenity, k))
            self.assertEqual(type(getattr(amenity, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_amenity_class(self):
        """Test to check amenity class documentation
        """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_doc_amenity_methods(self):
        """Test to check amenity's methods documentation
        """
        for method in dir(Amenity):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
