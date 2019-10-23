# native libraries
import re

# third-party libraries
from flask_restful import Resource
from flask import request

# project libraries
from services.scrapper import ImagesWeb


class WebPage(Resource):
    def get(self):
        host = request.args.get('host')
        is_host_correct = re.compile(r"^https?://.+\..+$")

        if host is None:
            return {
                "message": "Data Incomplete. Please fill parameters correctly",
            }, 400

        if is_host_correct.match(host):
            images = ImagesWeb(host).images_links

            return {"results": images}, 200
        else:
            return {"message": "Incorrect host, check out what you written"}, 400

