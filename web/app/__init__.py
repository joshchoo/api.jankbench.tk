from config import Config
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import connexion

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app():
    # Initialize core app
    connex_app = connexion.App(__name__, specification_dir=".")
    connex_app.add_api("swagger.yaml", strict_validation=True, validate_responses=True)
    app = connex_app.app
    app.config.from_object(Config())

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from app.routes import bp as routes_bp

    app.register_blueprint(routes_bp, url_prefix="/api/v1")

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    with app.app_context():
        # Create tables
        db.create_all()

    return app
