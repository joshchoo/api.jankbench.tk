from ma import ma
from marshmallow import validates, ValidationError
from models.device import DeviceModel  # DO NOT REMOVE
from models.result import ResultModel


class ResultSchema(ma.ModelSchema):
    device = ma.Nested("DeviceSchema", many=False, exclude=("results",))

    class Meta:
        model = ResultModel
        dump_only = ("id", "device_id")
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
