from flask import Blueprint
from flask_restful import Api
from resources.WebPage import WebPage

api_core = Blueprint('api', __name__)
api = Api(api_core)

api.add_resource(WebPage, '/webpages/')
