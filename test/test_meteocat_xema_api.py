#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

import requests
from src.gisfire_meteocat_lib.remote_api import meteocat_xema_api
from src.gisfire_meteocat_lib.remote_api import meteocat_urls
from src.gisfire_meteocat_lib.remote_api import meteocat_api


def test_metadata_variables_01(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.VARIABLES_METADATA, json=meteocat_invalid_token, status_code=403)
    result = meteocat_xema_api.get_variables_measured_metadata('1234')
    assert result is None


def test_metadata_variables_02(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.VARIABLES_METADATA, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xema_api.get_variables_measured_metadata('2406')
    assert result is None
    # Return to previous state
    meteocat_api.TIMEOUT = 5


def test_metadata_variables_03(requests_mock, meteocat_variables_measured_metadata):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_measured_metadata: Fixture that simulates the return data from a real request obtained
    from MeteoCat API
    """
    requests_mock.get(meteocat_urls.VARIABLES_METADATA, json=meteocat_variables_measured_metadata, status_code=200)
    result = meteocat_xema_api.get_variables_measured_metadata('2406')
    assert result == meteocat_variables_measured_metadata


def test_metadata_variables_04(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.MULTI_VARIABLES_METADATA, json=meteocat_invalid_token, status_code=403)
    result = meteocat_xema_api.get_variables_multivariate_metadata('1234')
    assert result is None


def test_metadata_variables_05(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.MULTI_VARIABLES_METADATA, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xema_api.get_variables_multivariate_metadata('2406')
    assert result is None
    # Return to previous state
    requests_mock.exc = None
    meteocat_api.TIMEOUT = 5


def test_metadata_variables_06(requests_mock, meteocat_variables_multivariate_metadata):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_multivariate_metadata: Fixture that simulates the return data from a real request obtained
    from MeteoCat API
    """
    requests_mock.get(meteocat_urls.MULTI_VARIABLES_METADATA, json=meteocat_variables_multivariate_metadata,
                      status_code=200)
    result = meteocat_xema_api.get_variables_multivariate_metadata('2406')
    assert result == meteocat_variables_multivariate_metadata


def test_metadata_variables_07(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.AUXILIAR_VARIABLES_METADATA, json=meteocat_invalid_token, status_code=403)
    result = meteocat_xema_api.get_variables_auxiliary_metadata('1234')
    assert result is None


def test_metadata_variables_08(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.AUXILIAR_VARIABLES_METADATA, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xema_api.get_variables_auxiliary_metadata('2406')
    assert result is None
    # Return to previous state
    requests_mock.exc = None
    meteocat_api.TIMEOUT = 5


def test_metadata_variables_09(requests_mock, meteocat_variables_auxiliary_metadata):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_auxiliary_metadata: Fixture that simulates the return data from a real request obtained
    from MeteoCat API
    """
    requests_mock.get(meteocat_urls.AUXILIAR_VARIABLES_METADATA, json=meteocat_variables_auxiliary_metadata,
                      status_code=200)
    result = meteocat_xema_api.get_variables_auxiliary_metadata('2406')
    assert result == meteocat_variables_auxiliary_metadata


def test_metadata_stations_01(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the weather station MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.WEATHER_STATIONS, json=meteocat_invalid_token, status_code=403)
    result = meteocat_xema_api.get_weather_stations('1234')
    assert result is None


def test_metadata_stations_02(requests_mock):
    """
    Tests a no response in the weather stations data MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.WEATHER_STATIONS, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xema_api.get_weather_stations('2406')
    assert result is None
    # Return to previous state
    meteocat_api.TIMEOUT = 5


def test_metadata_stations_03(requests_mock, meteocat_stations_metadata):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_stations_metadata: Fixture that simulates the return data from a real request obtained from MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.WEATHER_STATIONS, json=meteocat_stations_metadata, status_code=200)
    result = meteocat_xema_api.get_weather_stations('2406')
    assert result == meteocat_stations_metadata


def test_station_variables_01(requests_mock, meteocat_station_measured_variables):
    """
    Tests a correct response of the measured variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_station_measured_variables: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_MEASURED_VARIABLES.format('CC'), json=meteocat_station_measured_variables,
                      status_code=200)
    result = meteocat_xema_api.get_station_measured_variables('2406', 'CC')
    assert result == meteocat_station_measured_variables


def test_station_variables_02(requests_mock, meteocat_station_multi_variables):
    """
    Tests a correct response of the multivariate variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_station_multi_variables: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_MULTI_VARIABLES.format('CC'), json=meteocat_station_multi_variables,
                      status_code=200)
    result = meteocat_xema_api.get_station_multi_variables('2406', 'CC')
    assert result == meteocat_station_multi_variables


def test_station_variables_03(requests_mock, meteocat_station_auxiliar_variables):
    """
    Tests a correct response of the auxiliar variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_station_auxiliar_variables: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_AUXILIAR_VARIABLES.format('CC'), json=meteocat_station_auxiliar_variables,
                      status_code=200)
    result = meteocat_xema_api.get_station_auxiliar_variables('2406', 'CC')
    assert result == meteocat_station_auxiliar_variables


def test_variable_data_01(requests_mock, meteocat_variables_measured_data):
    """
    Tests a correct response of the auxiliar variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_measured_data: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_MEASURED_DATA.format('1', '2021', '10', '22', 'YN'),
                      json=meteocat_variables_measured_data, status_code=200)
    result = meteocat_xema_api.get_measures_of_station_measured_variables('2406', 'YN', 1,
                                                                          datetime.date(2021, 10, 22))
    assert result == meteocat_variables_measured_data['lectures']


def test_variable_data_02(requests_mock, meteocat_variables_multi_data):
    """
    Tests a correct response of the auxiliar variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_multi_data: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_MULTI_DATA.format('6006', '2021', '10', '22', 'YN'),
                      json=meteocat_variables_multi_data, status_code=200)
    result = meteocat_xema_api.get_measures_of_station_multi_variables('2406', 'YN', 6006,
                                                                       datetime.date(2021, 10, 22))
    assert result == meteocat_variables_multi_data['lectures']


def test_variable_data_03(requests_mock, meteocat_variables_auxiliar_data):
    """
    Tests a correct response of the auxiliar variables assigned to a station from the MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_variables_auxiliar_data: Fixture that simulates the return data from a real request obtained from
    MeteoCat
    API
    """
    requests_mock.get(meteocat_urls.STATION_AUXILIAR_DATA.format('901', '2021', '10', '21', 'CE'),
                      json=meteocat_variables_auxiliar_data, status_code=200)
    result = meteocat_xema_api.get_measures_of_station_auxiliar_variables('2406', 'CE', 901,
                                                                          datetime.date(2021, 10, 21))
    assert result == meteocat_variables_auxiliar_data['lectures']
