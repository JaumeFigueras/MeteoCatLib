#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    requests_mock.get(meteocat_urls.AUXILIARY_VARIABLES_METADATA, json=meteocat_invalid_token, status_code=403)
    result = meteocat_xema_api.get_variables_auxiliary_metadata('1234')
    assert result is None


def test_metadata_variables_08(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.AUXILIARY_VARIABLES_METADATA, exc=requests.exceptions.ConnectTimeout)
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
    requests_mock.get(meteocat_urls.AUXILIARY_VARIABLES_METADATA, json=meteocat_variables_auxiliary_metadata,
                      status_code=200)
    result = meteocat_xema_api.get_variables_auxiliary_metadata('2406')
    assert result == meteocat_variables_auxiliary_metadata
