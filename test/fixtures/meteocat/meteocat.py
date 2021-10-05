import pytest


@pytest.fixture(scope='session')
def meteocat_invalid_token():
    return {"message": "Forbidden"}
