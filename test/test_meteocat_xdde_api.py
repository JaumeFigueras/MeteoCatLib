#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

import requests
from src.gisfire_meteocat_lib.remote_api import meteocat_xdde_api
from src.gisfire_meteocat_lib.remote_api import meteocat_urls
from src.gisfire_meteocat_lib.remote_api import meteocat_api


def test_lightnings_01(requests_mock, meteocat_lightnings_invalid_date):
    """
    Tests the lightning api with an invalid date

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_invalid_date: Fixture that simulates the return data from a requests with an invalid date
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 258)
    requests_mock.get(url, json=meteocat_lightnings_invalid_date, status_code=400)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 258)
    assert result['status_code'] == 400
    assert result['data'] is None


def test_lightnings_02(requests_mock):
    """
    Tests the lightning api with an invalid date

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_invalid_date: Fixture that simulates the return data from a requests with an invalid date
    """
    meteocat_api.TIMEOUT = 0.1
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 2)
    requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 2)
    assert result['status_code'] is None
    assert result['data'] is None
    meteocat_api.TIMEOUT = 5


def test_lightnings_03(requests_mock, meteocat_lightnings_data):
    """
    Tests the lightning api with an invalid date

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_data: Fixture that simulates the return data from a requests with an invalid date
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 7)
    requests_mock.get(url, json=meteocat_lightnings_data, status_code=200)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.date(2021, 11, 11), 7)
    assert result['status_code'] == 200
    assert result['data'] == meteocat_lightnings_data


