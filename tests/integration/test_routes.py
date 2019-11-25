from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
import json


class TestApiV1:
    def test_get_devices_empty_db(self, client: FlaskClient, db: SQLAlchemy):
        with client:  # establish request context
            rv = client.get("/v1/devices")
            assert rv.status_code == 200

            response = rv.get_json()
            assert len(response["devices"]) == 0

    def test_get_results_empty_db(self, client: FlaskClient, db: SQLAlchemy):
        with client:
            rv = client.get("/v1/results")
            assert rv.status_code == 200

            response = rv.get_json()
            assert len(response["results"]) == 0

    def test_post_incomplete_result(self, client: FlaskClient, db: SQLAlchemy):
        post_result = {
            "benchmark_version": "0.1",
            "device_name": "OnePlus6T",
            "device_model": "ONEPLUS A6013",
            "device_product": "OnePlus6T",
        }
        with client:
            rv = client.post("/v1/results", json=post_result)
            assert rv.status_code == 400

    def test_post_data_without_result(self, client: FlaskClient, db: SQLAlchemy):
        post_result = {
            "benchmark_version": "0.1",
            "device_name": "OnePlus6T",
            "device_model": "ONEPLUS A6013",
            "device_product": "OnePlus6T",
            "device_board": "sdm845",
            "device_manufacturer": "OnePlus",
            "device_brand": "OnePlus",
            "device_hardware": "qcom",
            "android_version": "10",
            "build_type": "user",
            "build_time": "1570526427",
            "fingerprint": "OnePlus/OnePlus6T/OnePlus6T:10/QKQ1.190716.003/1910050400:user/release-keys",
            "kernel_version": "Linux version 4.9.179-perf+",
            "run_id": 23940825,
        }
        with client:
            rv = client.post("/v1/results", json=post_result)
            assert rv.status_code == 400

    def test_post_data_empty_result(self, client: FlaskClient, db: SQLAlchemy):
        post_result = {
            "benchmark_version": "0.1",
            "device_name": "OnePlus6T",
            "device_model": "ONEPLUS A6013",
            "device_product": "OnePlus6T",
            "device_board": "sdm845",
            "device_manufacturer": "OnePlus",
            "device_brand": "OnePlus",
            "device_hardware": "qcom",
            "android_version": "10",
            "build_type": "user",
            "build_time": "1570526427",
            "fingerprint": "OnePlus/OnePlus6T/OnePlus6T:10/QKQ1.190716.003/1910050400:user/release-keys",
            "kernel_version": "Linux version 4.9.179-perf+",
            "run_id": 23940825,
            "results": [],
        }
        with client:
            rv = client.post("/v1/results", json=post_result)
            assert rv.status_code == 400

    def test_post_valid_result(self, client: FlaskClient, db: SQLAlchemy):
        post_result = {
            "benchmark_version": "0.1",
            "device_name": "OnePlus6T",
            "device_model": "ONEPLUS A6013",
            "device_product": "OnePlus6T",
            "device_board": "sdm845",
            "device_manufacturer": "OnePlus",
            "device_brand": "OnePlus",
            "device_hardware": "qcom",
            "android_version": "10",
            "build_type": "user",
            "build_time": "1570526427",
            "fingerprint": "OnePlus/OnePlus6T/OnePlus6T:10/QKQ1.190716.003/1910050400:user/release-keys",
            "kernel_version": "Linux version 4.9.179-perf+",
            "run_id": 23940823,
            "results": [
                {
                    "test_name": "List View Fling",
                    "score": 32,
                    "jank_penalty": 54,
                    "consistency_bonus": 50,
                    "jank_pct": 12.3,
                    "bad_frame_pct": 32.7,
                    "total_frames": 9100,
                    "ms_avg": 9.76,
                    "ms_90th_pctl": 11.12,
                    "ms_95th_pctl": 18.54,
                    "ms_99th_pctl": 24.13,
                }
            ],
        }

        with client:
            rv = client.post("/v1/results", json=post_result)
            assert rv.status_code == 201

    def test_get_results_for_model(self, client: FlaskClient, db: SQLAlchemy):
        oneplus6t_data = {
            "benchmark_version": "0.1",
            "device_name": "OnePlus6T",
            "device_model": "ONEPLUS A6013",
            "device_product": "OnePlus6T",
            "device_board": "sdm845",
            "device_manufacturer": "OnePlus",
            "device_brand": "OnePlus",
            "device_hardware": "qcom",
            "android_version": "10",
            "build_type": "user",
            "build_time": "1570526427",
            "fingerprint": "OnePlus/OnePlus6T/OnePlus6T:10/QKQ1.190716.003/1910050400:user/release-keys",
            "kernel_version": "Linux version 4.9.179-perf+",
            "run_id": 23940823,
            "results": [
                {
                    "test_name": "List View Fling",
                    "score": 32,
                    "jank_penalty": 54,
                    "consistency_bonus": 50,
                    "jank_pct": 12.3,
                    "bad_frame_pct": 32.7,
                    "total_frames": 9100,
                    "ms_avg": 9.76,
                    "ms_90th_pctl": 11.12,
                    "ms_95th_pctl": 18.54,
                    "ms_99th_pctl": 24.13,
                },
                {
                    "test_name": "Image List View Fling",
                    "score": 32,
                    "jank_penalty": 54,
                    "consistency_bonus": 50,
                    "jank_pct": 12.3,
                    "bad_frame_pct": 32.7,
                    "total_frames": 9100,
                    "ms_avg": 9.76,
                    "ms_90th_pctl": 11.12,
                    "ms_95th_pctl": 18.54,
                    "ms_99th_pctl": 24.13,
                },
            ],
        }

        oneplus5_data = {
            "android_version": "9",
            "benchmark_version": "0.1",
            "build_time": "1564569199000",
            "build_type": "user",
            "device_board": "msm8998",
            "device_brand": "OnePlus",
            "device_hardware": "qcom",
            "device_manufacturer": "OnePlus",
            "device_model": "ONEPLUS A5000",
            "device_name": "OnePlus5",
            "device_product": "OnePlus5",
            "fingerprint": "OnePlus/OnePlus5/OnePlus5:9/PKQ1.180716.001/1907311824:user/release-keys",
            "kernel_version": "Linux version 4.4.153-perf+",
            "run_id": -1718173302,
            "results": [
                {
                    "bad_frame_pct": 9.2741935483871,
                    "consistency_bonus": 1,
                    "jank_pct": 2.21774193548387,
                    "jank_penalty": 19,
                    "ms_90th_pctl": 11.4477123,
                    "ms_95th_pctl": 15.66393,
                    "ms_99th_pctl": 41.7292242599998,
                    "ms_avg": 7.52272483669355,
                    "score": 821,
                    "test_name": "Edit Text Input",
                    "total_frames": 496,
                },
            ],
        }

        with client:
            rv = client.post("/v1/results", json=oneplus6t_data)
            assert rv.status_code == 201

            rv = client.post("/v1/results", json=oneplus5_data)
            assert rv.status_code == 201

            rv = client.get("v1/results/ONEPLUS A6013")
            assert rv.status_code == 200

            response = rv.get_json()

            assert len(response["results"]) == 2

            for result in response["results"]:
                assert result["device"]["device_model"] == "ONEPLUS A6013"
