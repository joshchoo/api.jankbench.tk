from app import create_app
from app import db as _db
import pytest


@pytest.fixture(scope="session", autouse=False)
def app(request):
    app = create_app("TestingConfig")

    # Push Application Context
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="function", autouse=False)
def client(app):
    return app.test_client()


@pytest.fixture(scope="function", autouse=False)
def db(app, request):
    _db.app = app
    _db.drop_all()
    _db.session.commit()
    _db.create_all()

    def teardown():
        _db.drop_all()
        _db.session.commit()

    request.addfinalizer(teardown)
    return _db
