from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import bs4
import re

is_link_well_formed = re.compile(r"^https://.+(png|jpg|jpeg|JPEG|JPG|PNG)$")

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/images/')
def get_images():
    web_page = request.args.get('host')
    response = requests.get(web_page)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    images_link = soup.select("img")

    images = [image['src'] for image in images_link if is_link_well_formed.match(image['src'])]

    images_without_repeats = list(set(images))

    return jsonify({
        "count": len(images_without_repeats),
        "results": images_without_repeats,
        "status": 200
    })


@app.route('/api/')
def index():
    return jsonify({
        "message": "Welcome to Foxbel Scrapper.",
        "version": "1.0"
    })


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "message": "este recurso no existe."
    })