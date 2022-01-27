#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import meteocat_urls
from . import meteocat_api
from ..classes.weather_station import WeatherStation
from ..classes.weather_station import WeatherStationState
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



