from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure your Flask app here
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with your Flask app
db = SQLAlchemy(app)

# Import routes after initializing the app to avoid circular imports
from app import routes