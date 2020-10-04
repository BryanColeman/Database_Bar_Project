import os

from flask import Flask
from flask_login import LoginManager

from config import Config

from flask_uploads import configure_uploads, IMAGES, UploadSet

base_directory = os.path.abspath(os.path.dirname(__file__))

applicatio = app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'temp_password'
app.config['UPLOADS_DEFAULT_DEST'] = base_directory + '/static/img/'
app.config['UPLOADS_DEFAULT_URL'] = 'http://localhost:5000/static/img/'
app.config['UPLOADED_IMAGES_DEST'] = base_directory + '/static/img/'
app.config['UPLOADED_IMAGES_URL'] = 'http://localhost:5000/static/img/'

images=UploadSet('images', IMAGES)
configure_uploads(app, images)

login = LoginManager(app)
# this will automatically send the user back to the
# login page if there is no user logined
# this essentially requires a login
login.login_view = 'index'

from app import models, routes