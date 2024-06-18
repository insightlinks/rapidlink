from flask import Blueprint

authorize = Blueprint("auth", __name__)

from rapidlink.auth import auth