import unittest
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class Test_DBStorage():

    def setUp(self):
        """Set up a clean DBStorage instance before each test."""
        storage.reload()

    def test_new(self):
        """Test adding a new object to the database."""
        user = User()
        storage.new(user)
        storage.save()
        user_key = "User." + user.id
        self.assertTrue(user_key in storage.all(User))

    def test_all(self):
        """Test querying all objects of a class or all classes."""
        user = User()
        state = State()
        city = City()
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.save()
        user_key = "User." + user.id
        state_key = "State." + state.id
        city_key = "City." + city.id

        # Test querying all objects of a specific class
        self.assertTrue(user_key in storage.all(User))
        self.assertTrue(state_key in storage.all(State))
        self.assertTrue(city_key in storage.all(City))

        # Test querying all objects for all classes
        all_objects = storage.all()
        self.assertTrue(user_key in all_objects)
        self.assertTrue(state_key in all_objects)
        self.assertTrue(city_key in all_objects)

    def test_delete(self):
        """Test deleting an object from the database."""
        user = User()
        storage.new(user)
        storage.save()
        user_key = "User." + user.id

        # Test that the object is initially in the database
        self.assertTrue(user_key in storage.all(User))

        # Delete the object and test that it's removed from the database
        storage.delete(user)
        storage.save()
        self.assertFalse(user_key in storage.all(User))

    def test_reload(self):
        """Test reloading the database."""
        user = User()
        storage.new(user)
        storage.save()
        user_key = "User." + user.id

        # Test that the object is initially in the database
        self.assertTrue(user_key in storage.all(User))

        # Reload the database and test that the object is still there
        storage.reload()
        self.assertTrue(user_key in storage.all(User))


if __name__ == "__main__":
    unittest.main()
