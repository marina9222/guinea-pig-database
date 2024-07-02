import os
from functools import wraps
from flask import (
Flask,flash,render_template,
redirect,request,session,url_for)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from collections import defaultdict
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
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)


@app.route("/")
@app.route("/get_pets")
def get_pets():
    all_pets = list(mongo.db.pets.find())
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})
        liked_pets = user.get("liked_pets", [])
    else:
        liked_pets = []

    all_users = list(mongo.db.users.find({}, {"liked_pets": 1}))
    pet_likes = defaultdict(int)
    for user in all_users:
        for pet_id in user.get("liked_pets", []):
            pet_likes[pet_id] += 1
    
    # Create a combined list of pets, with their liked status
    pets = []
    for pet in all_pets:
        pet_id = pet["_id"]
        liked = pet_id in liked_pets
        likes = pet_likes[pet_id]
        pets.append({"pet": pet, "liked": liked, "likes": likes})

    pets = sorted(pets, key=lambda x: x["likes"], reverse=True)
    return render_template('pets.html', pets=pets)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")      
            return redirect(url_for("register"))
         
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Password do not match!!")
            return redirect(url_for("register"))


        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "liked_pets": []
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!!")
        return redirect(url_for("get_pets", username= session["user"]))

        
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "get_pets", username= session["user"]))   
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/add_pet", methods=["GET", "POST"])
def add_pet():
    if request.method == "POST":
        pet_name = request.form.get("pet_name")
        pet_age = request.form.get("pet_age")
        pet_breed = request.form.get("pet_breed")
        pet_character = request.form.get("pet_character")
        pet_image = request.files.get("pet_image")
    
        
        if pet_image:
            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(pet_image)
            image_url = upload_result["secure_url"]
                
            pet = {
                "pet_name": pet_name,
                "pet_age": pet_age,
                "pet_breed": pet_breed,
                "pet_character": pet_character,
                "image_url": image_url,  
                "owner": session["user"]
            }

            mongo.db.pets.insert_one(pet)
            flash("Pet added successfully!")
            return redirect(url_for("my_pets"))
        else:
            flash("Please upload an image of your pet.")
            return redirect(url_for("add_pet"))
    
    
    breeds = mongo.db.breeds.find().sort("pet_breed", 1)
    return render_template("add_pet.html", breeds=breeds)


@app.route("/edit_pet/<pet_id>", methods =["GET", "POST"])
def edit_pet(pet_id):
    if request.method == "POST":
        pet_name = request.form.get("pet_name")
        pet_age = request.form.get("pet_age")
        pet_breed = request.form.get("pet_breed")
        pet_character = request.form.get("pet_character")
        pet_image = request.files.get("pet_image")
    
        
        update_data = {
            "pet_name": pet_name,
            "pet_age": pet_age,
            "pet_breed": pet_breed,
            "pet_character": pet_character,
            "owner": session["user"]
        }
        
        if pet_image:
            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(pet_image)
            image_url = upload_result["secure_url"]
            update_data["image_url"] = image_url

        mongo.db.pets.update_one({"_id": ObjectId(pet_id)}, {"$set": update_data})
        flash("Pet Information Updated Successfully!")
        return redirect(url_for("edit_pet", pet_id=pet_id))
    
    pet = mongo.db.pets.find_one({"_id": ObjectId(pet_id)})
    breeds = mongo.db.breeds.find().sort("pet_breed", 1)
    return render_template("edit_pet.html", pet=pet,  breeds=breeds)


@app.route("/delete_pet,<pet_id>", methods =["GET", "POST"])
def delete_pet(pet_id):
     pet = mongo.db.pets.find_one({"_id": ObjectId(pet_id)})
     if not pet:
        flash("Pet not found.")
        return redirect(url_for("my_pets")) 

     if request.method == "POST":
        confirm_delete = request.form.get("confirm_delete")
        if confirm_delete == "yes":
            mongo.db.pets.delete_one({"_id": ObjectId(pet_id)})
            flash("Pet Successfully Deleted!!")
        return redirect(url_for("my_pets"))  
     return render_template("confirm_delete_pet.html", pet=pet)
    

@app.route("/get_breeds")
def get_breeds():
    breeds = list(mongo.db.breeds.find().sort("pet_breed",1))
    return render_template("breeds.html",breeds = breeds)


@app.route("/breed/<breed_name>")
def breed_details(breed_name):
    breed = mongo.db.breeds.find_one({"pet_breed": breed_name})
    pets = list(mongo.db.pets.find({"pet_breed": breed_name}))
     
    if not breed:
        flash("Breed not found.")
        return redirect(url_for('get_breeds'))
    return render_template("breed_details.html", breed=breed, pets=pets)


@app.route("/my_pets")
def my_pets():
    if "user" not in session:
        flash("You need to be logged in to view your pets.")
        return redirect(url_for("login"))

    user = session["user"]
    pets = list(mongo.db.pets.find({"owner": user}))

    return render_template("my_pets.html", pets=pets)




@app.route("/like_pet/<pet_id>")
def like_pet(pet_id):
    """
    Add pet to user favourites if logged-in.
    """
    if "user" not in session:
        flash("You need to be logged in to like a pet.")
        return redirect(url_for("login"))

    mongo.db.users.find_one_and_update(
        {"username": session["user"]},
        {"$push": {"liked_pets": ObjectId(pet_id)}})
    flash("Lovely to hear you like this pet!")
    return redirect(url_for("get_pets"))


@app.route("/unlike_pet/<pet_id>")
def unlike_pet(pet_id):
    """
    Remove pet from user favourites if logged-in.
    """
    if "user" not in session:
        flash("You need to be logged in to unlike a pet.")
        return redirect(url_for("login"))

    mongo.db.users.find_one_and_update(
        {"username": session["user"]},
        {"$pull": {"liked_pets": ObjectId(pet_id)}})
    flash("How sad, you no longer like this pet.")
    return redirect(url_for("get_pets"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            
