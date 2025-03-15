from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import the routes from the routes.py file
from app import routes
