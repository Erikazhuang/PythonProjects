import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'erikazhuang@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '7791350184'
    ADMINS = ['erikazhuang@gmail.com']

    UPLOAD_PATH = 'C:\\Users\\44792\\Documents\\PythonProjects\\adaptivemath\\web\\app\\upload\\'

    ITEMS_PER_PAGE = 10

    TOTAL_QUESTIONS_PER_TEST = 2