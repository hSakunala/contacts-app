# Contains the main cofiguration of the applicaiton
# Building the api with Flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # Cross Origin Request- send request to backend from different url

app= Flask(__name__)
CORS(app)

# Specify the location of the local sqlite db on machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# dont track all modifications to the db (for now)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create a db instance and gives access to specified db
db = SQLAlchemy(app)

