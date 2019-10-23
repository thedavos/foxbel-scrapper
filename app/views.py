# third party libraries
from flask import Blueprint, jsonify

views = Blueprint('views', __name__)


# @main.route('/api/')
# def index():
#     return jsonify({
#         "message": "Welcome to Foxbel Scrapper.",
#         "version": "1.0"
#     })

@views.route('/')
def index():
    return jsonify({"message": "Welcome"})


@views.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "message": "This resource doesn't exist"
    })
