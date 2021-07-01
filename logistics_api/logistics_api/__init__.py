from flask import Flask
from logistics_api.configuration import config_by_name

def create_app(config_name: str) -> Flask:
    """
    Application factory, creates and configure the Flask application.
    """
    app = Flask(__name__)
    from .api.v1.routes import api_bp_v1

    if not isinstance(config_name, str):
        config_name = 'prod'

    app.register_blueprint(api_bp_v1)
    app.config.from_object(config_by_name[config_name])

    return app

