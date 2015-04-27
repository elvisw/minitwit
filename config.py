# configuration
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, 'minitwit.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'
