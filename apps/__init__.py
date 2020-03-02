from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)
Migrate(app, db)

from apps.home.routes import home
app.register_blueprint(home, url_prefix='/')
