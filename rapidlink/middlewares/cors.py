def default_app_cors():
    return {
        "supports_credentials": True,
        "resources": {
            r"/api/*": {"origins": "*", "methods": "GET,POST,PUT,DELETE,OPTIONS"},
            r"/auth/*": {"origins": "*", "methods": "POST,OPTIONS"},
        },
        "expose_headers": "*",
        "allow_headers": "*",
        "max_age": 3600,
    }