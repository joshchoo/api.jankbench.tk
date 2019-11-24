from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.models import DeviceModel, ResultModel
from app.schemas import DeviceSchema, ResultSchema
from app.services import DeviceService, ResultService


def test_device_create(db: SQLAlchemy):
    # GIVEN 1 device entry is created
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
        "kernel_version": "Linux version 4.4.153-perf+ (OnePlus@rd-build-191) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Wed Jul 31 18:37:40 HKT 2019",
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

    device: DeviceModel = DeviceSchema().load(oneplus5_data)
    DeviceService.create(device)

    # WHEN user requests for all devices
    devices: List[DeviceModel] = DeviceService.get_all()

    # THEN 1 device should be returned
    assert len(devices) == 1


def test_device_get_all(db: SQLAlchemy):
    # GIVEN 2 existing devices in database
    oneplus6_data = {
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
        "kernel_version": "Linux version 4.9.179-perf+ (OnePlus@rd-build-75) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Tue Oct 8 17:52:41 CST 2019",
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
        "kernel_version": "Linux version 4.4.153-perf+ (OnePlus@rd-build-191) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Wed Jul 31 18:37:40 HKT 2019",
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

    oneplus5: DeviceModel = DeviceSchema().load(oneplus5_data)
    oneplus6: DeviceModel = DeviceSchema().load(oneplus6_data)

    DeviceService.create(oneplus5)
    DeviceService.create(oneplus6)

    # WHEN user requests for all devices
    devices: List[DeviceModel] = DeviceService.get_all()

    # THEN 2 devices should be returned
    assert len(devices) == 2


def test_result_get_all(db: SQLAlchemy):
    # GIVEN 3 existing test results in database
    oneplus6_data = {
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
        "kernel_version": "Linux version 4.9.179-perf+ (OnePlus@rd-build-75) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Tue Oct 8 17:52:41 CST 2019",
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
        "kernel_version": "Linux version 4.4.153-perf+ (OnePlus@rd-build-191) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Wed Jul 31 18:37:40 HKT 2019",
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

    oneplus5: DeviceModel = DeviceSchema().load(oneplus5_data)
    oneplus6: DeviceModel = DeviceSchema().load(oneplus6_data)

    DeviceService.create(oneplus5)
    DeviceService.create(oneplus6)

    # WHEN user requests for all test results
    results: List[ResultModel] = ResultService.get_all()

    # THEN 3 test results should be returned
    assert len(results) == 3


def test_result_get_by_model(db: SQLAlchemy):
    # GIVEN 3 existing test results for ONEPLUS A6013 in database
    oneplus6_data_a = {
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
        "kernel_version": "Linux version 4.9.179-perf+ (OnePlus@rd-build-75) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Tue Oct 8 17:52:41 CST 2019",
        "run_id": 1,
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

    oneplus6_data_b = {
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
        "kernel_version": "Linux version 4.9.179-perf+ (OnePlus@rd-build-75) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Tue Oct 8 17:52:41 CST 2019",
        "run_id": 2,
        "results": [
            {
                "test_name": "Bitmap Upload Test",
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
        "kernel_version": "Linux version 4.4.153-perf+ (OnePlus@rd-build-191) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Wed Jul 31 18:37:40 HKT 2019",
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

    oneplus5: DeviceModel = DeviceSchema().load(oneplus5_data)
    oneplus6_a: DeviceModel = DeviceSchema().load(oneplus6_data_a)
    oneplus6_b: DeviceModel = DeviceSchema().load(oneplus6_data_b)

    DeviceService.create(oneplus5)
    DeviceService.create(oneplus6_a)
    DeviceService.create(oneplus6_b)

    # WHEN user requests for all test results for ONEPLUS A6013
    results: List[ResultModel] = ResultService.get_by_model("ONEPLUS A6013")

    # THEN 3 results should be returned
    assert len(results) == 3
