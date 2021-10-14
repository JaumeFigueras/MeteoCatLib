#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import meteocat_urls
from . import meteocat_api


def get_variables_measured_metadata(api_token):
    """
    Gets the measured variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.VARIABLES_METADATA)


def get_variables_multivariate_metadata(api_token):
    """
    Gets the multivariate variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.MULTI_VARIABLES_METADATA)


def get_variables_auxiliary_metadata(api_token):
    """
    Gets the auxiliary variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.AUXILIARY_VARIABLES_METADATA)


def get_weather_stations(api_token):
    """
    Gets the weather stations data of MeteoCat network from its public API.  Uses the default time-out time and number
    of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.WEATHER_STATIONS)