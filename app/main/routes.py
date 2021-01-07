from flask import render_template, flash, redirect, url_for, request
from app import db
from flask_babel import get_locale
from flask import g
from app.main import bp
from flask import current_app

@bp.before_app_request
def before_request():
  pass

@bp.route("/")
@bp.route("/index")
def index():
  return render_template("index.html")