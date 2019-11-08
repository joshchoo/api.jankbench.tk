CREATE TABLE devices (
	id INTEGER NOT NULL,
	run_id INTEGER NOT NULL,
	benchmark_version VARCHAR(10) NOT NULL,
	device_name VARCHAR(80) NOT NULL,
	device_model VARCHAR(80) NOT NULL,
	device_product VARCHAR(80) NOT NULL,
	device_board VARCHAR(80) NOT NULL,
	device_manufacturer VARCHAR(80) NOT NULL,
	device_brand VARCHAR(80) NOT NULL,
	device_hardware VARCHAR(80) NOT NULL,
	android_version VARCHAR(80) NOT NULL,
	build_type VARCHAR(80) NOT NULL,
	build_time VARCHAR(80) NOT NULL,
	fingerprint VARCHAR(120) NOT NULL,
	kernel_version VARCHAR(200),
	timestamp DATETIME NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE results (
	id INTEGER NOT NULL,
	test_name VARCHAR(80) NOT NULL,
	score INTEGER NOT NULL,
	jank_penalty INTEGER NOT NULL,
	consistency_bonus INTEGER NOT NULL,
	jank_pct FLOAT NOT NULL,
	bad_frame_pct FLOAT NOT NULL,
	total_frames INTEGER NOT NULL,
	ms_avg FLOAT NOT NULL,
	ms_90th_pctl FLOAT NOT NULL,
	ms_95th_pctl FLOAT NOT NULL,
	ms_99th_pctl FLOAT NOT NULL,
	device_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(device_id) REFERENCES devices (id)
);
