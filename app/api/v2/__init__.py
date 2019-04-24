''' module for creating and registering endpoints '''
from flask import Blueprint
from flask_restful import Api
from .views.user_view import UserSignup

VERSION = Blueprint('api_v2', __name__, url_prefix='/api/v2')

API = Api(VERSION)
API.add_resource(UserSignup, '/auth/signup')
