import unittest
from tests.test_models.test_base_model import Test_BaseModel
from models.amenity import Amenity


class Test_Amenity(Test_BaseModel):
    """Test the Amenity class"""

    def setUp(self):
        """Set up a clean storage instance before each test."""
        super().setUp()
        self.name = "Amenity"
        self.value = Amenity

    def test_name_column(self):
        """Test the name column in the Amenity table."""
        new_amenity = self.value()
        self.assertTrue(hasattr(new_amenity, 'name'))
        self.assertIsInstance(new_amenity.name, str)

    def test_place_amenities_relationship(self):
        """Test the relationship between Amenity and Place."""
        amenity = Amenity(name="Gym")
        self.assertIsInstance(amenity.place_amenities, list)

    def test_save_to_database(self):
        """Test saving an Amenity instance to the database."""
        amenity = Amenity(name="Pool")
        self.save_instance(amenity)

        amenity_key = "Amenity." + amenity.id
        self.assertTrue(amenity_key in self.storage.all(Amenity))

    def test_reload_from_database(self):
        """Test reloading an Amenity instance from the database."""
        amenity = Amenity(name="Sauna")
        self.save_instance(amenity)

        amenity_id = amenity.id
        self.storage.reload()

        # Test that the reloaded object has the same attributes
        reloaded_amenity = self.storage.get(Amenity, amenity_id)
        self.assertIsNotNone(reloaded_amenity)
        self.assertEqual(amenity.name, reloaded_amenity.name)


if __name__ == "__main__":
    unittest.main()
