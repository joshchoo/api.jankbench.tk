from . import db
from .models import DeviceModel, ResultModel
from typing import List


class DeviceService:
    @staticmethod
    def get_all() -> List[DeviceModel]:
        return DeviceModel.query.all()

    @staticmethod
    def create(device: DeviceModel) -> DeviceModel:
        db.session.add(device)
        db.session.commit()


class ResultService:
    @staticmethod
    def get_all() -> List[ResultModel]:
        return ResultModel.query.all()

    @staticmethod
    def get_by_model(model: str) -> List[ResultModel]:
        return ResultModel.query.join(DeviceModel).filter_by(device_model=model).all()
