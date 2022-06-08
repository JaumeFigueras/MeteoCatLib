#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.gisfire_meteocat_lib.classes.lightning import Lightning
from src.gisfire_meteocat_lib.classes.lightning import LightningAPIRequest
import pytest
import json
import datetime
import pytz
from sqlalchemy import func

def test_json_parse_lightning_01(meteocat_lightning_meteocat_api_string, meteocat_lightning_meteocat_api_json):
    """
    Test JSON parsing, a list of Lightning objects have to be returned when the parsing of a Meteocat API string of
    three lightnings

    :param meteocat_lightning_meteocat_api_string: Pytest fixture with a Meteocat API XDDE lightning stored in a string
    :type meteocat_lightning_meteocat_api_string: str
    :param meteocat_lightning_meteocat_api_json: Pytest fixture with a Meteocat API XDDE lightning parsed with the json
    standard library to check the results
    :type meteocat_lightning_meteocat_api_json: dict
    :return: None
    """
    lightning = json.loads(meteocat_lightning_meteocat_api_string, object_hook=Lightning.object_hook)
    assert not(lightning is None)
    assert type(lightning) is Lightning
    assert lightning.meteocat_id == meteocat_lightning_meteocat_api_json['id']
    assert lightning.date == datetime.datetime.strptime(meteocat_lightning_meteocat_api_json['data'],
                                                        "%Y-%m-%dT%H:%M:%S.%f%z")
    assert lightning.peak_current == meteocat_lightning_meteocat_api_json['correntPic']
    assert lightning.chi_squared == meteocat_lightning_meteocat_api_json['chi2']
    assert lightning.ellipse_major_axis == meteocat_lightning_meteocat_api_json['ellipse']['eixMajor']
    assert lightning.ellipse_minor_axis == meteocat_lightning_meteocat_api_json['ellipse']['eixMenor']
    assert lightning.ellipse_angle == meteocat_lightning_meteocat_api_json['ellipse']['angle']
    assert lightning.number_of_sensors == meteocat_lightning_meteocat_api_json['numSensors']
    assert lightning.hit_ground == meteocat_lightning_meteocat_api_json['nuvolTerra']
    assert lightning._coordinates_latitude == meteocat_lightning_meteocat_api_json['coordenades']['latitud']
    assert lightning._coordinates_longitude == meteocat_lightning_meteocat_api_json['coordenades']['longitud']
    assert lightning.municipality_code == int(meteocat_lightning_meteocat_api_json['idMunicipi'])
    assert lightning.geom == "SRID={2:};POINT({0:} {1:})".format(lightning._coordinates_longitude,
                                                                 lightning._coordinates_latitude,
                                                                 Lightning.DEFAULT_SRID_LIGHTNINGS)


def test_json_parse_lightning_02(meteocat_lightning_meteocat_api_string_list,
                                 meteocat_lightning_meteocat_api_json_list):
    """
    Test JSON parsing, a list of Lightning objects have to be returned when the parsing of a Meteocat API string of
    three lightnings

    :param meteocat_lightning_meteocat_api_string_list: Pytest fixture with a Meteocat API XDDE list of lightnings
    stored in a string
    :type meteocat_lightning_meteocat_api_string_list: str
    :param meteocat_lightning_meteocat_api_json_list: Pytest fixture with a Meteocat API XDDE list of lightnings parsed
    with the json standard library to check the results
    :type meteocat_lightning_meteocat_api_json_list: list(dict)
    :return: None
    """
    lightnings = json.loads(meteocat_lightning_meteocat_api_string_list, object_hook=Lightning.object_hook)
    assert len(lightnings) == len(meteocat_lightning_meteocat_api_json_list)
    for i in range(len(lightnings)):
        assert lightnings[i] is not None
        assert type(lightnings[i]) is Lightning
        assert lightnings[i].meteocat_id == meteocat_lightning_meteocat_api_json_list[i]['id']
        assert lightnings[i].date == datetime.datetime.strptime(meteocat_lightning_meteocat_api_json_list[i]['data'],
                                                                "%Y-%m-%dT%H:%M:%S.%f%z")
        assert lightnings[i].peak_current == meteocat_lightning_meteocat_api_json_list[i]['correntPic']
        assert lightnings[i].chi_squared == meteocat_lightning_meteocat_api_json_list[i]['chi2']
        assert lightnings[i].ellipse_major_axis == meteocat_lightning_meteocat_api_json_list[i]['ellipse']['eixMajor']
        assert lightnings[i].ellipse_minor_axis == meteocat_lightning_meteocat_api_json_list[i]['ellipse']['eixMenor']
        assert lightnings[i].ellipse_angle == meteocat_lightning_meteocat_api_json_list[i]['ellipse']['angle']
        assert lightnings[i].number_of_sensors == meteocat_lightning_meteocat_api_json_list[i]['numSensors']
        assert lightnings[i].hit_ground == meteocat_lightning_meteocat_api_json_list[i]['nuvolTerra']
        assert lightnings[i]._coordinates_latitude == \
               meteocat_lightning_meteocat_api_json_list[i]['coordenades']['latitud']
        assert lightnings[i]._coordinates_longitude == \
               meteocat_lightning_meteocat_api_json_list[i]['coordenades']['longitud']
        if 'idMunicipi' in meteocat_lightning_meteocat_api_json_list[i]:
            assert lightnings[i].municipality_code == int(meteocat_lightning_meteocat_api_json_list[i]['idMunicipi'])
        else:
            assert lightnings[i].municipality_code is None
        assert lightnings[i].geom == "SRID={2:};POINT({0:} {1:})".format(lightnings[i]._coordinates_longitude,
                                                                         lightnings[i]._coordinates_latitude,
                                                                         Lightning.DEFAULT_SRID_LIGHTNINGS)


