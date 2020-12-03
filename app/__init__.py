import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

base_directory = os.path.abspath(os.path.dirname(__file__))

application = app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'this_is_a_secret'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# this will automatically send the user back to the
# login page if there is no user logined
# this essentially requires a login
login.login_view = 'index'

from app import models, routes
from app import seed