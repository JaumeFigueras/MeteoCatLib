import pytest
import json


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


@pytest.fixture(scope='session')
def meteocat_stations_metadata():
    return json.loads(""" [
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
          },
          {
            "codi": "CF",
            "nom": "Lloret de Mar",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.72346,
              "longitud": 2.84282
            },
            "emplacament": "Abocador municipal",
            "altitud": 63.3,
            "municipi": {
              "codi": "170950",
              "nom": "Lloret de Mar"
            },
            "comarca": {
              "codi": 34,
              "nom": "Selva"
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
                "dataInici": "1996-02-05T12:00Z",
                "dataFi": "2003-06-16T09:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2003-06-16T09:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CG",
            "nom": "Molló - Fabert",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.37717,
              "longitud": 2.41456
            },
            "emplacament": "Veïnat de Fabert",
            "altitud": 1405,
            "municipi": {
              "codi": "171077",
              "nom": "Molló"
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
                "dataInici": "1996-06-06T14:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CH",
            "nom": "Falset - Escola",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.15076,
              "longitud": 0.82357
            },
            "emplacament": "Col·legi Públic Antoni Vilanova",
            "altitud": 350,
            "municipi": {
              "codi": "430555",
              "nom": "Falset"
            },
            "comarca": {
              "codi": 29,
              "nom": "Priorat"
            },
            "provincia": {
              "codi": 43,
              "nom": "Tarragona"
            },
            "xarxa": {
              "codi": 1,
              "nom": "XEMA"
            },
            "estats": [
              {
                "codi": 2,
                "dataInici": "1995-12-01T02:00Z",
                "dataFi": "2005-07-05T16:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2005-07-05T16:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CI",
            "nom": "Sant Pau de Segúries",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.25839,
              "longitud": 2.36429
            },
            "emplacament": "Estació meteorològica municipal",
            "altitud": 852,
            "municipi": {
              "codi": "171772",
              "nom": "Sant Pau de Segúries"
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
                "dataInici": "1995-11-24T15:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CJ",
            "nom": "Organyà",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.21624,
              "longitud": 1.33132
            },
            "emplacament": "Càmping municipal",
            "altitud": 566.5,
            "municipi": {
              "codi": "251556",
              "nom": "Organyà"
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
                "dataInici": "1996-01-16T10:30Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CK",
            "nom": "Santa Coloma de Farners",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.86472,
              "longitud": 2.66451
            },
            "emplacament": "Dipòsit d'aigua",
            "altitud": 163,
            "municipi": {
              "codi": "171805",
              "nom": "Santa Coloma de Farners"
            },
            "comarca": {
              "codi": 34,
              "nom": "Selva"
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
                "dataInici": "1996-02-05T17:30Z",
                "dataFi": "2004-06-08T09:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2004-06-08T09:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CL",
            "nom": "Sant Salvador de Guardiola",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.67399,
              "longitud": 1.76796
            },
            "emplacament": "Urbanització Miralda",
            "altitud": 349,
            "municipi": {
              "codi": "080983",
              "nom": "Sant Salvador de Guardiola"
            },
            "comarca": {
              "codi": 7,
              "nom": "Bages"
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
                "dataInici": "1996-02-02T11:30Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CM",
            "nom": "Montmeló",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.54911,
              "longitud": 2.24546
            },
            "emplacament": "Torreta de Can Campanyà",
            "altitud": 75.2,
            "municipi": {
              "codi": "081350",
              "nom": "Montmeló"
            },
            "comarca": {
              "codi": 41,
              "nom": "Vallès Oriental"
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
                "dataInici": "1996-01-23T19:30Z",
                "dataFi": "2006-03-22T09:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2006-03-22T09:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CN",
            "nom": "Guardiola de Berguedà - Escola",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.22903,
              "longitud": 1.87672
            },
            "emplacament": "Centre d'Assistència Primària",
            "altitud": 719.8,
            "municipi": {
              "codi": "080996",
              "nom": "Guardiola de Berguedà"
            },
            "comarca": {
              "codi": 14,
              "nom": "Berguedà"
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
                "dataInici": "1996-02-20T11:00Z",
                "dataFi": "2005-03-21T10:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2005-03-21T10:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CO",
            "nom": "Torres de Segre - Depuradora",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.52603,
              "longitud": 0.52711
            },
            "emplacament": "Depuradora municipal",
            "altitud": 143.6,
            "municipi": {
              "codi": "252326",
              "nom": "Torres de Segre"
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
                "dataInici": "1995-11-23T17:00Z",
                "dataFi": "2006-05-25T10:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2006-05-25T10:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CP",
            "nom": "Sant Romà d'Abella",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.13924,
              "longitud": 1.03893
            },
            "emplacament": "Sant Romà d'Abella - el Tossal",
            "altitud": 690,
            "municipi": {
              "codi": "251155",
              "nom": "Isona i Conca Dellà"
            },
            "comarca": {
              "codi": 25,
              "nom": "Pallars Jussà"
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
                "dataInici": "1996-05-20T14:30Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CQ",
            "nom": "Vilanova de Meià",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.99546,
              "longitud": 1.02569
            },
            "emplacament": "Camp de fútbol",
            "altitud": 594,
            "municipi": {
              "codi": "252509",
              "nom": "Vilanova de Meià"
            },
            "comarca": {
              "codi": 23,
              "nom": "Noguera"
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
                "dataInici": "1996-04-01T11:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CR",
            "nom": "la Quar",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.08032,
              "longitud": 1.9624
            },
            "emplacament": "Sant Maurici",
            "altitud": 873,
            "municipi": {
              "codi": "081770",
              "nom": "La Quar"
            },
            "comarca": {
              "codi": 14,
              "nom": "Berguedà"
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
                "dataInici": "1996-03-13T11:30Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CS",
            "nom": "Viladrau - centre",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.84502,
              "longitud": 2.3881
            },
            "emplacament": "Mas del Torrent",
            "altitud": 777,
            "municipi": {
              "codi": "172207",
              "nom": "Viladrau"
            },
            "comarca": {
              "codi": 24,
              "nom": "Osona"
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
                "dataInici": "1995-12-05T10:30Z",
                "dataFi": "2004-06-08T14:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2004-06-08T14:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CT",
            "nom": "el Pont de Suert",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.39811,
              "longitud": 0.74362
            },
            "emplacament": "Depuradora municipal",
            "altitud": 823,
            "municipi": {
              "codi": "251734",
              "nom": "El Pont de Suert"
            },
            "comarca": {
              "codi": 5,
              "nom": "Alta Ribagorça"
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
                "dataInici": "1996-02-14T14:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CV",
            "nom": "la Pobla de Segur - Bombers",
            "tipus": "A",
            "coordenades": {
              "latitud": 42.23939,
              "longitud": 0.96434
            },
            "emplacament": "Parc de Bombers",
            "altitud": 513.3,
            "municipi": {
              "codi": "251713",
              "nom": "La Pobla de Segur"
            },
            "comarca": {
              "codi": 25,
              "nom": "Pallars Jussà"
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
                "dataInici": "1995-12-22T16:00Z",
                "dataFi": "2016-11-18T14:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2016-11-18T14:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CW",
            "nom": "l'Espluga de Francolí",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.39241,
              "longitud": 1.09894
            },
            "emplacament": "Urb. Espluga Parc",
            "altitud": 446,
            "municipi": {
              "codi": "430542",
              "nom": "L'Espluga de Francolí"
            },
            "comarca": {
              "codi": 16,
              "nom": "Conca de Barberà"
            },
            "provincia": {
              "codi": 43,
              "nom": "Tarragona"
            },
            "xarxa": {
              "codi": 1,
              "nom": "XEMA"
            },
            "estats": [
              {
                "codi": 2,
                "dataInici": "1996-02-23T21:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CX",
            "nom": "Vic - 1",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.93582,
              "longitud": 2.23857
            },
            "emplacament": "Estadi d'atletisme",
            "altitud": 497.8,
            "municipi": {
              "codi": "082981",
              "nom": "Vic"
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
                "dataInici": "1996-01-18T14:30Z",
                "dataFi": "2003-01-01T00:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2003-01-01T00:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CY",
            "nom": "Muntanyola",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.87813,
              "longitud": 2.17873
            },
            "emplacament": "Esglèsia de St. Quirze i Sta. Julita",
            "altitud": 816,
            "municipi": {
              "codi": "081290",
              "nom": "Muntanyola"
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
                "dataInici": "1996-01-12T12:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "CZ",
            "nom": "Ulldemolins - Zona Esportiva",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.3191,
              "longitud": 0.87868
            },
            "emplacament": "Poliesportiu municipal",
            "altitud": 631,
            "municipi": {
              "codi": "431573",
              "nom": "Ulldemolins"
            },
            "comarca": {
              "codi": 29,
              "nom": "Priorat"
            },
            "provincia": {
              "codi": 43,
              "nom": "Tarragona"
            },
            "xarxa": {
              "codi": 1,
              "nom": "XEMA"
            },
            "estats": [
              {
                "codi": 2,
                "dataInici": "1996-03-04T10:30Z",
                "dataFi": "2008-04-15T09:00Z"
              },
              {
                "codi": 1,
                "dataInici": "2008-04-15T09:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "C6",
            "nom": "Castellnou de Seana",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.6566,
              "longitud": 0.95172
            },
            "emplacament": "Abocador comarcal",
            "altitud": 264,
            "municipi": {
              "codi": "250680",
              "nom": "Castellnou de Seana"
            },
            "comarca": {
              "codi": 27,
              "nom": "Pla d'Urgell"
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
                "dataInici": "1995-12-16T23:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "C7",
            "nom": "Tàrrega",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.66695,
              "longitud": 1.16234
            },
            "emplacament": "Abocador comarcal",
            "altitud": 427,
            "municipi": {
              "codi": "252173",
              "nom": "Tàrrega"
            },
            "comarca": {
              "codi": 38,
              "nom": "Urgell"
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
                "dataInici": "1995-11-06T18:00Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "C8",
            "nom": "Cervera",
            "tipus": "A",
            "coordenades": {
              "latitud": 41.67555,
              "longitud": 1.29609
            },
            "emplacament": "Abocador comarcal",
            "altitud": 554,
            "municipi": {
              "codi": "250729",
              "nom": "Cervera"
            },
            "comarca": {
              "codi": 32,
              "nom": "Segarra"
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
                "dataInici": "1995-10-27T10:30Z",
                "dataFi": null
              }
            ]
          },
          {
            "codi": "C9",
            "nom": "Mas de Barberans",
            "tipus": "A",
            "coordenades": {
              "latitud": 40.71825,
              "longitud": 0.39988
            },
            "emplacament": "Abocador comarcal",
            "altitud": 240,
            "municipi": {
              "codi": "430770",
              "nom": "Mas de Barberans"
            },
            "comarca": {
              "codi": 22,
              "nom": "Montsià"
            },
            "provincia": {
              "codi": 43,
              "nom": "Tarragona"
            },
            "xarxa": {
              "codi": 1,
              "nom": "XEMA"
            },
            "estats": [
              {
                "codi": 2,
                "dataInici": "1997-04-11T11:30Z",
                "dataFi": null
              }
            ]
          }
        ]""")
