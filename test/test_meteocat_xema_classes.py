#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.gisfire_meteocat_lib.classes.weather_station import WeatherStation
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationCategory
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationState
from src.gisfire_meteocat_lib.classes.weather_station import WeatherStationStateCategory
from src.gisfire_meteocat_lib.classes.variable import Variable
from src.gisfire_meteocat_lib.classes.variable import VariableCategory
from src.gisfire_meteocat_lib.classes.variable import VariableState
from src.gisfire_meteocat_lib.classes.variable import VariableStateCategory
from src.gisfire_meteocat_lib.classes.variable import VariableTimeBase
from src.gisfire_meteocat_lib.classes.variable import VariableTimeBaseCategory
from src.gisfire_meteocat_lib.classes.measure import Measure
from src.gisfire_meteocat_lib.classes.measure import MeasureValidityCategory
from src.gisfire_meteocat_lib.classes.measure import MeasureTimeBaseCategory

import pytest
import json
import datetime
import pytz

from typing import Dict
from typing import List
from typing import Any


def test_json_parse_weather_station_status_01(weather_station_status_str_closed: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_status_str_closed: String fixture with the text of a state with both dates
    :type weather_station_status_str_closed: str
    """
    state: WeatherStationState = json.loads(weather_station_status_str_closed,
                                            object_hook=WeatherStationState.object_hook)
    raw: Dict[str, Any] = json.loads(weather_station_status_str_closed)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == datetime.datetime.strptime(raw['dataFi'], "%Y-%m-%dT%H:%M%z")


def test_json_parse_weather_station_status_02(weather_station_status_str_open: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_status_str_open: String fixture with the text of a state with just the first date
    :type weather_station_status_str_open: str
    """
    state: WeatherStationState = json.loads(weather_station_status_str_open,
                                            object_hook=WeatherStationState.object_hook)
    raw: Dict[str, Any] = json.loads(weather_station_status_str_open)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == raw['dataFi'] and state.to_date is None and raw['dataFi'] is None


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


def test_json_parse_weather_station_01(weather_station_str: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param weather_station_str: String fixture with the text of a state with both dates
    :type weather_station_str: str
    """
    station: WeatherStation = json.loads(weather_station_str, object_hook=WeatherStation.object_hook)
    weather_station_json: Dict[str, Any] = json.loads(weather_station_str)
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


def test_geojson_encode_weather_station_02():
    # noinspection DuplicatedCode
    state = WeatherStationState(code=WeatherStationStateCategory.ACTIVE,
                                from_date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC))
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    station.states.append(state)
    string = ('{"type": "Feature", "id": null, "crs": {"type": "link", '
              '"properties": {"href": "https://spatialreference.org/ref/epsg/4258/proj4/", "type": "proj4"}}, '
              '"geometry": {"type": "Point", "coordinates": [0.40562, 41.46014]}, "properties": {'
              '"code": "VL", "name": "Seròs - la Creu", "category": 0, '
              '"placement": "Crta. de Seròs a la Granja d\'Escarp", "altitude": 100, "coordinates_latitude": 41.46014, '
              '"coordinates_longitude": 0.40562, "coordinates_epsg": 4258, "municipality_code": 252043, '
              '"municipality_name": "Seròs", "county_code": 33, "county_name": "Segrià", "province_code": 25, '
              '"province_name": "Lleida", "network_code": 1, "network_name": "XEMA", "states": [{'
              '"code": 2, "from_date":"2020-01-01T10:30Z", "to_date": null'
              '}]}}')
    assert json.loads(string) == json.loads(json.dumps(station, cls=WeatherStation.GeoJSONEncoder, ensure_ascii=False))


def test_geojson_encode_weather_station_03():
    state_01 = WeatherStationState(code=WeatherStationStateCategory.REPAIR,
                                   from_date=datetime.datetime(2018, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                   to_date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC))
    # noinspection DuplicatedCode
    state_02 = WeatherStationState(code=WeatherStationStateCategory.ACTIVE,
                                   from_date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC))
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    station.states.append(state_01)
    station.states.append(state_02)
    string = ('{"type": "Feature", "id": null, "crs": {"type": "link", '
              '"properties": {"href": "https://spatialreference.org/ref/epsg/4258/proj4/", "type": "proj4"}}, '
              '"geometry": {"type": "Point", "coordinates": [0.40562, 41.46014]}, "properties": {'
              '"code": "VL", "name": "Seròs - la Creu", "category": 0, '
              '"placement": "Crta. de Seròs a la Granja d\'Escarp", "altitude": 100, "coordinates_latitude": 41.46014, '
              '"coordinates_longitude": 0.40562, "coordinates_epsg": 4258, "municipality_code": 252043, '
              '"municipality_name": "Seròs", "county_code": 33, "county_name": "Segrià", "province_code": 25, '
              '"province_name": "Lleida", "network_code": 1, "network_name": "XEMA", "states": [{'
              '"code": 3, "from_date": "2018-01-01T10:30Z", "to_date": "2020-01-01T10:30Z"'
              '},{'
              '"code": 2, "from_date":"2020-01-01T10:30Z", "to_date": null'
              '}]}}')
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
    assert station.postgis_geometry == 'SRID=4258;POINT(0.40562 41.46014)'


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
    assert station.postgis_geometry == "SRID={0:};POINT(0.40562 -34)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station.lat = 19
    assert station._coordinates_latitude == 19
    assert station.postgis_geometry == "SRID={0:};POINT(0.40562 19)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station = WeatherStation()
    station.lat = -34
    assert station._coordinates_latitude == -34
    assert station.postgis_geometry is None
    station.lat = 19
    assert station._coordinates_latitude == 19
    assert station.postgis_geometry is None


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
    assert station.postgis_geometry == "SRID={0:};POINT(-34 41.46014)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station.lon = 19
    assert station._coordinates_longitude == 19
    assert station.postgis_geometry == "SRID={0:};POINT(19 41.46014)".format(WeatherStation.SRID_WEATHER_STATIONS)
    station = WeatherStation()
    station.lon = -34
    assert station._coordinates_longitude == -34
    assert station.postgis_geometry is None
    station.lon = 19
    assert station._coordinates_longitude == 19
    assert station.postgis_geometry is None


def test_json_parse_variable_state_01(variable_state_str_closed: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param variable_state_str_closed: String fixture with the text of a state with both dates
    :type variable_state_str_closed: str
    """
    state: VariableState = json.loads(variable_state_str_closed, object_hook=VariableState.object_hook)
    raw: Dict[str, Any] = json.loads(variable_state_str_closed)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == datetime.datetime.strptime(raw['dataFi'], "%Y-%m-%dT%H:%M%z")


def test_json_parse_variable_state_02(variable_state_str_open: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param variable_state_str_open: String fixture with the text of a state with both dates
    :type variable_state_str_open: str
    """
    state: VariableState = json.loads(variable_state_str_open, object_hook=VariableState.object_hook)
    raw: Dict[str, Any] = json.loads(variable_state_str_open)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == raw['dataFi'] and state.to_date is None and raw['dataFi'] is None


def test_json_encode_variable_state_01() -> None:
    state = VariableState(VariableStateCategory.ACTIVE,
                          datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                          datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    string = '{"code": 2, "from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}'
    assert json.loads(string) == json.loads(json.dumps(state, cls=VariableState.JSONEncoder))


def test_json_parse_variable_time_base_01(variable_time_base_str_closed: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param variable_time_base_str_closed: String fixture with the text of a state with both dates
    :type variable_time_base_str_closed: str
    """
    state: VariableState = json.loads(variable_time_base_str_closed, object_hook=VariableTimeBase.object_hook)
    raw: Dict[str, Any] = json.loads(variable_time_base_str_closed)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == datetime.datetime.strptime(raw['dataFi'], "%Y-%m-%dT%H:%M%z")


def test_json_parse_variable_time_base_02(variable_time_base_str_open: str) -> None:
    """
    Test parsing a string to JSON of a weather station status without errors

    :param variable_time_base_str_open: String fixture with the text of a state with both dates
    :type variable_time_base_str_open: str
    """
    state: VariableState = json.loads(variable_time_base_str_open, object_hook=VariableTimeBase.object_hook)
    raw: Dict[str, Any] = json.loads(variable_time_base_str_open)
    assert state.code.value == raw['codi']
    assert state.from_date == datetime.datetime.strptime(raw['dataInici'], "%Y-%m-%dT%H:%M%z")
    assert state.to_date == raw['dataFi'] and state.to_date is None and raw['dataFi'] is None


def test_json_encode_variable_time_base_01() -> None:
    time_base_01 = VariableTimeBase(VariableTimeBaseCategory.HO,
                                    datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                    datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    string = '{"code": "HO", "from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}'
    assert json.loads(string) == json.loads(json.dumps(time_base_01, cls=VariableTimeBase.JSONEncoder))
    time_base_02 = VariableTimeBase(VariableTimeBaseCategory.SH,
                                    datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                    datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    string = '{"code": "SH", "from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}'
    assert json.loads(string) == json.loads(json.dumps(time_base_02, cls=VariableTimeBase.JSONEncoder))


def test_json_parse_variable_01(variable_str: str) -> None:
    """
    Test parsing a string to JSON of a variable without errors

    :param variable_str: String fixture with the text of a state with both dates
    :type variable_str: str
    """
    variable: Variable = json.loads(variable_str, object_hook=Variable.object_hook)
    variable_json: Dict[str, Any] = json.loads(variable_str)
    assert variable.code == variable_json['codi']
    assert variable.name == variable_json['nom']
    assert variable.unit == variable_json['unitat']
    assert variable.acronym == variable_json['acronim']
    assert variable.category.value == variable_json['tipus']
    assert variable.decimal_positions == variable_json['decimals']
    assert len(variable.states) == len(variable_json['estats'])
    for idx in range(len(variable.states)):
        state: VariableState = variable.states[idx]
        assert state.code.value == variable_json['estats'][idx]['codi']
        assert state.from_date == datetime.datetime.strptime(variable_json['estats'][idx]['dataInici'],
                                                             "%Y-%m-%dT%H:%M%z")
        if state.to_date is None:
            assert variable_json['estats'][idx]['dataFi'] is None
        else:
            assert state.to_date == datetime.datetime.strptime(variable_json['estats'][idx]['dataFi'],
                                                               "%Y-%m-%dT%H:%M%z")
    # There is an error in the API and multiple equal time bases are sent, so in the fixture there appear the error
    # but the tests checks the classes recover from it
    assert len(variable.time_bases) == 2  # len(variable_json['basesTemporals'])
    assert len(variable_json['basesTemporals']) == 4  # the error described
    for idx in range(len(variable.time_bases)):
        time_base: VariableTimeBase = variable.time_bases[idx]
        assert time_base.code.value == variable_json['basesTemporals'][idx]['codi']
        assert time_base.from_date == datetime.datetime.strptime(variable_json['basesTemporals'][idx]['dataInici'],
                                                                 "%Y-%m-%dT%H:%M%z")
        if time_base.to_date is None:
            assert variable_json['basesTemporals'][idx]['dataFi'] is None
        else:
            assert time_base.to_date == datetime.datetime.strptime(variable_json['basesTemporals'][idx]['dataFi'],
                                                                   "%Y-%m-%dT%H:%M%z")


def test_json_parse_variable_02(variable_str_incomplete: str) -> None:
    """
    Test parsing a string to JSON of a variable without errors

    :param variable_str_incomplete: String fixture with the text of a state with both dates
    :type variable_str_incomplete: str
    """
    variable: Variable = json.loads(variable_str_incomplete, object_hook=Variable.object_hook)
    assert variable is None


def test_json_encode_variable_01() -> None:
    """
    Tests the encoding into JSON of a Variable (without state and time_base)
    """
    variable = Variable(code=26, name='Velocitat del vent a 2 m (vec.)', unit='m/s', acronym='VV2vec',
                        category=VariableCategory.DAT, decimal_positions=1)
    string = ('{"code": 26, "name": "Velocitat del vent a 2 m (vec.)", "category": "DAT", '
              '"unit": "m/s", "acronym": "VV2vec", "decimal_positions": 1, "states": [], "time_bases": []}')
    assert json.loads(string) == json.loads(json.dumps(variable, cls=Variable.JSONEncoder, ensure_ascii=False))


def no_test_json_encode_variable_02() -> None:
    """
    Tests the encoding into JSON of a Variable (with state and time_base)
    """
    variable = Variable(code=26, name='Velocitat del vent a 2 m (vec.)', unit='m/s', acronym='VV2vec',
                        category=VariableCategory.DAT, decimal_positions=1)
    state = VariableState(VariableStateCategory.ACTIVE,
                          datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                          datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    variable.states.append(state)
    time_base = VariableTimeBase(VariableTimeBaseCategory.HO,
                                 datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                 datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    variable.time_bases.append(time_base)
    time_base = VariableTimeBase(VariableTimeBaseCategory.SH,
                                 datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                                 datetime.datetime(2021, 1, 1, 10, 30, tzinfo=pytz.UTC))
    variable.time_bases.append(time_base)
    string = ('{"code": 26, "name": "Velocitat del vent a 2 m (vec.)", "category": "DAT", '
              '"unit": "m/s", "acronym": "VV2vec", "decimal_positions": 1, "states": [{"code": 2, '
              '"from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}], "time_bases": [{"code": "HO", '
              '"from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}, {"code": "SH", '
              '"from_date": "2020-01-01T10:30Z", "to_date": "2021-01-01T10:30Z"}]}')
    assert json.loads(string) == json.loads(json.dumps(variable, cls=Variable.JSONEncoder, ensure_ascii=False))


def test_json_parse_measure_01(measure_str: str) -> None:
    """
    Tests the parsing of a JSON string of a set of measures with errors

    :param measure_str: String fixture with the text of a set of measures
    :type measure_str: str
    """
    measures: List[Measure] = json.loads(measure_str, object_hook=Measure.object_hook)
    raw: Dict[str, Any] = json.loads(measure_str)
    assert len(measures) == len(raw['lectures'])
    for idx in range(len(measures)):
        assert measures[idx].value == raw['lectures'][idx]['valor']
        assert measures[idx].date == datetime.datetime.strptime(raw['lectures'][idx]['data'], "%Y-%m-%dT%H:%M%z")
        assert measures[idx].validity_state.value == raw['lectures'][idx]['estat']
        assert measures[idx].time_base.value == raw['lectures'][idx]['baseHoraria']


def test_json_parse_measure_02(measure_error_str: str) -> None:
    """
    Tests the parsing of a JSON string of a set of measures with errors

    :param measure_error_str: String fixture with a set of measures with missing parameters
    :type measure_error_str: str
    """
    measures: List[Measure] = json.loads(measure_error_str, object_hook=Measure.object_hook)
    assert measures is None


def test_json_encode_measure_01() -> None:
    """
    Tests the encoding into JSON of a Measure
    """
    measure = Measure(value=12.34, date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      validity_state=MeasureValidityCategory.VALID, time_base=MeasureTimeBaseCategory.SH)
    string = '{"value": 12.34, "date": "2020-01-01T10:30UTC", "date_extreme": null, "validity_state": "V", "time_base": "SH"}'
    assert json.loads(string) == json.loads(json.dumps(measure, cls=Measure.JSONEncoder, ensure_ascii=False))


def test_json_encode_measure_02() -> None:
    """
    Tests the encoding into JSON of a Measure
    """
    measure = Measure(value=12.34, date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      date_extreme=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      validity_state=MeasureValidityCategory.VALID, time_base=MeasureTimeBaseCategory.SH)
    string = '{"value": 12.34, "date": "2020-01-01T10:30UTC", "date_extreme": "2020-01-01T10:30UTC", "validity_state": "V", "time_base": "SH"}'
    assert json.loads(string) == json.loads(json.dumps(measure, cls=Measure.JSONEncoder, ensure_ascii=False))


def test_geojson_encode_measure_01() -> None:
    """
    Tests the encoding into a GeoJSON of a Measure without a station (and therefore without a location)
    """
    measure = Measure(value=12.34, date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      validity_state=MeasureValidityCategory.VALID, time_base=MeasureTimeBaseCategory.SH)
    string = '{"error": "No Weather Station linked with the Measure"}'
    assert json.loads(string) == json.loads(json.dumps(measure, cls=Measure.GeoJSONEncoder, ensure_ascii=False))


def test_geojson_encode_measure_02() -> None:
    """
    Tests the encoding into a GeoJSON of a Measure with a valid station
    """
    measure = Measure(value=12.34, date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      validity_state=MeasureValidityCategory.VALID, time_base=MeasureTimeBaseCategory.SH)
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    measure.station = station
    string = ('{"type": "Feature", "id": null, "crs": {"type": "link", '
              '"properties": {"href": "https://spatialreference.org/ref/epsg/4258/proj4/", "type": "proj4"}}, '
              '"geometry": {"type": "Point", "coordinates": [0.40562, 41.46014]}, "properties": {"value": 12.34, '
              '"date": "2020-01-01T10:30UTC", "date_extreme": null, "validity_state": "V", "time_base": "SH"}}')
    assert json.loads(string) == json.loads(json.dumps(measure, cls=Measure.GeoJSONEncoder, ensure_ascii=False))


def test_geojson_encode_measure_03() -> None:
    """
    Tests the encoding into a GeoJSON of a Measure with a valid station
    """
    measure = Measure(value=12.34, date=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      date_extreme=datetime.datetime(2020, 1, 1, 10, 30, tzinfo=pytz.UTC),
                      validity_state=MeasureValidityCategory.VALID, time_base=MeasureTimeBaseCategory.SH)
    station = WeatherStation(code='VL', name='Seròs - la Creu', category=WeatherStationCategory.AUTO,
                             coordinates_latitude=41.46014, coordinates_longitude=0.40562,
                             placement='Crta. de Seròs a la Granja d\'Escarp', altitude=100, municipality_code=252043,
                             municipality_name='Seròs', county_code=33, county_name='Segrià', province_code=25,
                             province_name='Lleida', network_code=1, network_name='XEMA')
    measure.station = station
    string = ('{"type": "Feature", "id": null, "crs": {"type": "link", '
              '"properties": {"href": "https://spatialreference.org/ref/epsg/4258/proj4/", "type": "proj4"}}, '
              '"geometry": {"type": "Point", "coordinates": [0.40562, 41.46014]}, "properties": {"value": 12.34, '
              '"date": "2020-01-01T10:30UTC", "date_extreme": "2020-01-01T10:30UTC", "validity_state": "V", "time_base": "SH"}}')
    assert json.loads(string) == json.loads(json.dumps(measure, cls=Measure.GeoJSONEncoder, ensure_ascii=False))




