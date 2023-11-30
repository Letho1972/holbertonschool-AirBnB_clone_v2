import unittest
from tests.test_models.test_base_model import Test_BaseModel
from models.city import City
from models.state import State


class TestCity(Test_BaseModel):
    """Test the City class"""

    def setUp(self):
        """Set up a clean storage instance before each test."""
        super().setUp()
        self.name = "City"
        self.value = City

    def test_name_column(self):
        """Test the name column in the City table."""
        new_city = self.value()
        self.assertTrue(hasattr(new_city, 'name'))
        self.assertIsInstance(new_city.name, str)

    def test_state_id_column(self):
        """Test the state_id column in the City table."""
        new_city = self.value()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertIsInstance(new_city.state_id, str)

    def test_state_id_foreign_key(self):
        """Test the foreign key relationship with the State table."""
        new_city = self.value()
        self.assertIsInstance(new_city.state_id, str)

        # Assuming you have a State class with a corresponding 'id' column
        state_id = "test_state_id"
        new_city.state_id = state_id
        self.save_instance(new_city)

        # Retrieve the saved city from the database
        reloaded_city = self.storage.get(City, new_city.id)
        self.assertIsNotNone(reloaded_city)
        self.assertEqual(reloaded_city.state_id, state_id)

    def test_relationship_with_state(self):
        """Test the relationship between City and State."""
        city = City(name="Test City", state_id="test_state_id")
        self.assertIsInstance(city.state, State)

    def test_save_to_database(self):
        """Test saving a City instance to the database."""
        city = City(name="Test City", state_id="test_state_id")
        self.save_instance(city)

        city_key = "City." + city.id
        self.assertTrue(city_key in self.storage.all(City))

    def test_reload_from_database(self):
        """Test reloading a City instance from the database."""
        city = City(name="Test City", state_id="test_state_id")
        self.save_instance(city)

        city_id = city.id
        self.storage.reload()

        # Test that the reloaded object has the same attributes
        reloaded_city = self.storage.get(City, city_id)
        self.assertIsNotNone(reloaded_city)
        self.assertEqual(city.name, reloaded_city.name)
        self.assertEqual(city.state_id, reloaded_city.state_id)


if __name__ == "__main__":
    unittest.main()
