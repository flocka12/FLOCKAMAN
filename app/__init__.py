""" module to Create the app """
from flask import Flask

def create_app():
    ''' create app and register blueprints '''
    app = Flask(__name__)

    return app
    