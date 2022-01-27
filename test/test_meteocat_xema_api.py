#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytz

from src.gisfire_meteocat_lib.remote_api import meteocat_xema_api
from src.gisfire_meteocat_lib.remote_api import meteocat_urls
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStation
import datetime
import requests
import pytest

from typing import List


def test_weather_stations_01(requests_mock, weather_station_api_response):
    """
    Tests an exception to a lightning request

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    url = meteocat_urls.WEATHER_STATIONS
    requests_mock.get(url, exc=requests.exceptions.HTTPError)
    with pytest.raises(requests.exceptions.RequestException):
        _ = meteocat_xema_api.get_weather_stations('1234')


def test_weather_stations_02(requests_mock):
    """
    Tests a timeout exception to a lightning request

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    url = meteocat_urls.WEATHER_STATIONS
    requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
    with pytest.raises(requests.exceptions.RequestException):
        _ = meteocat_xema_api.get_weather_stations('1234')


def test_weather_station_03(requests_mock, weather_station_api_response):
    """
    Tests a correct lightning request and check both the returned lightnings and the LightningAPIRequest object

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param weather_station_api_response: Fixture that simulates the return data from a lightning request
    """
    url = meteocat_urls.WEATHER_STATIONS
    requests_mock.get(url, text=weather_station_api_response, status_code=200)
    stations = meteocat_xema_api.get_weather_stations('1234')
    print(stations)
    assert len(stations) == 6
    for station in stations:
        assert isinstance(station, WeatherStation)


def test_weather_station_04(requests_mock, meteocat_lightnings_meteocat_api_invalid_date):
    """
    Tests a response error

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_meteocat_api_invalid_date: Fixture that simulates the return data from a requests with
    an invalid date
    """
    url = meteocat_urls.WEATHER_STATIONS
    requests_mock.get(url, json=meteocat_lightnings_meteocat_api_invalid_date, status_code=500)
    stations = meteocat_xema_api.get_weather_stations('1234')
    assert stations == []
