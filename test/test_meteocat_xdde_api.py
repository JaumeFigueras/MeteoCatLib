#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytz

from meteocat.api import meteocat_urls, meteocat_xdde_api
from meteocat.data_model.lightning import Lightning
from meteocat.data_model.lightning import LightningAPIRequest
import datetime
import requests
import pytest

from typing import List


def test_lightnings_01(requests_mock):
    """
    Tests an exception to a lightning request

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 10)
    requests_mock.get(url, exc=requests.exceptions.HTTPError)
    with pytest.raises(requests.exceptions.RequestException):
        _ = meteocat_xdde_api.get_lightnings('1234', datetime.datetime(2021, 11, 11, 10, 0, 0, tzinfo=pytz.UTC))


def test_lightnings_02(requests_mock):
    """
    Tests a timeout exception to a lightning request

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 2)
    requests_mock.get(url, exc=requests.exceptions.ConnectTimeout)
    with pytest.raises(requests.exceptions.RequestException):
        _ = meteocat_xdde_api.get_lightnings('1234', datetime.datetime(2021, 11, 11, 2, 0, 0, tzinfo=pytz.UTC))


def test_lightnings_03(requests_mock, meteocat_lightning_meteocat_api_json_list):
    """
    Tests a correct lightning request and check both the returned lightnings and the LightningAPIRequest object

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightning_meteocat_api_json_list: Fixture that simulates the return data from a lightning request
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 7)
    requests_mock.get(url, json=meteocat_lightning_meteocat_api_json_list, status_code=200)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.datetime(2021, 11, 11, 7, 0, 0, tzinfo=pytz.UTC))
    assert type(result['lightning_api_request']) == LightningAPIRequest
    for lightning in result['lightnings']:
        assert type(lightning) == Lightning
    lightning_api_request: LightningAPIRequest = result['lightning_api_request']
    lightnings: List[Lightning] = result['lightnings']
    assert lightning_api_request.date == datetime.datetime(2021, 11, 11, 7, 0, 0, tzinfo=pytz.UTC)
    assert lightning_api_request.http_status_code == 200
    assert lightning_api_request.number_of_lightnings == len(lightnings)
    assert len(lightnings) == len(meteocat_lightning_meteocat_api_json_list)


def test_lightnings_04(requests_mock, meteocat_lightnings_meteocat_api_invalid_date):
    """
    Tests a response error

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_lightnings_meteocat_api_invalid_date: Fixture that simulates the return data from a requests with
    an invalid date
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(2021, 11, 11, 10)
    requests_mock.get(url, json=meteocat_lightnings_meteocat_api_invalid_date, status_code=500)
    result = meteocat_xdde_api.get_lightnings('1234', datetime.datetime(2021, 11, 11, 10, 0, 0, tzinfo=pytz.UTC))
    assert type(result['lightning_api_request']) == LightningAPIRequest
    assert result['lightnings'] == []
    lightning_api_request: LightningAPIRequest = result['lightning_api_request']
    assert lightning_api_request.date == datetime.datetime(2021, 11, 11, 10, 0, 0, tzinfo=pytz.UTC)
    assert lightning_api_request.http_status_code == 500
    assert lightning_api_request.number_of_lightnings is None

