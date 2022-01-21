#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.gisfire_meteocat_lib.classes.weather_station import WeatherStation
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationCategory
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationState
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationStateCategory
import pytest
import json
import datetime
import pytz

from typing import Dict
from typing import Any


def test_json_parse_weather_station_status_01(weather_station_status_str_closed: str,
                                              weather_station_status_json_closed: Dict[str, Any]) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_status_str_closed: String fixture with the text of a state with both dates
    :type weather_station_status_str_closed: str
    :param weather_station_status_json_closed: Same string but json parser to compare with the result
    :type weather_station_status_json_closed: dict(str, *)
    """
    state: WeatherStationState = json.loads(weather_station_status_str_closed,
                                            object_hook=WeatherStationState.object_hook)
    assert state.code.value == weather_station_status_json_closed['codi']
    assert state.from_date == datetime.datetime.strptime(weather_station_status_json_closed['dataInici'],
                                                         "%Y-%m-%dT%H:%M%z")
    assert state.to_date == datetime.datetime.strptime(weather_station_status_json_closed['dataFi'],
                                                       "%Y-%m-%dT%H:%M%z")


def test_json_parse_weather_station_status_02(weather_station_status_str_open, weather_station_status_json_open):
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_status_str_open: String fixture with the text of a state with just the first date
    :type weather_station_status_str_open: str
    :param weather_station_status_json_open: Same string but json parser to compare with the result
    :type weather_station_status_json_open: dict(str, *)
    """
    state: WeatherStationState = json.loads(weather_station_status_str_open,
                                            object_hook=WeatherStationState.object_hook)
    assert state.code.value == weather_station_status_json_open['codi']
    assert state.from_date == datetime.datetime.strptime(weather_station_status_json_open['dataInici'],
                                                         "%Y-%m-%dT%H:%M%z")
    assert state.to_date == weather_station_status_json_open['dataFi']
    assert state.to_date is None


def test_json_parse_weather_station_status_03(weather_station_status_str_error_from_date):
    """
    Test parsing a string to JSON of a weather station status with an error in the first date

    :param weather_station_status_str_error_from_date: String fixture with the text of a state with error in the first date
    :type weather_station_status_str_error_from_date: str
    """
    with pytest.raises(ValueError):
        state: WeatherStationState = json.loads(weather_station_status_str_error_from_date,
                                                object_hook=WeatherStationState.object_hook)


def test_json_parse_weather_station_status_04(weather_station_status_str_error_to_date):
    """
    Test parsing a string to JSON of a weather station status with an error in the first date

    :param weather_station_status_str_error_to_date: String fixture with the text of a state with error in the first date
    :type weather_station_status_str_error_to_date: str
    """
    with pytest.raises(ValueError):
        state: WeatherStationState = json.loads(weather_station_status_str_error_to_date,
                                                object_hook=WeatherStationState.object_hook)


def test_json_encode_weather_station_status_01():
    state = WeatherStationState(WeatherStationStateCategory.ACTIVE,
                                datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    string = '{"code": 2, "from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}'
    assert json.loads(string) == json.loads(json.dumps(state, cls=WeatherStationState.JSONEncoder))


def test_json_encode_weather_station_status_02():
    state = WeatherStationState(WeatherStationStateCategory.DISMANTLED,
                                datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC), None)
    string = '{"code": 1, "from_date": "2020-01-01T10:30Z", "to_date": null}'
    assert json.loads(string) == json.loads(json.dumps(state, cls=WeatherStationState.JSONEncoder))


def test_json_parse_weather_station_01(weather_station_str: str, weather_station_json: Dict[str, Any]) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_str: String fixture with the text of a state with both dates
    :type weather_station_str: str
    :param weather_station_json: Same string but json parser to compare with the result
    :type weather_station_json: dict(str, *)
    """
    station: WeatherStation = json.loads(weather_station_str, object_hook=WeatherStation.object_hook)
    assert station.code == weather_station_json['codi']
    assert station.name == weather_station_json['nom']
    assert station.category == WeatherStationCategory.AUTO if weather_station_json['tipus'] == 'A' \
        else WeatherStationCategory.OTHER
    assert station.placement == weather_station_json['emplacament']
    assert station.altitude == float(weather_station_json['altitud'])
    assert station._coordinates_latitude == float(weather_station_json['coordenades']['latitud'])
    assert station._coordinates_longitude == float(weather_station_json['coordenades']['longitud'])
    assert station.municipality_code == int(weather_station_json['municipi']['codi'])
    assert station.municipality_name == str(weather_station_json['municipi']['nom'])
    assert station.county_code == int(weather_station_json['comarca']['codi'])
    assert station.county_name == weather_station_json['comarca']['nom']
    assert station.province_code == int(weather_station_json['provincia']['codi'])
    assert station.province_name == weather_station_json['provincia']['nom']
    assert station.network_code == int(weather_station_json['xarxa']['codi'])
    assert station.network_name == weather_station_json['xarxa']['nom']
    assert len(station.states) == len(weather_station_json['estats'])
    for idx in range(len(weather_station_json['estats'])):
        elem: WeatherStationState = station.states[idx]
        assert elem.code.value == weather_station_json['estats'][idx]['codi']
        assert elem.from_date == datetime.datetime.strptime(weather_station_json['estats'][idx]['dataInici'],
                                                            "%Y-%m-%dT%H:%M%z")
        if weather_station_json['estats'][idx]['dataFi'] is None:
            assert elem.to_date is None
        else:
            assert elem.to_date == datetime.datetime.strptime(weather_station_json['estats'][idx]['dataFi'],
                                                              "%Y-%m-%dT%H:%M%z")


def test_json_parse_weather_station_02(weather_station_str_incomplete: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_str_incomplete: String fixture with the text of a state with both dates
    :type weather_station_str_incomplete: str
    """
    assert json.loads(weather_station_str_incomplete, object_hook=WeatherStation.object_hook) is None


