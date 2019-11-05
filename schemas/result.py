from ma import ma
from models.result import ResultModel


class ResultSchema(ma.ModelSchema):
    class Meta:
        model = ResultModel
        dump_only = ("id",)
        include_fk = True
