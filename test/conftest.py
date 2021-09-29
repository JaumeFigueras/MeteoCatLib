import pytest
from pytest_postgresql import factories
from pathlib import Path

test_folder = Path(__file__).parent
postgresql_session = factories.postgresql_proc(host='127.0.0.1', port=9876, user='gisfireuser')
postgresql_schema = factories.postgresql('postgresql_proc', dbname='test', load=[
    'database_init.sql',
    str(test_folder.parent) + '/database/meteocat_xdde.sql',
    str(test_folder.parent) + '/database/meteocat_xema.sql',
    str(test_folder.parent) + '/database/meteocat_ref.sql',
    'database_populate.sql'])


@pytest.fixture(scope='session')
def meteocat_invalid_token():
    return {"message": "Forbidden"}


@pytest.fixture(scope='session')
def meteocat_variables_measured_metadata():
    return [
          {
            "codi": 1,
            "nom": "Pressió atmosfèrica màxima",
            "unitat": "hPa",
            "acronim": "Px",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 2,
            "nom": "Pressió atmosfèrica mínima",
            "unitat": "hPa",
            "acronim": "Pn",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 3,
            "nom": "Humitat relativa màxima",
            "unitat": "%",
            "acronim": "HRx",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 4,
            "nom": "Temperatura màxima de subsòl a 5 cm",
            "unitat": "°C",
            "acronim": "TSUBx5",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 5,
            "nom": "Temperatura mínima de subsòl a 5 cm",
            "unitat": "°C",
            "acronim": "TSUBn5",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 6,
            "nom": "TDR màxima a 10 cm",
            "unitat": "%(1)",
            "acronim": "TDRx10",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 7,
            "nom": "TDR mínima a 10 cm",
            "unitat": "%(1)",
            "acronim": "TDRn10",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 8,
            "nom": "Desviació estàndard de la irradiància neta",
            "unitat": "W/m²",
            "acronim": "RNdest",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 9,
            "nom": "Irradiància reflectida",
            "unitat": "W/m²",
            "acronim": "Ir",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 10,
            "nom": "Irradiància fotosintèticament activa (PAR)",
            "unitat": "W/m²",
            "acronim": "PAR",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 11,
            "nom": "Temperatura de supefície",
            "unitat": "ºC",
            "acronim": "TSUP",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 12,
            "nom": "Temperatura màxima de superfície",
            "unitat": "ºC",
            "acronim": "TSUPx",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 13,
            "nom": "Temperatura mínima de superfície",
            "unitat": "ºC",
            "acronim": "TSUPn",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 14,
            "nom": "Temperatura de subsòl a 40 cm",
            "unitat": "ºC",
            "acronim": "TSUB40",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 20,
            "nom": "Velocitat del vent a 10 m (vec.)",
            "unitat": "m/s",
            "acronim": "VV10vec",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 21,
            "nom": "Direcció del vent a 10 m (m. u) ",
            "unitat": "°",
            "acronim": "DV10u",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 22,
            "nom": "Desviació est. de la direcció del vent a 10 m",
            "unitat": "°",
            "acronim": "DVdest10",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 23,
            "nom": "Velocitat del vent a 6 m (vec.)",
            "unitat": "m/s",
            "acronim": "VV6vec",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 24,
            "nom": "Direcció del vent a 6 m (m. u) ",
            "unitat": "°",
            "acronim": "DV6u",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 25,
            "nom": "Desviació est. de la direcció de vent a 6 m",
            "unitat": "°",
            "acronim": "DVdest6",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 26,
            "nom": "Velocitat del vent a 2 m (vec.)",
            "unitat": "m/s",
            "acronim": "VV2vec",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 27,
            "nom": "Direcció del vent a 2 m (m. u)",
            "unitat": "°",
            "acronim": "DV2u",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 28,
            "nom": "Desviació est. de la direcció del vent a 2 m",
            "unitat": "°",
            "acronim": "DVdest2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 30,
            "nom": "Velocitat del vent a 10 m (esc.)",
            "unitat": "m/s",
            "acronim": "VV10",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 31,
            "nom": "Direcció de vent 10 m (m. 1) ",
            "unitat": "°",
            "acronim": "DV10",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 32,
            "nom": "Temperatura",
            "unitat": "°C",
            "acronim": "T",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 33,
            "nom": "Humitat relativa",
            "unitat": "%",
            "acronim": "HR",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 34,
            "nom": "Pressió atmosfèrica",
            "unitat": "hPa",
            "acronim": "P",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 35,
            "nom": "Precipitació",
            "unitat": "mm",
            "acronim": "PPT",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 36,
            "nom": "Irradiància solar global",
            "unitat": "W/m²",
            "acronim": "RS",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 37,
            "nom": "Desviació est. de la irradiància solar global",
            "unitat": "W/m²",
            "acronim": "RSdest",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 38,
            "nom": "Gruix de neu a terra",
            "unitat": "mm",
            "acronim": "GNEU",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 39,
            "nom": "Radiació UV",
            "unitat": "MED/h",
            "acronim": "RUV",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 40,
            "nom": "Temperatura màxima",
            "unitat": "°C",
            "acronim": "Tx",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 42,
            "nom": "Temperatura mínima",
            "unitat": "°C",
            "acronim": "Tn",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 44,
            "nom": "Humitat relativa mínima",
            "unitat": "%",
            "acronim": "HRn",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 46,
            "nom": "Velocitat del vent a 2 m (esc.) ",
            "unitat": "m/s",
            "acronim": "VV2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 47,
            "nom": "Direcció del vent a 2 m (m. 1) ",
            "unitat": "°",
            "acronim": "DV2",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 48,
            "nom": "Velocitat del vent a 6 m (esc.)",
            "unitat": "m/s",
            "acronim": "VV6",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 49,
            "nom": "Direcció del vent a 6 m (m. 1)",
            "unitat": "°",
            "acronim": "DV6",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 50,
            "nom": "Ratxa màxima del vent a 10 m",
            "unitat": "m/s",
            "acronim": "VVx10",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 51,
            "nom": "Direcció de la ratxa màxima del vent a 10 m",
            "unitat": "°",
            "acronim": "DVVx10",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 53,
            "nom": "Ratxa màxima del vent a 6 m",
            "unitat": "m/s",
            "acronim": "VVx6",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 54,
            "nom": "Direcció de la ratxa màxima del vent a 6 m",
            "unitat": "°",
            "acronim": "DVVx6",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 56,
            "nom": "Ratxa màxima del vent a 2 m",
            "unitat": "m/s",
            "acronim": "VVx2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 57,
            "nom": "Direcció de la ratxa màxima del vent a 2 m",
            "unitat": "°",
            "acronim": "DVVx2",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 59,
            "nom": "Irradiància neta",
            "unitat": "W/m²",
            "acronim": "RN",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 60,
            "nom": "Temperatura de subsòl a 5 cm",
            "unitat": "°C",
            "acronim": "TSUB5",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 61,
            "nom": "Temperatura de subsòl a 50 cm",
            "unitat": "°C",
            "acronim": "TSUB50",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 62,
            "nom": "TDR a 10 cm",
            "unitat": "%(1)",
            "acronim": "TDR10",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 63,
            "nom": "TDR a 35 cm",
            "unitat": "%(1)",
            "acronim": "TDR35",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 64,
            "nom": "Humectació moll",
            "unitat": "%(1)",
            "acronim": "HMOLL",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 65,
            "nom": "Humectació sec",
            "unitat": "%(1)",
            "acronim": "HSEC",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 66,
            "nom": "Humectació res",
            "unitat": "Ohms",
            "acronim": "HRES",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 67,
            "nom": "Humectació moll 2",
            "unitat": "%(1)",
            "acronim": "HMOLL2",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 68,
            "nom": "Humectació sec 2",
            "unitat": "%(1)",
            "acronim": "HSEC2",
            "tipus": "DAT",
            "decimals": 2
          },
          {
            "codi": 69,
            "nom": "Humectació res 2",
            "unitat": "Ohms",
            "acronim": "HRES2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 70,
            "nom": "Precipitació acumulada",
            "unitat": "mm",
            "acronim": "PPTacu",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 71,
            "nom": "Bateria",
            "unitat": "V",
            "acronim": "BAT",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 72,
            "nom": "Precipitació màxima en 1 minut",
            "unitat": "mm",
            "acronim": "PPTx1min",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 74,
            "nom": "Humitat del combustible forestal 1",
            "unitat": "mV",
            "acronim": "HCF1",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 75,
            "nom": "Temperatura del combustible forestal  1",
            "unitat": "mV",
            "acronim": "TCF1",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 76,
            "nom": "Humitat del combustible forestal 2",
            "unitat": "mV",
            "acronim": "HCF2",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 77,
            "nom": "Temperatura del combustible forestal 2",
            "unitat": "mV",
            "acronim": "TCF2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 78,
            "nom": "Humitat del combustible forestal 3",
            "unitat": "%",
            "acronim": "HCF3",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 79,
            "nom": "Temperatura del combustible forestal 3",
            "unitat": "°C",
            "acronim": "TCF3",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 80,
            "nom": "Temperatura de la neu 1",
            "unitat": "°C",
            "acronim": "TNEU1",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 81,
            "nom": "Temperatura de la neu 2",
            "unitat": "°C",
            "acronim": "TNEU2",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 82,
            "nom": "Temperatura de la neu 3",
            "unitat": "°C",
            "acronim": "TNEU3",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 83,
            "nom": "Temperatura de la neu 4",
            "unitat": "°C",
            "acronim": "TNEU4",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 84,
            "nom": "Temperatura de la neu 5",
            "unitat": "°C",
            "acronim": "TNEU5",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 85,
            "nom": "Temperatura de la neu 6",
            "unitat": "°C",
            "acronim": "TNEU6",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 86,
            "nom": "Temperatura de la neu 7",
            "unitat": "°C",
            "acronim": "TNEU7",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 87,
            "nom": "Temperatura de la neu 8",
            "unitat": "°C",
            "acronim": "TNEU8",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 88,
            "nom": "Quality number",
            "unitat": "%(1)",
            "acronim": "QN",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 89,
            "nom": "Temperatura del datalogger",
            "unitat": "°C",
            "acronim": "TDLOG",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 90,
            "nom": "Altura màxima",
            "unitat": "cm",
            "acronim": "ALTx",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 91,
            "nom": "Període màxima",
            "unitat": "s",
            "acronim": "PERx",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 92,
            "nom": "Altura significant",
            "unitat": "cm",
            "acronim": "ALTsig",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 93,
            "nom": "Període significant",
            "unitat": "s",
            "acronim": "PERsig",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 94,
            "nom": "Altura mitjana",
            "unitat": "cm",
            "acronim": "ALTm",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 95,
            "nom": "Període mitjà",
            "unitat": "s",
            "acronim": "PERm",
            "tipus": "DAT",
            "decimals": 1
          },
          {
            "codi": 96,
            "nom": "Direcció del pic",
            "unitat": "°",
            "acronim": "DPIC",
            "tipus": "DAT",
            "decimals": 0
          },
          {
            "codi": 97,
            "nom": "Temperatura superficial del mar",
            "unitat": "°C",
            "acronim": "TMAR",
            "tipus": "DAT",
            "decimals": 1
          }
        ]


@pytest.fixture(scope='session')
def meteocat_variables_multivariate_metadata():
    return [
          {
            "codi": 6006,
            "nom": "Evapotranspiració de referència",
            "unitat": "mm",
            "acronim": "ETo",
            "tipus": "CMV",
            "decimals": 2
          }
        ]


@pytest.fixture(scope='session')
def meteocat_variables_auxiliary_metadata():
    return [
          {
            "codi": 900,
            "nom": "Precipitació acumulada en 10 min",
            "unitat": "mm",
            "acronim": "PPT10min",
            "tipus": "AUX",
            "decimals": 1
          },
          {
            "codi": 901,
            "nom": "Precipitació acumulada en 1 min",
            "unitat": "mm",
            "acronim": "PPT1min",
            "tipus": "AUX",
            "decimals": 1
          }
        ]