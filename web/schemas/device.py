from ma import ma
from models.device import DeviceModel


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = DeviceModel
        dump_only = ("id",)
