import unittest
from tests.test_models.test_base_model import Test_BaseModel
from models.state import State
from models.city import City
from os import getenv
from models import storage


class TestState(Test_BaseModel):
    """Test the State class"""

    def setUp(self):
        """Set up the test environment"""
        super().setUp()
        self.name = "State"
        self.value = State

    def test_name_column(self):
        """Test the name column in the State table."""
        new_state = self.value()
        self.assertTrue(hasattr(new_state, 'name'))
        self.assertIsInstance(new_state.name, str)

    def test_cities_relation(self):
        """Test the relationship between State and City."""
        state = State(name="California")
        self.save_instance(state)

        if getenv("HBNB_TYPE_STORAGE") == "db":
            # Test relationship in database storage
            city = City(name="Los Angeles", state_id=state.id)
            self.save_instance(city)

            self.assertIn(city, state.cities)
            self.assertIn(state, city.state)

        else:
            # Test relationship in non-database storage
            city = City(name="San Francisco", state_id=state.id)
            self.save_instance(city)

            state_id = state.id
            storage.reload()

            # Test that the relationship is correctly loaded
            reloaded_state = storage.get(State, state_id)
            reloaded_city = storage.get(City, city.id)

            self.assertIn(reloaded_city, reloaded_state.cities)

    def test_cities_property(self):
        """Test the cities property in non-database storage."""
        if getenv("HBNB_TYPE_STORAGE") != "db":
            state = State(name="New York")
            self.save_instance(state)

            city1 = City(name="Albany", state_id=state.id)
            city2 = City(name="Buffalo", state_id=state.id)
            city3 = City(name="Syracuse", state_id=state.id)

            self.save_instance(city1)
            self.save_instance(city2)
            self.save_instance(city3)

            state_id = state.id
            storage.reload()

            # Test that the property correctly returns the list of cities
            reloaded_state = storage.get(State, state_id)
            cities = reloaded_state.cities

            self.assertEqual(len(cities), 3)
            self.assertIn(city1, cities)
            self.assertIn(city2, cities)
            self.assertIn(city3, cities)


if __name__ == "__main__":
    unittest.main()
