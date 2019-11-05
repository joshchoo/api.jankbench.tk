from db import db
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
