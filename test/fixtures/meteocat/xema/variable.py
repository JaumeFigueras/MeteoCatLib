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
