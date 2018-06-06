# encoding=UTF-8
from flask import Blueprint
from flask_restful import Api
from RESTfulApi.resources.account import Account


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Account, '/account')
