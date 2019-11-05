from db import db
from flask import Flask, jsonify
from flask_restful import Api
from ma import ma
from marshmallow import ValidationError
from resources.device import Devices
from resources.result import DeviceResults, Results

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
api.add_resource(Devices, "/api/v1/devices")
api.add_resource(Results, "/api/v1/results")
api.add_resource(DeviceResults, "/api/v1/results/<string:model>")

db.init_app(app)
ma.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
