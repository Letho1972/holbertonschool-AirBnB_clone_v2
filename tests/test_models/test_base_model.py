import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
import json
import os


class Test_BaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        try:
            os.remove('file.json')
        except:
            pass

    def tearDown(self):
        """Clean up after the test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test creating a default instance"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_kwargs(self):
        """Test creating an instance with kwargs"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance, instance)

    def test_kwargs_int(self):
        """Test creating an instance with invalid kwargs (int)"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        instance_dict.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**instance_dict)

    def test_save(self):
        """Test saving an instance to a file"""
        instance = BaseModel()
        instance.save()
        key = "BaseModel." + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """Test the string representation of an instance"""
        instance = BaseModel()
        string_repr = str(instance)
        self.assertIn('[BaseModel] ({})'.format(instance.id), string_repr)

    def test_to_dict(self):
        """Test converting an instance to a dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_kwargs_none(self):
        """Test creating an instance with invalid kwargs (None)"""
        invalid_kwargs = {None: None}
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**invalid_kwargs)

    def test_kwargs_one(self):
        """Test creating an instance with invalid kwargs (one key)"""
        invalid_kwargs = {'name': 'test'}
        new_instance = BaseModel(**invalid_kwargs)
        self.assertIn('Name', new_instance.to_dict())
        self.assertEqual(new_instance.updated_at, 'test')

    def test_id(self):
        """Test the id attribute"""
        instance = BaseModel()
        self.assertIsInstance(UUID(instance.id), UUID)

    def test_created_at(self):
        """Test the created_at attribute"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance.created_at, new_instance.updated_at)


if __name__ == "__main__":
    unittest.main()
