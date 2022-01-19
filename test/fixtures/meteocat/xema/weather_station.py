import pytest
import json


@pytest.fixture(scope='function')
def weather_station_status_str_closed():
    return """
    {
        "codi": 2,
        "dataInici": "1992-05-11T15:30Z",
        "dataFi": "2002-10-29T05:00Z"
    }
    """


@pytest.fixture(scope='function')
def weather_station_status_str_open():
    return """
    {
        "codi": 1,
        "dataInici": "2002-10-29T05:00Z",
        "dataFi": null
    }
    """


@pytest.fixture(scope='function')
def weather_station_status_json_closed(weather_station_status_str_closed):
    return json.loads(weather_station_status_str_closed)


@pytest.fixture(scope='function')
def weather_station_status_json_open(weather_station_status_str_open):
    return json.loads(weather_station_status_str_open)
