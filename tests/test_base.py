import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

os.environ["TESTING"] = "True"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
