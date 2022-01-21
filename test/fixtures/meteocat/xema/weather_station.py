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
def weather_station_status_str_error_from_date():
    return """
    {
        "codi": 2,
        "dataInici": "1992-05-11T53:30Z",
        "dataFi": "2002-10-29T05:00Z"
    }
    """


@pytest.fixture(scope='function')
def weather_station_status_str_error_to_date():
    return """
    {
        "codi": 2,
        "dataInici": "1992-05-11T15:30Z",
        "dataFi": "2002-18-29T05:00Z"
    }
    """


@pytest.fixture(scope='function')
def weather_station_status_json_closed(weather_station_status_str_closed):
    return json.loads(weather_station_status_str_closed)


@pytest.fixture(scope='function')
def weather_station_status_json_open(weather_station_status_str_open):
    return json.loads(weather_station_status_str_open)


@pytest.fixture(scope='function')
def weather_station_str():
    return """
    {
        "codi": "VM",
        "nom": "Vilanova de Segrià",
        "tipus": "A",
        "coordenades": {
            "latitud": 41.7145,
            "longitud": 0.62839
        },
        "emplacament": "Partida lo Sort",
        "altitud": 222,
        "municipi": {
            "codi": "252516",
            "nom": "Vilanova de Segrià"
        },
        "comarca": {
            "codi": 33,
            "nom": "Segrià"
        },
        "provincia": {
            "codi": 25,
            "nom": "Lleida"
        },
        "xarxa": {
            "codi": 1,
            "nom": "XEMA"
        },
        "estats": [
            {
                "codi": 2,
                "dataInici": "1997-09-17T15:00Z",
                "dataFi": "2003-02-24T21:00Z"
            },
            {
                "codi": 3,
                "dataInici": "2003-02-24T21:00Z",
                "dataFi": "2004-12-03T12:00Z"
            },
            {
                "codi": 2,
                "dataInici": "2004-12-03T12:00Z",
                "dataFi": null
            }
        ]
    }
    """


@pytest.fixture(scope='function')
def weather_station_json(weather_station_str):
    return json.loads(weather_station_str)


@pytest.fixture(scope='function')
def weather_station_str_incomplete():
    return """
    {
        "codi": "VM",
        "nom": "Vilanova de Segrià",
        "tipus": "A",
        "coordenades": {
            "latitud": 41.7145,
            "longitud": 0.62839
        },
        "emplacament": "Partida lo Sort",
        "altitud": 222,
        "municipi": {
            "codi": "252516",
            "nom": "Vilanova de Segrià"
        },
        "comarca": {
            "codi": 33,
            "nom": "Segrià"
        },
        "provincia": {
            "codi": 25,
            "nom": "Lleida"
        },
        "xarxa": {
            "codi": 1,
            "nom": "XEMA"
        }
    }
    """

