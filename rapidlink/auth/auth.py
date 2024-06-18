from flask import request
from rapidlink.helpers import response
from rapidlink.auth import authorize
from rapidlink.controllers import auth_controller


@authorize.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return response.ResponseClass.bad_request(
            message="Username and password are required to login",
        )
    return auth_controller.login(username, password)


@authorize.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    if not username:
        return response.ResponseClass.bad_request(
            message="Username is required",
        )
    if password != confirm_password or not password or not confirm_password:
        return response.ResponseClass.bad_request(
            message="Passwords do not match",
        )
    return auth_controller.signup(username, password)


@authorize.route("/signout", methods=["POST"])
def signout():
    return "signout"


@authorize.route("/forgot-password", methods=["POST"])
def forgot_password():
    return "forgot_password"


@authorize.route("/reset-password", methods=["POST"])
def reset_password():
    return "reset_password"