def test_json_encode_weather_station_01():
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    string = ('{"code": "VL", "name": "Seròs - la Creu", "category": 0, '
              '"placement": "Crta. de Seròs a la Granja d\'Escarp", "altitude": 100, "coordinates_latitude": 41.46014, '
              '"coordinates_longitude": 0.40562, "coordinates_epsg": 4258, "municipality_code": 252043, '
              '"municipality_name": "Seròs", "county_code": 33, "county_name": "Segrià", "province_code": 25, '
              '"province_name": "Lleida", "network_code": 1, "network_name": "XEMA", "states": []}')
    assert json.loads(string) == json.loads(json.dumps(station, cls=WeatherStation.JSONEncoder, ensure_ascii=False))


def test_geojson_encode_weather_station_01():
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    string = ('{"type": "Feature", "id": null, "crs": {"type": "link", '
              '"properties": {"href": "https://spatialreference.org/ref/epsg/4258/proj4/", "type": "proj4"}}, '
              '"geometry": {"type": "Point", "coordinates": [0.40562, 41.46014]}, "properties": {'
              '"code": "VL", "name": "Seròs - la Creu", "category": 0, '
              '"placement": "Crta. de Seròs a la Granja d\'Escarp", "altitude": 100, "coordinates_latitude": 41.46014, '
              '"coordinates_longitude": 0.40562, "coordinates_epsg": 4258, "municipality_code": 252043, '
              '"municipality_name": "Seròs", "county_code": 33, "county_name": "Segrià", "province_code": 25, '
              '"province_name": "Lleida", "network_code": 1, "network_name": "XEMA", "states": []}}')
    assert json.loads(string) == json.loads(json.dumps(station, cls=WeatherStation.GeoJSONEncoder, ensure_ascii=False))


def test_latitude_and_longitude_getter_weather_station_01():
    """
    Test the weather station location getters

    :return: None
    """
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    assert station.lat == 41.46014
    assert station.lon == 0.40562
    assert station.geom == 'SRID=4258;POINT(0.40562 41.46014)'


def test_latitude_setter_weather_station_01():
    """
    Test the weather station lat property setter with a value higher than the upper bound

    :return: None
    """
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    with pytest.raises(ValueError):
        station.lat = 123
    with pytest.raises(ValueError):
        station.lat = -123
    station.lat = -34
    assert station._coordinates_latitude == -34
    assert station.geom == "SRID={0:};POINT(0.40562 -34)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station.lat = 19
    assert station._coordinates_latitude == 19
    assert station.geom == "SRID={0:};POINT(0.40562 19)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station = WeatherStation()
    station.lat = -34
    assert station._coordinates_latitude == -34
    assert station.geom is None
    station.lat = 19
    assert station._coordinates_latitude == 19
    assert station.geom is None


def test_longitude_setter_weather_station_01():
    """
    Test the weather station lat property setter with a value higher than the upper bound

    :return: None
    """
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    with pytest.raises(ValueError):
        station.lon = 1234
    with pytest.raises(ValueError):
        station.lon = -1234
    station.lon = -34
    assert station._coordinates_longitude == -34
    assert station.geom == "SRID={0:};POINT(-34 41.46014)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station.lon = 19
    assert station._coordinates_longitude == 19
    assert station.geom == "SRID={0:};POINT(19 41.46014)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station = WeatherStation()
    station.lon = -34
    assert station._coordinates_longitude == -34
    assert station.geom is None
    station.lon = 19
    assert station._coordinates_longitude == 19
    assert station.geom is None

