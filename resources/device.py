from flask_restful import Resource
from models.device import DeviceModel
from schemas.device import DeviceSchema


class Devices(Resource):
    @classmethod
    def get(cls):
        device_list_schema = DeviceSchema(many=True, exclude=("results",))
        devices = device_list_schema.dump(DeviceModel.query.all())
        return {"devices": devices}, 200