def test_json_parse_lightning_03(meteocat_lightning_meteocat_api_string_error_ellipse):
    """
    Test JSON parsing, a None object has to be returned when the parsing of a Meteocat API string is missing some
    mandatory data

    :param meteocat_lightning_meteocat_api_string_error_ellipse: Pytest fixture with a Meteocat API XDDE lightning
    string with a missing 'ellipse' field
    :type meteocat_lightning_meteocat_api_string_error_ellipse: str
    :return:
    """
    lightning = json.loads(meteocat_lightning_meteocat_api_string_error_ellipse, object_hook=Lightning.object_hook)
    assert lightning is None


def test_json_parse_lightning_04(meteocat_lightning_meteocat_api_string_error_date):
    """
    Test JSON parsing, a None object has to be returned when the parsing of a Meteocat API string contains an error in
    the date format

    :param meteocat_lightning_meteocat_api_string_error_date: Pytest fixture with a Meteocat API XDDE lightning string
    with an error in the 'data' field
    :type meteocat_lightning_meteocat_api_string_error_date: str
    :return: None
    """
    lightning = json.loads(meteocat_lightning_meteocat_api_string_error_date, object_hook=Lightning.object_hook)
    assert lightning is None


def test_json_encoder_lightning_01():
    """
    Tests the JSON encoding of a Lightning object

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    string = json.dumps(lightning, cls=Lightning.JSONEncoder)
    assert string == ('{"meteocat_id": 22449035, "date": "2021-11-11T08:45:00.868454Z", "peak_current": -137.455, '
                      '"chi_squared": 0.40000001, "ellipse_major_axis": 4000, "ellipse_minor_axis": 600, '
                      '"ellipse_angle": 51, "number_of_sensors": 3, "hit_ground": true, "municipality_code": 170144, '
                      '"coordinates_latitude": 42.407753, "coordinates_longitude": 2.7945485, '
                      '"coordinates_epsg": 4258}')


def test_date_parse_lightning_01():
    """
    Test the string to date conversion of the recording date of a lightning

    :return: None
    """
    lightning = Lightning(date="2021-11-11T08:45:00.868454Z")
    assert lightning.date == datetime.datetime(2021, 11, 11, 8, 45, 0, 868454, tzinfo=pytz.UTC)
    with pytest.raises(ValueError):
        _ = Lightning(date="2021-11-1108:45:00.868454")


def test_latitude_getter_01():
    """
    Test the lightning lat property getter

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    assert lightning.lat == 42.407753


def test_longitude_getter_01():
    """
    Test the lightning lon property getter

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    assert lightning.lon == 2.7945485


# noinspection DuplicatedCode
def test_latitude_setter_01():
    """
    Test the lightning lat property setter with a value higher than the upper bound

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    with pytest.raises(ValueError):
        lightning.lat = 1234


def test_latitude_setter_02():
    """
    Test the lightning lat property setter with a value smaller than the lower bound

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    with pytest.raises(ValueError):
        lightning.lat = -1234


def test_latitude_setter_03():
    """
    Test the lightning lat property setter with a valid value

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    lightning.lat = -34
    assert lightning._coordinates_latitude == -34
    assert lightning.geom == "SRID={0:};POINT(2.7945485 -34)".format(Lightning.DEFAULT_SRID_LIGHTNINGS)
    lightning.lat = 19
    assert lightning._coordinates_latitude == 19
    assert lightning.geom == "SRID={0:};POINT(2.7945485 19)".format(Lightning.DEFAULT_SRID_LIGHTNINGS)


def test_latitude_setter_04():
    """
    Test the lightning lat property setter with a valid value

    :return: None
    """
    lightning = Lightning()
    lightning.lat = -34
    assert lightning._coordinates_latitude == -34
    assert lightning.geom is None
    lightning.lat = 19
    assert lightning._coordinates_latitude == 19
    assert lightning.geom is None


