#!/usr/bin/python3

"""Define unit test for base model class
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel
import pep8


class TestBaseClass(unittest.TestCase):
    """Representation of a set of tests for base model class
    """

    def setUp(self):
        """set up the test
        """
        pass

    def test_type_of_id(self):
        """Test to check the type of id
        """
        model = BaseModel()
        self.assertTrue(type(model.id) == str)

    def test_type_of_datetime(self):
        """Test to check the type of created_at and updated_at
        """
        model = BaseModel()
        self.assertTrue(type(model.created_at) == datetime)
        self.assertTrue(type(model.updated_at) == datetime)

    def test_str(self):
        """Test to check the __str__ method
        """
        model = BaseModel()
        self.assertEqual(model.__str__(), "[" + model.__class__.__name__ + "]"
                         " (" + model.id + ") " + str(model.__dict__))

    def test_uuid_generation(self):
        """Test to check the generation of uuid
        """
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()
        self.assertNotTrue(model1.id == model2.id)
        self.assertNotTrue(model2.id == model3.id)
        self.assertNotTrue(model3.id == model1.id)

    def test_to_dict(self):
        """Test to check to_dict method
        """
        model = BaseModel()
        my_model = model.to_dict()
        self.assertTrue(type(my_model["created_at"] == str))
        self.assertTrue(type(my_model["updated_at"] == str))
        self.assertTrue(type(model.created_at) == datetime)
        self.assertTrue(type(model.updated_at) == datetime)
        self.assertEqual(my_model["created_at"], model.created_at.isoformat())
        self.assertEqual(my_model["updated_at"], model.updated_at.isoformat())

    def test_none_dict(self):
        """Test to check for None dict
        """
        model = BaseModel(None)
        self.assertTrue(type(model.id) == str)
        self.assertTrue(type(model.created_at) == datetime)
        self.assertTrue(type(model.updated_at) == datetime)

    def test_kwargs_with_dict(self):
        """Test to check when kwargs not empty
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model_json, my_new_model.to_dict())
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_kwargs_with_emp_dict(self):
        """Test to check when kwargs is empty
        """
        my_dict = {}
        my_model = BaseModel(**my_dict)
        self.assertTrue(type(my_model.id) == str)
        self.assertTrue(type(my_model.created_at) == datetime)
        self.assertTrue(type(my_model.updated_at) == datetime)

    def test_pep8(self):
        """Test to check python code style
        """
        py_code_style = pep8.StyleGuide(quiet=True)
        check = py_code_style.check_files(
            ['models/base_model.py', 'tests/test_models/test_base_model.py'])
        self.assertEqual(check.total_errors, 0, "errors found.")

    def test_doc_base_model_class(self):
        """Test to check base model class documentation
        """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_doc_amenity_methods(self):
        """Test to check base_model's methods documentation
        """
        for method in dir(BaseModel):
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
