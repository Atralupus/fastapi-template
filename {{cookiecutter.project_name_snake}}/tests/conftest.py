import pytest
from fastapi.testclient import TestClient
from rest_api.app import create_app

_app = create_app()


@pytest.fixture()
def app():
    return _app


@pytest.fixture()
def test_client():
    return TestClient(_app)
