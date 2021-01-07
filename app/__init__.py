from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel
from flask import current_app
from redis import Redis
import rq


db = SQLAlchemy()
migrate = Migrate()

# If implementing an auth blueprint
#login = LoginManager()
#login.login_view = "auth.login"
#login.login_message = "Please login to access this page"

mail = Mail()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):

  app = Flask(__name__, static_folder="static", template_folder="templates")
  app.config.from_object(config_class)

  # If using Redis
  app.redis = Redis.from_url(app.config["REDIS_URL"])
  app.task_queue = rq.Queue("main-queue", connection=app.redis)

  db.init_app(app)
  migrate.init_app(app, db)
  # If implementing an auth blueprint
  #login.init_app(app)
  mail.init_app(app)
  moment.init_app(app)
  babel.init_app(app)

  # Load blueprints
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.errors import bp as errors_bp
  app.register_blueprint(errors_bp)

  # Get log by email
  if not app.debug and not app.testing:
    if app.config['MAIL_SERVER']:
      auth = None
      if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
      secure = None
      if app.config['MAIL_USE_TLS']:
        secure = ()
      mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject='Application Failure',
        credentials=auth, secure=secure)
      mail_handler.setLevel(logging.ERROR)
      app.logger.addHandler(mail_handler)

    # Log to STDOUT - For Heroku
    if app.config['LOG_TO_STDOUT']:
      stream_handler = logging.StreamHandler()
      stream_handler.setLevel(logging.INFO)
      app.logger.addHandler(stream_handler)
    # Log to .log file
    else:
      if not os.path.exists('logs'):
        os.mkdir('logs')
      file_handler = RotatingFileHandler('logs/application.log', maxBytes=10240,
                                         backupCount=10)
      file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
      file_handler.setLevel(logging.INFO)
      app.logger.addHandler(file_handler)

      app.logger.setLevel(logging.INFO)
      app.logger.info('Application startup')

  return app

@babel.localeselector
def get_locale():
  return request.accept_languages.best_match(current_app.config["LANGUAGES"])

from app import models