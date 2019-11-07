from ma import ma
from marshmallow import validates, ValidationError
from models.device import DeviceModel
from models.result import ResultModel  # DO NOT REMOVE


class DeviceSchema(ma.ModelSchema):
    results = ma.Nested("ResultSchema", many=True, exclude=("device",))

    class Meta:
        model = DeviceModel
        exclude = ("id",)

    @validates("results")
    def validate_results(self, results):
        if not results:
            raise ValidationError("results cannot be empty.")

    @validates("run_id")
    def validate_run_id(self, run_id):
        results = DeviceModel.query.filter_by(run_id=run_id).all()
        if len(results) > 0:
            raise ValidationError("Duplicate results not accepted.")
