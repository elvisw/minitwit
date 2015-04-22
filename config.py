# configuration
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, 'minitwit.db')
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'
