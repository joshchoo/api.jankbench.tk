from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import connexion

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()


def create_app(config_name=None):
    # Initialize core app
    connex_app = connexion.App(__name__, specification_dir=".")
    connex_app.add_api("swagger.yaml", strict_validation=True, validate_responses=True)
    app = connex_app.app
    app.config.from_object("config.DefaultConfig")
    # Overwrite config values
    if config_name:
        app.config.from_object("config." + config_name)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Register Blueprints
    from app.api.routes import bp as routes_bp

    app.register_blueprint(routes_bp, url_prefix="/v1")

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    return app
