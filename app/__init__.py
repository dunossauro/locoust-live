from flask import Flask


def create_app():
    """Flask Factory."""
    app = Flask('locust tests')
    app.config.from_object("config.DevelopmentConfig")

    return app
