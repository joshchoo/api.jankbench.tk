from flask_restful import Resource
from models.result import ResultModel


class Results(Resource):
    def get(self):
        pass

    def post(self):
        pass


class DeviceResults(Resource):
    def get(self, model):
        pass
