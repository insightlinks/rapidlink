from flask import Flask
from flask_cors import CORS
from config import Config
from rapidlink.middlewares import cors, jwt
from rapidlink.helpers import response


def create_app(config_class=Config) -> Flask:
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    CORS(app, **cors.default_app_cors())
    app.config.from_object(config_class)
    jwt.init_jwt(app)

    # add health check for Kubernetes health check
    app.add_url_rule(
        "/health",
        "health",
        lambda: response.ResponseClass.success(message="ok"),
        methods=["GET", "POST"],
    )

    from rapidlink.api import api
    from rapidlink.auth import authorize

    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(authorize, url_prefix="/auth")

    return app
