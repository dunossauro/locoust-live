from unittest import TestCase
from flask import Flask
from app import create_app
from base_testcase import FlaskTestCase


class TestFlaskFactory(TestCase):
    def test_create_app_sould_return_flask_app(self):
        self.assertIsInstance(create_app(), Flask)


class TestFlaskConfig(FlaskTestCase):
    def test_app_should_load_development_configuration_secret_key(self):
        self.assertEqual(
            self.app.config['SECRET_KEY'], 'Essa chave não é segura'
        )
