import unittest
from tests.test_models.test_base_model import Test_BaseModel
from models.user import User
from models.place import Place
from models.review import Review


class TestUser(Test_BaseModel):
    """Test the User class"""

    def setUp(self):
        """Set up the test environment"""
        super().setUp()
        self.name = "User"
        self.value = User

    def test_email_column(self):
        """Test the email column in the User table."""
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'email'))
        self.assertIsInstance(new_user.email, str)

    def test_password_column(self):
        """Test the password column in the User table."""
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertIsInstance(new_user.password, str)

    def test_first_name_column(self):
        """Test the first_name column in the User table."""
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'first_name'))
        self.assertIsInstance(new_user.first_name, str)

    def test_last_name_column(self):
        """Test the last_name column in the User table."""
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'last_name'))
        self.assertIsInstance(new_user.last_name, str)

    def test_places_relationship(self):
        """Test the relationship between User and Place."""
        user = User(email="test@example.com", password="password")
        self.save_instance(user)

        place = Place(name="Test Place", user_id=user.id)
        self.save_instance(place)

        self.assertIn(place, user.places)
        self.assertEqual(user, place.user)

    def test_reviews_relationship(self):
        """Test the relationship between User and Review."""
        user = User(email="test@example.com", password="password")
        self.save_instance(user)

        review = Review(text="Great place!", user_id=user.id)
        self.save_instance(review)

        self.assertIn(review, user.reviews)
        self.assertEqual(user, review.user)


if __name__ == "__main__":
    unittest.main()
