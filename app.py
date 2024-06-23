import os
from functools import wraps
from flask import (
Flask,flash,render_template,
redirect,request,session,url_for)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
import cloudinary.uploader
import cloudinary.api

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Configurations for MONGO DB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Configurations for Cloudinary API
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)


@app.route("/")
@app.route("/get_pets")
def get_pets():
    pets = mongo.db.pets.find()
    return render_template('pets.html', pets=pets)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            
