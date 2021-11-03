#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VARIABLES_METADATA = 'https://api.meteo.cat/xema/v1/variables/mesurades/metadades'
MULTI_VARIABLES_METADATA = 'https://api.meteo.cat/xema/v1/variables/cmv/metadades'
AUXILIAR_VARIABLES_METADATA = 'https://api.meteo.cat/xema/v1/variables/auxiliars/metadades'
WEATHER_STATIONS = 'https://api.meteo.cat/xema/v1/estacions/metadades'
STATION_MEASURED_VARIABLES = 'https://api.meteo.cat/xema/v1/estacions/{0:}/variables/mesurades/metadades'
STATION_MULTI_VARIABLES = 'https://api.meteo.cat/xema/v1/estacions/{0:}/variables/cmv/metadades'
STATION_AUXILIAR_VARIABLES = 'https://api.meteo.cat/xema/v1/estacions/{0:}/variables/auxiliars/metadades'
STATION_MEASURED_DATA = 'https://api.meteo.cat/xema/v1/variables/mesurades/{0:}/{1:}/{2:}/{3:}?codiEstacio={4:}'
STATION_MULTI_DATA = 'https://api.meteo.cat/xema/v1/variables/cmv/{0:}/{1:}/{2:}/{3:}?codiEstacio={4:}'
STATION_AUXILIAR_DATA = 'https://api.meteo.cat/xema/v1/variables/auxiliars/{0:}/{1:}/{2:}/{3:}?codiEstacio={4:}'
