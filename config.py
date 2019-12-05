import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            "sqlite:///" + os.path.join(BASEDIR, "app.db")
    SQLALCHEMY_ECHO = True

    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "localhost"
    MAIL_PORT = os.environ.get("MAIL_PORT") or 8025
