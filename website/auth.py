#defines the login and authentication services used for website
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/Sign-up")
def Sign_up():
    return "<p>Sign-Up</p>"