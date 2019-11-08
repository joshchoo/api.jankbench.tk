from app.errors import bp
from flask import jsonify
from marshmallow import ValidationError


@bp.app_errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400
