from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()


class WebPage(Resource):
    def get(self):
        parser.add_argument('host', type=str)
        args = parser.parse_args(strict=True)
        host = args.host

        return {"message": host}

