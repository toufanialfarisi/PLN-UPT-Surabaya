import os
basedir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///" + os.path.join(basedir, "db.sqlite")


class BaseConfig(object):
    SECRET_KEY = "mySecretKey2019Bisa"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(BaseConfig):
    SQLALCHEMY_DATABASE_URI = db_file

