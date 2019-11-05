import datetime
from db import db


class DeviceModel(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    benchmark_version = db.Column(db.String(10), nullable=False)
    device_model = db.Column(db.String(80), nullable=False)
    device_product = db.Column(db.String(80), nullable=False)
    device_board = db.Column(db.String(80), nullable=False)
    device_manufacturer = db.Column(db.String(80), nullable=False)
    device_brand = db.Column(db.String(80), nullable=False)
    device_hardware = db.Column(db.String(80), nullable=False)
    android_version = db.Column(db.String(80), nullable=False)
    build_type = db.Column(db.String(80), nullable=False)
    build_time = db.Column(db.String(80), nullable=False)
    fingerprint = db.Column(db.String(120), nullable=False)
    kernel_version = db.Column(db.String(200))
    timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    results = db.relationship(
        "ResultModel",
        backref=db.backref("device", lazy=True),
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )
