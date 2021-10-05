import pytest
import json


@pytest.fixture(scope='session')
def meteocat_comarques():
    return [
      {
        "codi": 5,
        "nom": "Alta Ribagorça"
      },
      {
        "codi": 1,
        "nom": "Alt Camp"
      },
      {
        "codi": 2,
        "nom": "Alt Empordà"
      },
      {
        "codi": 3,
        "nom": "Alt Penedès"
      },
      {
        "codi": 4,
        "nom": "Alt Urgell"
      },
      {
        "codi": 6,
        "nom": "Anoia"
      },
      {
        "codi": 7,
        "nom": "Bages"
      },
      {
        "codi": 8,
        "nom": "Baix Camp"
      },
      {
        "codi": 9,
        "nom": "Baix Ebre"
      },
      {
        "codi": 10,
        "nom": "Baix Empordà"
      },
      {
        "codi": 11,
        "nom": "Baix Llobregat"
      },
      {
        "codi": 12,
        "nom": "Baix Penedès"
      },
      {
        "codi": 13,
        "nom": "Barcelonès"
      },
      {
        "codi": 14,
        "nom": "Berguedà"
      },
      {
        "codi": 15,
        "nom": "Cerdanya"
      },
      {
        "codi": 16,
        "nom": "Conca de Barberà"
      },
      {
        "codi": 17,
        "nom": "Garraf"
      },
      {
        "codi": 18,
        "nom": "Garrigues"
      },
      {
        "codi": 19,
        "nom": "Garrotxa"
      },
      {
        "codi": 20,
        "nom": "Gironès"
      },
      {
        "codi": 21,
        "nom": "Maresme"
      },
      {
        "codi": 42,
        "nom": "Moianès"
      },
      {
        "codi": 22,
        "nom": "Montsià"
      },
      {
        "codi": 23,
        "nom": "Noguera"
      },
      {
        "codi": 24,
        "nom": "Osona"
      },
      {
        "codi": 25,
        "nom": "Pallars Jussà"
      },
      {
        "codi": 26,
        "nom": "Pallars Sobirà"
      },
      {
        "codi": 28,
        "nom": "Pla de l'Estany"
      },
      {
        "codi": 27,
        "nom": "Pla d'Urgell"
      },
      {
        "codi": 29,
        "nom": "Priorat"
      },
      {
        "codi": 30,
        "nom": "Ribera d'Ebre"
      },
      {
        "codi": 31,
        "nom": "Ripollès"
      },
      {
        "codi": 32,
        "nom": "Segarra"
      },
      {
        "codi": 33,
        "nom": "Segrià"
      },
      {
        "codi": 34,
        "nom": "Selva"
      },
      {
        "codi": 35,
        "nom": "Solsonès"
      },
      {
        "codi": 36,
        "nom": "Tarragonès"
      },
      {
        "codi": 37,
        "nom": "Terra Alta"
      },
      {
        "codi": 38,
        "nom": "Urgell"
      },
      {
        "codi": 39,
        "nom": "Val d'Aran"
      },
      {
        "codi": 40,
        "nom": "Vallès Occidental"
      },
      {
        "codi": 41,
        "nom": "Vallès Oriental"
      }
    ]


