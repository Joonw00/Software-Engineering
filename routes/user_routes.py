from flask import Blueprint, render_template, request, redirect

from models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/login")
def login():
    return render_template("login.html")


@user_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get the form data
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")

        # Create a new User instance
        user = User(username=username, name=name, password=password, coin=0, money=0)

        # Save the user to the MongoDB collection
        from app import mongo
        mongo.db.users.insert_one(user.__dict__)

        # Redirect to the login page after successful signup
        return redirect("/login")

    # Render the signup page
    return render_template("signup.html")
