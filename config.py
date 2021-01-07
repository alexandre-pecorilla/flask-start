import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
  SECRET_KEY = os.environ.get('SECRET_KEY')

  LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT') # Optional - for Heroku
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  MAIL_SERVER = os.environ.get('MAIL_SERVER')
  MAIL_PORT = int(os.environ.get('MAIL_PORT'))
  MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['alexandre@pecorilla.us'] # Replace by your admin email(s)

  POSTS_PER_PAGE = 10 # For pagination
  LANGUAGES = ["en"]

  REDIS_URL = os.environ.get("REDIS_URL") or "redis://"