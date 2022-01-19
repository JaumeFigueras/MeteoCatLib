#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.gisfire_meteocat_lib.classes.weather_station import WeatherStation
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationStatus
import pytest
import json
import datetime
import pytz


def test_json_parse_weather_station_status_01(weather_station_status_str_closed, weather_station_status_json_closed):
    state: WeatherStationStatus = json.loads(weather_station_status_str_closed,
                                             object_hook=WeatherStationStatus.object_hook)
    assert state.code.value == weather_station_status_json_closed['codi']
    assert state.from_date == datetime.datetime.strptime(weather_station_status_json_closed['dataInici'],
                                                         "%Y-%m-%dT%H:%M%z")
    assert state.to_date == datetime.datetime.strptime(weather_station_status_json_closed['dataFi'],
                                                       "%Y-%m-%dT%H:%M%z")


def test_json_parse_weather_station_status_02(weather_station_status_str_open, weather_station_status_json_open):
    state: WeatherStationStatus = json.loads(weather_station_status_str_open,
                                             object_hook=WeatherStationStatus.object_hook)
    assert state.code.value == weather_station_status_json_open['codi']
    assert state.from_date == datetime.datetime.strptime(weather_station_status_json_open['dataInici'],
                                                         "%Y-%m-%dT%H:%M%z")
    assert state.to_date == weather_station_status_json_open['dataFi']
    assert state.to_date is None
