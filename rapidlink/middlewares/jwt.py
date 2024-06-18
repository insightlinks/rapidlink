from flask_jwt_extended import JWTManager


def init_jwt(app):
    jwt = JWTManager(app)
    return jwt
