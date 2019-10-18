# native libraries
import os

# third party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# author modules
from api.api import api_core as api_blueprint
import main as main_blueprint


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    load_dotenv()
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{os.getenv("DIALECT")}+{os.getenv("DRIVER")}://' \
                                            f'{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/' \
                                            f'{os.getenv("DATABASE")} '

    db.init_app(app)

    # blueprint for api routes
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # blueprint for non-api routes
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
