# third party libraries
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/api/')
def index():
    return jsonify({
        "message": "Welcome to Foxbel Scrapper.",
        "version": "1.0"
    })


@main.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "message": "This resource doesn't exist"
    })
