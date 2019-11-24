from . import ma
from marshmallow import validates, ValidationError
from .models import DeviceModel, ResultModel


class DeviceSchema(ma.ModelSchema):
    results = ma.Nested("ResultSchema", many=True, exclude=("device",), required=True)

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


class ResultSchema(ma.ModelSchema):
    device = ma.Nested("DeviceSchema", many=False, exclude=("results",))

    class Meta:
        model = ResultModel
        exclude = ("id", "device_id")
        include_fk = True

    @validates("test_name")
    def validate_test_name(self, test_name):
        allowable_tests = (
            "List View Fling",
            "Image List View Fling",
            "Shadow Grid Fling",
            "High-hitrate text render",
            "Low-hitrate text render",
            "Edit Text Input",
            "Overdraw Test",
            "Bitmap Upload Test",
        )

        if test_name not in allowable_tests:
            raise ValidationError(f"{test_name} is not a valid test.")
