''' module for creating app '''
from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import APP_CONFIG
from DB.db_queries import create_tables
from .api.v2 import VERSION

def create_app(config_name):
    ''' creates app and registers blueprints '''
    app = Flask(__name__, instance_relative_config=True)
    create_tables()
    JWTManager(app)
    app.register_blueprint(VERSION)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    return app
    