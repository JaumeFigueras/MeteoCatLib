#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.gisfire_meteocat_lib.remote_api import meteocat_xdde_api
from src.gisfire_meteocat_lib.remote_api import meteocat_urls
from src.gisfire_meteocat_lib.remote_api import meteocat_api
from src.gisfire_meteocat_lib.classes.lightning import Lightning
import datetime
import requests


def test_lightnings_01(requests_mock, meteocat_lightnings_meteocat_api_invalid_date):
    """
    Tests the lightning api with an invalid date

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_meteocat_api_invalid_date: Fixture that simulates the return data from a requests with an invalid date
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 258)
    print(url)
    requests_mock.get(url, json=meteocat_lightnings_meteocat_api_invalid_date, status_code=400)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 258)
    assert result['status_code'] == 400
    assert result['data'] is None


def test_lightnings_02(requests_mock):
    """
    TODO:

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    meteocat_api.TIMEOUT = 0.1
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 2)
    requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 2)
    assert result['status_code'] == -1
    assert type(result['message']) == str
    assert result['data'] is None
    meteocat_api.TIMEOUT = 5


def test_lightnings_03(requests_mock, meteocat_lightning_meteocat_api_json_list):
    """
    TODO:

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightning_meteocat_api_json_list: Fixture that simulates the return data from a requests with an invalid date
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 7)
    requests_mock.get(url, json=meteocat_lightning_meteocat_api_json_list, status_code=200)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 7)
    assert result['status_code'] == 200
    assert result['message'] is None
    assert len(result['data']) == 3
    for light in result['data']:
        assert type(light) == Lightning


