from unittest import TestCase
from factory import alchemy, Sequence
from app.models import User
from app import create_app


class FlaskTestCase(TestCase):
    def setUp(self):
        self.app = create_app()


class UserFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User

    id = Sequence(lambda n: n)
    name = Sequence(lambda n: f'User {n}')
    password = Sequence(lambda n: f'pass{n}')
