#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import meteocat_urls
from . import meteocat_api
from ..data_model.weather_station import WeatherStation
from ..data_model.variable import Variable
import json

from typing import List


def get_weather_stations(api_token: str) -> List[WeatherStation]:
    """
    Gets all the weather station data from the MeteoCat agency

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :type api_token: str
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    url = meteocat_urls.WEATHER_STATIONS
    response = meteocat_api.get_from_api(api_token, url)
    stations: List[WeatherStation] = list()
    if response.status_code == 200:
        stations = json.loads(response.text, object_hook=WeatherStation.object_hook)
    return stations


def get_variables_from_station(api_token: str, station: WeatherStation) -> List[Variable]:
    """
    Gets all the variables of a station data from the MeteoCat agency

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :type api_token: str
    :param station: Weather station to retrieve the variables from
    :type station: WeatherStation
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    # Get the measured variables
    url = meteocat_urls.STATION_MEASURED_VARIABLES.format(station.code)
    response = meteocat_api.get_from_api(api_token, url)
    measured_variables: List[Variable] = list()
    if response.status_code == 200:
        measured_variables = json.loads(response.text, object_hook=Variable.object_hook)
    url = meteocat_urls.STATION_AUXILIAR_VARIABLES.format(station.code)
    response = meteocat_api.get_from_api(api_token, url)
    auxiliar_variables: List[Variable] = list()
    if response.status_code == 200:
        auxiliar_variables = json.loads(response.text, object_hook=Variable.object_hook)
    url = meteocat_urls.STATION_MULTI_VARIABLES.format(station.code)
    response = meteocat_api.get_from_api(api_token, url)
    multi_variables: List[Variable] = list()
    if response.status_code == 200:
        multi_variables = json.loads(response.text, object_hook=Variable.object_hook)
    variables = measured_variables + auxiliar_variables + multi_variables
    if None in variables:
        return list()
    return variables
