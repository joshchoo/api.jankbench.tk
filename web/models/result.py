from db import db


class ResultModel(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    jank_penalty = db.Column(db.Integer, nullable=False)
    consistency_bonus = db.Column(db.Integer, nullable=False)
    jank_pct = db.Column(db.Numeric, nullable=False)
    bad_frame_pct = db.Column(db.Numeric, nullable=False)
    total_frames = db.Column(db.Integer, nullable=False)
    ms_avg = db.Column(db.Numeric, nullable=False)
    ms_90th_pctl = db.Column(db.Numeric, nullable=False)
    ms_95th_pctl = db.Column(db.Numeric, nullable=False)
    ms_99th_pctl = db.Column(db.Numeric, nullable=False)

    device_id = db.Column(db.Integer, db.ForeignKey("devices.id"), nullable=False)
