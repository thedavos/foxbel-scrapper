# third party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# author libraries
from .config import Config
from .views import views as views_blueprint
from services.api import api_core as api_blueprint

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # blueprint for api routes
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # blueprint for non-api routes
    app.register_blueprint(views_blueprint, url_prefix='/')

    return app