@pytest.fixture(scope='session')
def meteocat_municipis():
    return json.loads("""[
      {
        "codi": "250019",
        "nom": "Abella de la Conca",
        "coordenades": {
          "latitud": 42.16130365400063,
          "longitud": 1.0917273756684127
        },
        "comarca": {
          "codi": 25,
          "nom": "Pallars Jussà"
        },
        "slug": null
      },
      {
        "codi": "080018",
        "nom": "Abrera",
        "coordenades": {
          "latitud": 41.51628633379985,
          "longitud": 1.902257195719771
        },
        "comarca": {
          "codi": 11,
          "nom": "Baix Llobregat"
        },
        "slug": null
      },
      {
        "codi": "250024",
        "nom": "Àger",
        "coordenades": {
          "latitud": 41.999231791502844,
          "longitud": 0.763564345690738
        },
        "comarca": {
          "codi": 23,
          "nom": "Noguera"
        },
        "slug": null
      },
      {
        "codi": "250030",
        "nom": "Agramunt",
        "coordenades": {
          "latitud": 41.78699058745335,
          "longitud": 1.09866060681363
        },
        "comarca": {
          "codi": 38,
          "nom": "Urgell"
        },
        "slug": null
      },
      {
        "codi": "080023",
        "nom": "Aguilar de Segarra",
        "coordenades": {
          "latitud": 41.73895349929133,
          "longitud": 1.630983141363597
        },
        "comarca": {
          "codi": 7,
          "nom": "Bages"
        },
        "slug": null
      },
      {
        "codi": "170010",
        "nom": "Agullana",
        "coordenades": {
          "latitud": 42.39412190155473,
          "longitud": 2.8463858365780417
        },
        "comarca": {
          "codi": 2,
          "nom": "Alt Empordà"
        },
        "slug": null
      },
      {
        "codi": "080142",
        "nom": "Aiguafreda",
        "coordenades": {
          "latitud": 41.76851326657006,
          "longitud": 2.2501486011278455
        },
        "comarca": {
          "codi": 41,
          "nom": "Vallès Oriental"
        },
        "slug": null
      },
      {
        "codi": "430017",
        "nom": "Aiguamúrcia",
        "coordenades": {
          "latitud": 41.34657835850532,
          "longitud": 1.3631313155952232
        },
        "comarca": {
          "codi": 1,
          "nom": "Alt Camp"
        },
        "slug": null
      },
      {
        "codi": "170025",
        "nom": "Aiguaviva",
        "coordenades": {
          "latitud": 41.93811503730425,
          "longitud": 2.762381184991045
        },
        "comarca": {
          "codi": 20,
          "nom": "Gironès"
        },
        "slug": null
      },
      {
        "codi": "250387",
        "nom": "Aitona",
        "coordenades": {
          "latitud": 41.49463067702478,
          "longitud": 0.4590185912191394
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250058",
        "nom": "Alàs i Cerc",
        "coordenades": {
          "latitud": 42.35164679089833,
          "longitud": 1.508187537292697
        },
        "comarca": {
          "codi": 4,
          "nom": "Alt Urgell"
        },
        "slug": null
      },
      {
        "codi": "170031",
        "nom": "Albanyà",
        "coordenades": {
          "latitud": 42.30477094086333,
          "longitud": 2.720110496343058
        },
        "comarca": {
          "codi": 2,
          "nom": "Alt Empordà"
        },
        "slug": null
      },
      {
        "codi": "250077",
        "nom": "Albatàrrec",
        "coordenades": {
          "latitud": 41.573098884033406,
          "longitud": 0.6054088776126012
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250083",
        "nom": "Albesa",
        "coordenades": {
          "latitud": 41.750734677657455,
          "longitud": 0.6595162234684376
        },
        "comarca": {
          "codi": 23,
          "nom": "Noguera"
        },
        "slug": null
      },
      {
        "codi": "430022",
        "nom": "Albinyana",
        "coordenades": {
          "latitud": 41.24566162778187,
          "longitud": 1.4862112736334072
        },
        "comarca": {
          "codi": 12,
          "nom": "Baix Penedès"
        },
        "slug": null
      },
      {
        "codi": "170046",
        "nom": "Albons",
        "coordenades": {
          "latitud": 42.1042749334684,
          "longitud": 3.0852015493001246
        },
        "comarca": {
          "codi": 10,
          "nom": "Baix Empordà"
        },
        "slug": null
      },
      {
        "codi": "430043",
        "nom": "Alcanar",
        "coordenades": {
          "latitud": 40.542895074496755,
          "longitud": 0.48201159249355163
        },
        "comarca": {
          "codi": 22,
          "nom": "Montsià"
        },
        "slug": null
      },
      {
        "codi": "250100",
        "nom": "Alcanó",
        "coordenades": {
          "latitud": 41.48047029935448,
          "longitud": 0.6171786659912544
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250117",
        "nom": "Alcarràs",
        "coordenades": {
          "latitud": 41.562893521217354,
          "longitud": 0.52435211814106
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250122",
        "nom": "Alcoletge",
        "coordenades": {
          "latitud": 41.64703015529643,
          "longitud": 0.6942872085642158
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "430056",
        "nom": "Alcover",
        "coordenades": {
          "latitud": 41.26265893136212,
          "longitud": 1.1702353264895855
        },
        "comarca": {
          "codi": 1,
          "nom": "Alt Camp"
        },
        "slug": null
      },
      {
        "codi": "430069",
        "nom": "Aldover",
        "coordenades": {
          "latitud": 40.87981922005625,
          "longitud": 0.5000448943288871
        },
        "comarca": {
          "codi": 9,
          "nom": "Baix Ebre"
        },
        "slug": null
      },
      {
        "codi": "080039",
        "nom": "Alella",
        "coordenades": {
          "latitud": 41.49387101370757,
          "longitud": 2.2951601232142504
        },
        "comarca": {
          "codi": 21,
          "nom": "Maresme"
        },
        "slug": null
      },
      {
        "codi": "430081",
        "nom": "Alfara de Carles",
        "coordenades": {
          "latitud": 40.87378475877814,
          "longitud": 0.400301375187861
        },
        "comarca": {
          "codi": 9,
          "nom": "Baix Ebre"
        },
        "slug": null
      },
      {
        "codi": "250138",
        "nom": "Alfarràs",
        "coordenades": {
          "latitud": 41.83000987817036,
          "longitud": 0.5696871624872141
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250143",
        "nom": "Alfés",
        "coordenades": {
          "latitud": 41.5214386503461,
          "longitud": 0.6193722238771672
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "430094",
        "nom": "Alforja",
        "coordenades": {
          "latitud": 41.2104813720337,
          "longitud": 0.9753075732189862
        },
        "comarca": {
          "codi": 8,
          "nom": "Baix Camp"
        },
        "slug": null
      },
      {
        "codi": "250156",
        "nom": "Algerri",
        "coordenades": {
          "latitud": 41.81582483177015,
          "longitud": 0.6385194207287183
        },
        "comarca": {
          "codi": 23,
          "nom": "Noguera"
        },
        "slug": null
      },
      {
        "codi": "250169",
        "nom": "Alguaire",
        "coordenades": {
          "latitud": 41.736202080035305,
          "longitud": 0.5837723854924972
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250175",
        "nom": "Alins",
        "coordenades": {
          "latitud": 42.548721903960065,
          "longitud": 1.3186796470051314
        },
        "comarca": {
          "codi": 26,
          "nom": "Pallars Sobirà"
        },
        "slug": null
      },
      {
        "codi": "430108",
        "nom": "Alió",
        "coordenades": {
          "latitud": 41.295153696867374,
          "longitud": 1.3064263694316864
        },
        "comarca": {
          "codi": 1,
          "nom": "Alt Camp"
        },
        "slug": null
      },
      {
        "codi": "250194",
        "nom": "Almacelles",
        "coordenades": {
          "latitud": 41.73159947444427,
          "longitud": 0.4367653304405636
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      },
      {
        "codi": "250208",
        "nom": "Almatret",
        "coordenades": {
          "latitud": 41.30558777832295,
          "longitud": 0.4236196039291015
        },
        "comarca": {
          "codi": 33,
          "nom": "Segrià"
        },
        "slug": null
      }
    ]""")


