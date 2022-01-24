import pytest


@pytest.fixture(scope='function')
def measure_str():
    return """
    {
      "codi": 32,
      "lectures": [
        {
          "data": "2022-01-01T00:00Z",
          "valor": 6.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T00:30Z",
          "valor": 5.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T01:00Z",
          "valor": 4.7,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T01:30Z",
          "valor": 5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T02:00Z",
          "valor": 3.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T02:30Z",
          "valor": 3.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T03:00Z",
          "valor": 3.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T03:30Z",
          "valor": 3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T04:00Z",
          "valor": 2.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T04:30Z",
          "valor": 2.1,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T05:00Z",
          "valor": 1.8,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T05:30Z",
          "valor": 1.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T06:00Z",
          "valor": 1.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T06:30Z",
          "valor": 1.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T07:00Z",
          "valor": 0.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T07:30Z",
          "valor": 1.1,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T08:00Z",
          "valor": 1.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T08:30Z",
          "valor": 3.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T09:00Z",
          "valor": 5.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T09:30Z",
          "valor": 7.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T10:00Z",
          "valor": 9.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T10:30Z",
          "valor": 12.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T11:00Z",
          "valor": 14.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T11:30Z",
          "valor": 17.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T12:00Z",
          "valor": 17.8,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T12:30Z",
          "valor": 17.7,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T13:00Z",
          "valor": 17.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T13:30Z",
          "valor": 18,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T14:00Z",
          "valor": 17.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T14:30Z",
          "valor": 16.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T15:00Z",
          "valor": 13.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T15:30Z",
          "valor": 11.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T16:00Z",
          "valor": 10.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T16:30Z",
          "valor": 10.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T17:00Z",
          "valor": 10.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T17:30Z",
          "valor": 9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T18:00Z",
          "valor": 8.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T18:30Z",
          "valor": 8.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T19:00Z",
          "valor": 7.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T19:30Z",
          "valor": 7.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T20:00Z",
          "valor": 6.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T20:30Z",
          "valor": 5.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T21:00Z",
          "valor": 5.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T21:30Z",
          "valor": 5.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T22:00Z",
          "valor": 4.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T22:30Z",
          "valor": 4.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T23:00Z",
          "valor": 5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T23:30Z",
          "valor": 4.3,
          "estat": "T",
          "baseHoraria": "SH"
        }
      ]
    }
    """


@pytest.fixture(scope='function')
def measure_error_str(measure_str):
    return """
    {
      "lectures": [
        {
          "data": "2022-01-01T00:00Z",
          "valor": 6.3,
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T00:30Z",
          "valor": 5.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T01:00Z",
          "valor": 4.7,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T01:30Z",
          "valor": 5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T02:00Z",
          "valor": 3.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T02:30Z",
          "valor": 3.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T03:00Z",
          "valor": 3.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T03:30Z",
          "valor": 3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T04:00Z",
          "valor": 2.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T04:30Z",
          "valor": 2.1,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T05:00Z",
          "valor": 1.8,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T05:30Z",
          "valor": 1.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T06:00Z",
          "valor": 1.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T06:30Z",
          "valor": 1.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T07:00Z",
          "valor": 0.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T07:30Z",
          "valor": 1.1,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T08:00Z",
          "valor": 1.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T08:30Z",
          "valor": 3.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T09:00Z",
          "valor": 5.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T09:30Z",
          "valor": 7.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T10:00Z",
          "valor": 9.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T10:30Z",
          "valor": 12.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T11:00Z",
          "valor": 14.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T11:30Z",
          "valor": 17.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T12:00Z",
          "valor": 17.8,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T12:30Z",
          "valor": 17.7,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T13:00Z",
          "valor": 17.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T13:30Z",
          "valor": 18,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T14:00Z",
          "valor": 17.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T14:30Z",
          "valor": 16.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T15:00Z",
          "valor": 13.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T15:30Z",
          "valor": 11.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T16:00Z",
          "valor": 10.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T16:30Z",
          "valor": 10.4,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T17:00Z",
          "valor": 10.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T17:30Z",
          "valor": 9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T18:00Z",
          "valor": 8.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T18:30Z",
          "valor": 8.3,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T19:00Z",
          "valor": 7.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T19:30Z",
          "valor": 7.2,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T20:00Z",
          "valor": 6.6,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T20:30Z",
          "valor": 5.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T21:00Z",
          "valor": 5.5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T21:30Z",
          "valor": 5.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T22:00Z",
          "valor": 4.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T22:30Z",
          "valor": 4.9,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T23:00Z",
          "valor": 5,
          "estat": "T",
          "baseHoraria": "SH"
        },
        {
          "data": "2022-01-01T23:30Z",
          "valor": 4.3,
          "estat": "T",
          "baseHoraria": "SH"
        }
      ]
    }
    """
