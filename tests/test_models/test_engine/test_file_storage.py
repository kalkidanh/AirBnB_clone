#!/usr/bin/python3

"""Define unit test for file storage class
"""

import os
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import pep8


class TestFileStorageClass(unittest.TestCase):
    """Representation of a set of tests for file storage class
    """

    def setUp(self):
        """set up the test
        """
        pass

    def test_pep8(self):
        """Test to check pycodestyle
        """
        py_code_style = pep8.StyleGuide(quiet=True)
        check = py_code_style.check_files(
            ['models/engine/file_storage.py', 'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(check.total_errors, 0, "Errors found")

    def test_is_instance(self):
        """Test to check that the storage is instance
        """
        self.assertTrue(isinstance(storage, FileStorage))

    def test_all(self):
        """Test to check the type of method all from file storage
        """
        file_stor = FileStorage()
        self.assertTrue(type(file_stor.all()) == str)

    def test_new(self):
        """Test to check the new method
        """
        file_stor = FileStorage()
        model = BaseModel()
        file_stor.new(model)
        dict1 = file_stor.all()
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertTrue(key in dict1)

    def test_reload(self):
        """Test to check reload method
        """
        file_stor = FileStorage()
        model = BaseModel()
        file_stor.new(model)
        file_stor.save()
        dict1 = file_stor.all()
        os.remove("test.json")
        file_stor.reload()
        dict2 = file_stor.all()
        self.assertEqual(dict1 == dict2)

    def test_save(self):
        """Test to check save method
        """
        file_stor = FileStorage()
        model = BaseModel()
        file_stor.new(model)
        dict1 = file_stor.all()
        file_stor.save()
        file_stor.reload()
        dict2 = file_stor.all()
        for key in dict1:
            key_1 = key
        for key in dict2:
            key_2 = key
        self.assertEqual(dict1[key_1].to_dict(), dict2[key_2].to_dict())


if __name__ == '__main__':
    unittest.main()
