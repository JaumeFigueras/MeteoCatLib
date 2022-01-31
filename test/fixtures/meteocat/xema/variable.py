import pytest


@pytest.fixture(scope='function')
def variable_state_str_closed():
    return """
    {
        "codi": 2,
        "dataInici": "2008-06-25T08:00Z",
        "dataFi": "2014-06-20T08:30Z"
    }
    """


@pytest.fixture(scope='function')
def variable_state_str_open():
    return """
    {
        "codi": 1,
        "dataInici": "2014-06-20T08:30Z",
        "dataFi": null
    }
    """


@pytest.fixture(scope='function')
def variable_time_base_str_closed():
    return """
    {
        "codi": "HO",
        "dataInici": "2008-06-25T08:00Z",
        "dataFi": "2014-04-24T00:00Z"
    }
    """


@pytest.fixture(scope='function')
def variable_time_base_str_open():
    return """
    {
        "codi": "SH",
        "dataInici": "2014-04-24T00:00Z",
        "dataFi": null
    }
    """


@pytest.fixture(scope='function')
def variable_str():
    return """
    {
        "codi": 26,
        "nom": "Velocitat del vent a 2 m (vec.)",
        "unitat": "m/s",
        "acronim": "VV2vec",
        "tipus": "DAT",
        "decimals": 1,
        "estats": [
            {
                "codi": 2,
                "dataInici": "2008-06-25T08:00Z",
                "dataFi": "2014-06-20T08:30Z"
            },
            {
                "codi": 1,
                "dataInici": "2014-06-20T08:30Z",
                "dataFi": null
            }
        ],
        "basesTemporals": [
            {
                "codi": "HO",
                "dataInici": "2008-06-25T08:00Z",
                "dataFi": "2014-04-24T00:00Z"
            },
            {
                "codi": "SH",
                "dataInici": "2014-04-24T00:00Z",
                "dataFi": null
            },
            {
                "codi": "HO",
                "dataInici": "2008-06-25T08:00Z",
                "dataFi": "2014-04-24T00:00Z"
            },
            {
                "codi": "SH",
                "dataInici": "2014-04-24T00:00Z",
                "dataFi": null
            }
        ]
    }
    """


@pytest.fixture(scope='function')
def variable_str_incomplete():
    return """
    {
        "codi": 26,
        "nom": "Velocitat del vent a 2 m (vec.)",
        "unitat": "m/s",
        "acronim": "VV2vec",
        "tipus": "DAT",
        "decimals": 1,
        "basesTemporals": [
            {
                "codi": "HO",
                "dataInici": "2008-06-25T08:00Z",
                "dataFi": "2014-04-24T00:00Z"
            },
            {
                "codi": "SH",
                "dataInici": "2014-04-24T00:00Z",
                "dataFi": null
            },
            {
                "codi": "HO",
                "dataInici": "2008-06-25T08:00Z",
                "dataFi": "2014-04-24T00:00Z"
            },
            {
                "codi": "SH",
                "dataInici": "2014-04-24T00:00Z",
                "dataFi": null
            }
        ]
    }
    """


@pytest.fixture(scope='function')
def variable_measured_api_response():
    return """
    [
      {
        "codi": 3,
        "nom": "Humitat relativa màxima",
        "unitat": "%",
        "acronim": "HRx",
        "tipus": "DAT",
        "decimals": 0,
        "estats": [
          {
            "codi": 2,
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 26,
        "nom": "Velocitat del vent a 2 m (vec.)",
        "unitat": "m/s",
        "acronim": "VV2vec",
        "tipus": "DAT",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "2008-06-25T08:00Z",
            "dataFi": "2014-06-20T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2014-06-20T08:30Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "2008-06-25T08:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          },
          {
            "codi": "HO",
            "dataInici": "2008-06-25T08:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 27,
        "nom": "Direcció del vent a 2 m (m. u)",
        "unitat": "°",
        "acronim": "DV2u",
        "tipus": "DAT",
        "decimals": 0,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-06-20T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2014-06-20T08:30Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          },
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 28,
        "nom": "Desviació est. de la direcció del vent a 2 m",
        "unitat": "°",
        "acronim": "DVdest2",
        "tipus": "DAT",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-06-20T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2014-06-20T08:30Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          },
          {
            "codi": "HO",
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 32,
        "nom": "Temperatura",
        "unitat": "°C",
        "acronim": "T",
        "tipus": "DAT",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 33,
        "nom": "Humitat relativa",
        "unitat": "%",
        "acronim": "HR",
        "tipus": "DAT",
        "decimals": 0,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 35,
        "nom": "Precipitació",
        "unitat": "mm",
        "acronim": "PPT",
        "tipus": "DAT",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 36,
        "nom": "Irradiància solar global",
        "unitat": "W/m²",
        "acronim": "RS",
        "tipus": "DAT",
        "decimals": 0,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-06-20T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2014-06-20T08:30Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          },
          {
            "codi": "HO",
            "dataInici": "1996-01-04T11:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 37,
        "nom": "Desviació est. de la irradiància solar global",
        "unitat": "W/m²",
        "acronim": "RSdest",
        "tipus": "DAT",
        "decimals": 0,
        "estats": [
          {
            "codi": 2,
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-06-20T08:30Z"
          },
          {
            "codi": 1,
            "dataInici": "2014-06-20T08:30Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          },
          {
            "codi": "HO",
            "dataInici": "2009-10-07T09:00Z",
            "dataFi": "2014-04-24T00:00Z"
          },
          {
            "codi": "SH",
            "dataInici": "2014-04-24T00:00Z",
            "dataFi": null
          }
        ]
      }]
    """


@pytest.fixture(scope='function')
def variable_auxiliar_api_response():
    return """
    [
      {
        "codi": 900,
        "nom": "Precipitació acumulada en 10 min",
        "unitat": "mm",
        "acronim": "PPT10min",
        "tipus": "AUX",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "1999-03-12T13:00Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "DM",
            "dataInici": "1999-03-12T13:00Z",
            "dataFi": null
          }
        ]
      },
      {
        "codi": 901,
        "nom": "Precipitació acumulada en 1 min",
        "unitat": "mm",
        "acronim": "PPT1min",
        "tipus": "AUX",
        "decimals": 1,
        "estats": [
          {
            "codi": 2,
            "dataInici": "2009-07-21T18:45Z",
            "dataFi": null
          }
        ],
        "basesTemporals": [
          {
            "codi": "MI",
            "dataInici": "2009-07-21T18:45Z",
            "dataFi": null
          }
        ]
      }
    ]    
    """


@pytest.fixture(scope='function')
def variable_cmv_api_response():
    return """
    [
      {
        "codi": 6006,
        "nom": "Evapotranspiració de referència",
        "unitat": "mm",
        "acronim": "ETo",
        "tipus": "CMV",
        "decimals": 2,
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1999-03-12T13:00Z",
            "dataFi": null
          }
        ]
      }
    ]
    """


@pytest.fixture(scope='function')
def variable_cmv_api_response_invalid():
    return """
    [
      {
        "codi": 6006,
        "nom": "Evapotranspiració de referència",
        "unitat": "mm",
        "acronim": "ETo",
        "tipus": "CMV",
        "basesTemporals": [
          {
            "codi": "HO",
            "dataInici": "1999-03-12T13:00Z",
            "dataFi": null
          }
        ]
      }
    ]
    """

