from db import db
from flask import request
from flask_restful import Resource
from models.device import DeviceModel
from models.result import ResultModel
from schemas.device import DeviceSchema
from schemas.result import ResultSchema


class Results(Resource):
    @classmethod
    def get(cls):
        result_list_schema = ResultSchema(many=True)
        results = result_list_schema.dump(ResultModel.query.all())
        return {"results": results}, 200

    @classmethod
    def post(cls):
        data = request.get_json()
        device_schema = DeviceSchema()
        result = device_schema.load(data)
        db.session.add(result)
        db.session.commit()

        return {"result": "Results uploaded successfully."}, 201


class DeviceResults(Resource):
    @classmethod
    def get(cls, model):
        result_list_schema = ResultSchema(many=True)
        device_results = ResultModel.query.join(DeviceModel).filter_by(device_model=model).all()
        response = result_list_schema.dump(device_results)

        if not response:
            return {"results": f"No results for {model}."}, 400

        return {"results": response}, 200
