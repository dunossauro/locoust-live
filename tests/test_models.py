from unittest import TestCase
from app.models import User


class TestUserModel(TestCase):
    def test_should_call_user_attrs(self):
        user = User('Testing', 'password')

        self.assertEqual(user.username, 'Testing')
        self.assertEqual(user.password, 'password')
