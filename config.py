class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'Essa chave não é segura'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
