#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

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
        """Tests instantiation of City class."""

        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        city = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(city, k))
            self.assertEqual(type(getattr(city, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_city_class(self):
        """Test to check city class documentation
        """
        self.assertTrue(len(City.__doc__) > 0)

    def test_doc_city_methods(self):
        """Test to check city's methods documentation
        """
        for method in dir(City):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
