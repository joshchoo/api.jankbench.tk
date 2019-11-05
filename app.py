from db import db
from flask import Flask, jsonify
from flask_restful import Api
from ma import ma
from marshmallow import ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db.init_app(app)
ma.init_app(app)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
