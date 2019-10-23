from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'{os.getenv("DIALECT")}+{os.getenv("DRIVER")}://' \
                              f'{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/' \
                              f'{os.getenv("DATABASE")}'
