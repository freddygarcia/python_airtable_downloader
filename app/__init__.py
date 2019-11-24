from flask import Flask
from flask_session import Session
from os import environ


def load_config(config_class):
    from . import config as config_module
    # config_module = __import__('config')
    config = getattr(config_module, config_class)
    return config


def create_app():

    # App Instance
    app = Flask(__name__, template_folder='templates', static_url_path='/static')
    app.secret_key = '9e3ebfef-27a1-47fc-b509-6f60d613c811'

    # Load configuration
    settings_name = 'DevelopmentConfig'
    config = load_config(settings_name)
    app.config.from_object(config)

    # enable session
    Session(app)

    from app.main_module import routes
    routes.init_app(app)

    return app
