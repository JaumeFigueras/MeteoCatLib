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


@pytest.fixture(scope='function')
def weather_station_api_response():
    return """
    [
      {
        "codi": "AN",
        "nom": "Barcelona - Av. Lluís Companys",
        "tipus": "A",
        "coordenades": {
          "latitud": 41.39004,
          "longitud": 2.18091
        },
        "emplacament": "Av. Lluís Companys (Ciutadella)",
        "altitud": 7.5,
        "municipi": {
          "codi": "080193",
          "nom": "Barcelona"
        },
        "comarca": {
          "codi": 13,
          "nom": "Barcelonès"
        },
        "provincia": {
          "codi": 8,
          "nom": "Barcelona"
        },
        "xarxa": {
          "codi": 1,
          "nom": "XEMA"
        },
        "estats": [
          {
            "codi": 2,
            "dataInici": "1992-05-11T15:30Z",
            "dataFi": "2002-10-29T05:00Z"
          },
          {
            "codi": 1,
            "dataInici": "2002-10-29T05:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": "CA",
        "nom": "Clariana de Cardener",
        "tipus": "A",
        "coordenades": {
          "latitud": 41.95378,
          "longitud": 1.5851
        },
        "emplacament": "Abocador comarcal",
        "altitud": 693,
        "municipi": {
          "codi": "250753",
          "nom": "Clariana de Cardener"
        },
        "comarca": {
          "codi": 35,
          "nom": "Solsonès"
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
            "dataInici": "1996-05-02T09:00Z",
            "dataFi": "2012-07-10T13:00Z"
          },
          {
            "codi": 1,
            "dataInici": "2012-07-10T13:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": "CB",
        "nom": "les Llosses",
        "tipus": "A",
        "coordenades": {
          "latitud": 42.15085,
          "longitud": 2.19914
        },
        "emplacament": "Abocador comarcal",
        "altitud": 700,
        "municipi": {
          "codi": "170963",
          "nom": "Les Llosses"
        },
        "comarca": {
          "codi": 31,
          "nom": "Ripollès"
        },
        "provincia": {
          "codi": 17,
          "nom": "Girona"
        },
        "xarxa": {
          "codi": 1,
          "nom": "XEMA"
        },
        "estats": [
          {
            "codi": 2,
            "dataInici": "1995-11-30T15:00Z",
            "dataFi": "2003-06-02T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2003-06-02T08:30Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": "CC",
        "nom": "Orís",
        "tipus": "A",
        "coordenades": {
          "latitud": 42.07398,
          "longitud": 2.20862
        },
        "emplacament": "Abocador comarcal",
        "altitud": 626,
        "municipi": {
          "codi": "081509",
          "nom": "Orís"
        },
        "comarca": {
          "codi": 24,
          "nom": "Osona"
        },
        "provincia": {
          "codi": 8,
          "nom": "Barcelona"
        },
        "xarxa": {
          "codi": 1,
          "nom": "XEMA"
        },
        "estats": [
          {
            "codi": 2,
            "dataInici": "1995-11-15T10:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": "CD",
        "nom": "la Seu d'Urgell - Bellestar",
        "tipus": "A",
        "coordenades": {
          "latitud": 42.37083,
          "longitud": 1.43277
        },
        "emplacament": "Abocador comarcal",
        "altitud": 849,
        "municipi": {
          "codi": "252038",
          "nom": "La Seu d'Urgell"
        },
        "comarca": {
          "codi": 4,
          "nom": "Alt Urgell"
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
            "dataInici": "1996-01-16T12:30Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": "CE",
        "nom": "els Hostalets de Pierola",
        "tipus": "A",
        "coordenades": {
          "latitud": 41.53109,
          "longitud": 1.80813
        },
        "emplacament": "Abocador de residus",
        "altitud": 316,
        "municipi": {
          "codi": "081629",
          "nom": "Els Hostalets de Pierola"
        },
        "comarca": {
          "codi": 6,
          "nom": "Anoia"
        },
        "provincia": {
          "codi": 8,
          "nom": "Barcelona"
        },
        "xarxa": {
          "codi": 1,
          "nom": "XEMA"
        },
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-03-31T23:00Z",
            "dataFi": null
          }
        ]
      }]
      """

