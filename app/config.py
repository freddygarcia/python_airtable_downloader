import os

# Application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    APP_PORT = '5000'
    APP_HOST = '127.0.0.1'


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SESSION_TYPE = 'filesystem'


class TestingConfig(BaseConfig):

    DEBUG = True
    TESTING = True
