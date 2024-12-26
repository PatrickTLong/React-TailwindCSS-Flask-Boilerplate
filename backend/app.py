from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
import sqlalchemy.orm as so
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/dbname'
#the above is for local development. 
# Once you want to store the URL
# in a safe location remove the above.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

@app.route("/")
def start():
    return jsonify("Works")

    