from flask import Blueprint, jsonify, request
from app.models import DeviceModel, ResultModel
from app.schemas import DeviceSchema, ResultSchema
from app.services import DeviceService, ResultService
from typing import List

bp = Blueprint("routes", __name__)


@bp.route("/devices", methods=["GET"])
def devices():
    device_list_schema = DeviceSchema(many=True, exclude=("results",))
    devices_list = device_list_schema.dump(DeviceService.get_all())
    return jsonify({"devices": devices_list}), 200


@bp.route("/results", methods=["GET"])
def get_results():
    result_list_schema = ResultSchema(many=True)
    results_list = result_list_schema.dump(ResultService.get_all())
    return jsonify({"results": results_list}), 200


@bp.route("/results", methods=["POST"])
def post_results():
    data = request.get_json()
    device_schema = DeviceSchema()
    result: DeviceModel = device_schema.load(data)
    DeviceService.create(result)

    return jsonify({"message": "Results uploaded successfully."}), 201


@bp.route("/results/<string:model>", methods=["GET"])
def results_model(model: str):
    result_list_schema = ResultSchema(many=True)
    device_results: List[ResultModel] = ResultService.get_by_model(model)
    response = result_list_schema.dump(device_results)

    if not response:
        return jsonify({"message": f"No results for {model}."}), 400

    return jsonify({"results": response}), 200
