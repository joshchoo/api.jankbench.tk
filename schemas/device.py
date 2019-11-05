from ma import ma
from models.device import DeviceModel
from models.result import ResultModel  # DO NOT REMOVE


class DeviceSchema(ma.ModelSchema):
    results = ma.Nested('ResultSchema', many=True, exclude=('device',))

    class Meta:
        model = DeviceModel
        dump_only = ("id",)
