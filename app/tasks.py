import json
import sys
import time
from flask import render_template
from rq import get_current_job
from app import create_app, db

app = create_app()
app.app_context().push()

# Put Redis tasks here