# noinspection DuplicatedCode
def test_longitude_setter_01():
    """
    Test the lightning lon property setter with a value higher than the upper bound

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    with pytest.raises(ValueError):
        lightning.lon = 1234


def test_longitude_setter_02():
    """
    Test the lightning lon property setter with a value smaller than the lower bound

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    with pytest.raises(ValueError):
        lightning.lon = -1234


def test_longitude_setter_03():
    """
    Test the lightning lon property setter with a valid value

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    lightning.lon = -34
    assert lightning._coordinates_longitude == -34
    assert lightning.geom == "SRID={0:};POINT(-34 42.407753)".format(Lightning.DEFAULT_SRID_LIGHTNINGS)
    lightning.lon = 19
    assert lightning._coordinates_longitude == 19
    assert lightning.geom == "SRID={0:};POINT(19 42.407753)".format(Lightning.DEFAULT_SRID_LIGHTNINGS)


def test_longitude_setter_04():
    """
    Test the lightning lat property setter with a valid value

    :return: None
    """
    lightning = Lightning()
    lightning.lon = -34
    assert lightning._coordinates_longitude == -34
    assert lightning.geom is None
    lightning.lon = 19
    assert lightning._coordinates_longitude == 19
    assert lightning.geom is None


def test_date_parse_lightning_api_request_01():
    """
    Test the string to date conversion of the recording date of a lightningAPIRequest

    :return: None
    """
    lightning_api_request = LightningAPIRequest(date="2021-11-11T08:45:00.868454Z")
    assert lightning_api_request.date == datetime.datetime(2021, 11, 11, 8, 0, 0, 0, tzinfo=pytz.UTC)
    with pytest.raises(ValueError):
        _ = LightningAPIRequest(date="2021-11-1108:45:00.868454")


def test_date_replace_lightning_api_request_01():
    """
    Test the string to date conversion of the recording date of a lightningAPIRequest

    :return: None
    """
    lightning_api_request = LightningAPIRequest(date=datetime.datetime(2021, 11, 11, 8, 45, 0, 868454, tzinfo=pytz.UTC))
    assert lightning_api_request.date == datetime.datetime(2021, 11, 11, 8, 0, 0, 0, tzinfo=pytz.UTC)
    lightning_api_request = LightningAPIRequest(date="2021-11-11T08:45:00.868454Z")
    assert lightning_api_request.date == datetime.datetime(2021, 11, 11, 8, 0, 0, 0, tzinfo=pytz.UTC)


def test_st_transform(db_session):
    """
    TODO Testing for custom SRID
    :param db_session:
    :type db_session:
    :return:
    :rtype:
    """
    # lightnings = db_session.query(Lightning.__geom.ST_Transform(25831)).all()
    mixed = db_session.query(Lightning, func.ST_X(Lightning.geometry.ST_Transform(25831)), func.ST_Y(Lightning.geometry.ST_Transform(25831))).all()
    lightnings = list()
    for lightning, x, y in mixed:
        lightning.y = y
        lightning.x = x
        lightning.srid = 25831
        lightnings.append(lightning)
    string = json.dumps(lightnings, cls=Lightning.JSONEncoder)
    print(string)


def test_geojson_encoder_lightning_00():
    """
    Tests the JSON encoding of a Lightning object

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    string = json.dumps({'type': 'kk', "elems": [lightning, lightning, lightning]}, cls=Lightning.GeoJSONEncoder)
    assert string == ('{"meteocat_id": 22449035, "date": "2021-11-11T08:45:00.868454Z", "peak_current": -137.455, '
                      '"chi_squared": 0.40000001, "ellipse_major_axis": 4000, "ellipse_minor_axis": 600, '
                      '"ellipse_angle": 51, "number_of_sensors": 3, "hit_ground": true, "municipality_code": 170144, '
                      '"coordinates_latitude": 42.407753, "coordinates_longitude": 2.7945485, '
                      '"coordinates_epsg": 4258}')


def test_geojson_encoder_lightning_01():
    """
    Tests the JSON encoding of a Lightning object

    :return: None
    """
    lightning = Lightning(22449035, "2021-11-11T08:45:00.868454Z", -137.455, 0.40000001, 4000, 600, 51, 3, True, 170144,
                          42.407753, 2.7945485)
    string = json.dumps(lightning, cls=Lightning.GeoJSONEncoder)
    assert string == ('{"meteocat_id": 22449035, "date": "2021-11-11T08:45:00.868454Z", "peak_current": -137.455, '
                      '"chi_squared": 0.40000001, "ellipse_major_axis": 4000, "ellipse_minor_axis": 600, '
                      '"ellipse_angle": 51, "number_of_sensors": 3, "hit_ground": true, "municipality_code": 170144, '
                      '"coordinates_latitude": 42.407753, "coordinates_longitude": 2.7945485, '
                      '"coordinates_epsg": 4258}')
