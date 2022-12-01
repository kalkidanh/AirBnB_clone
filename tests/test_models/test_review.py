#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

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
        """Tests instantiation of Review class."""

        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        review = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(review, k))
            self.assertEqual(type(getattr(review, k, None)), v)

    def test_pep8(self):
        """Testing python code style"""
        py_code_style = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = py_code_style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "errors found.")

    def test_doc_review_class(self):
        """Test to check review class documentation
        """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_doc_review_methods(self):
        """Test to check review's methods documentation
        """
        for method in dir(Review):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
