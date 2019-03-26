__author__ = 'Suleiman'


class Config:
    def __init__(self):
        pass

    CSRF_ENABLED = True
    DEBUG = False

    SECRET_KEY = '034545-this-is-a-big-secret-9345'

    STATIC_FOLDER = "static"


class ProdConfig(Config):
    SERVER_NAME = "my-super-website.com"
    DEBUG = False


class DevConfig(Config):
    SERVER_NAME = "flask-subdomain.com:5000"
    DEBUG = True
