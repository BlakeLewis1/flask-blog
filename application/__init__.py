
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application import routes
