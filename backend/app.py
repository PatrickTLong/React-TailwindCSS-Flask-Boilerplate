from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Use DATABASE_URL from the environment, fallback to local development URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://username:password@localhost:5432/dbname'
)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def start():
    return jsonify("Works")
