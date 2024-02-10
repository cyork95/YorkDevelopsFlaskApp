import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Initialize the Flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes after initializing the app to avoid circular imports
from app import models
from app import routes
