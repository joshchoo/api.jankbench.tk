import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS", False
    )


class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TESTING_DATABASE_URL", "sqlite:///" + os.path.join(basedir, "testing.db")
    )


cache_config = {
    "CACHE_TYPE": os.environ.get("CACHE_TYPE", "redis"),
    "CACHE_REDIS_URL": os.environ.get("REDIS_URL", "redis://localhost:6379"),
}
