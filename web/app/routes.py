from flask import Blueprint, jsonify, request
from . import db
from .models import DeviceModel, ResultModel
from .schemas import DeviceSchema, ResultSchema

bp = Blueprint('routes', __name__)


@bp.route('/devices', methods=['GET'])
def devices():
    device_list_schema = DeviceSchema(many=True, exclude=("results",))
    devices_list = device_list_schema.dump(DeviceModel.query.all())
    return jsonify({"devices": devices_list}), 200


@bp.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        result_list_schema = ResultSchema(many=True)
        results_list = result_list_schema.dump(ResultModel.query.all())
        return jsonify({"results": results_list}), 200

    elif request.method == 'POST':
        data = request.get_json()
        device_schema = DeviceSchema()
        result = device_schema.load(data)
        db.session.add(result)
        db.session.commit()

        return jsonify({"result": "Results uploaded successfully."}), 201


@bp.route('/results/<model>', methods=['GET'])
def results_model(model: str):
    result_list_schema = ResultSchema(many=True)
    device_results = (
        ResultModel.query.join(DeviceModel).filter_by(device_model=model).all()
    )
    response = result_list_schema.dump(device_results)

    if not response:
        return jsonify({"results": f"No results for {model}."}), 400

    return jsonify({"results": response}), 200