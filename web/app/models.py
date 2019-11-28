from . import db
from datetime import datetime


class DeviceModel(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    run_id = db.Column(db.Integer, nullable=False)
    benchmark_version = db.Column(db.String(10), nullable=False)
    device_name = db.Column(db.String(80), nullable=False)
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


class ResultModel(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    jank_penalty = db.Column(db.Integer, nullable=False)
    consistency_bonus = db.Column(db.Integer, nullable=False)
    jank_pct = db.Column(db.Numeric(8, 3), nullable=False)
    bad_frame_pct = db.Column(db.Numeric(8, 3), nullable=False)
    total_frames = db.Column(db.Integer, nullable=False)
    ms_avg = db.Column(db.Numeric(8, 3), nullable=False)
    ms_90th_pctl = db.Column(db.Numeric(8, 2), nullable=False)
    ms_95th_pctl = db.Column(db.Numeric(8, 2), nullable=False)
    ms_99th_pctl = db.Column(db.Numeric(8, 2), nullable=False)

    device_id = db.Column(db.Integer, db.ForeignKey("devices.id"), nullable=False)
