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
    return meteocat_api.get_from_api(api_token, meteocat_urls.AUXILIAR_VARIABLES_METADATA)


def get_weather_stations(api_token):
    """
    Gets the weather stations data of MeteoCat network from its public API.  Uses the default time-out time and number
    of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.WEATHER_STATIONS)


def get_station_measured_variables(api_token, station_code):
    """
    Gets the list of measured variables (with its metadata) that are present in a certain station. The data includes
    the statuses of the variables of MeteoCat from its public API. Uses the default time-out time and number of retries
    (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :type api_token: str
    :param station_code: Weather station id code
    :type station_code: str
    :return: JSON metadata obtained from the API. The data format can be retrieved from:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio
    :rtype: Union[list[dict], None]
    """
    url = meteocat_urls.STATION_MEASURED_VARIABLES.format(station_code)
    return meteocat_api.get_from_api(api_token, url)


def get_station_multi_variables(api_token, station_code):
    """
    Gets the list of multivariate variables (with its metadata) that are present in a certain station. The data includes
    the statuses of the variables of MeteoCat from its public API. Uses the default time-out time and number of retries
    (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :type api_token: str
    :param station_code: Weather station id code
    :type station_code: str
    :return: JSON metadata obtained from the API. The data format can be retrieved from:
    https://apidocs.meteocat.gencat.cat/documentacio/calcul-multivariable/#metadades-de-les-variables-duna-estacio
    :rtype: Union[list[dict], None]
    """
    url = meteocat_urls.STATION_MULTI_VARIABLES.format(station_code)
    return meteocat_api.get_from_api(api_token, url)


def get_station_auxiliar_variables(api_token, station_code):
    """
    Gets the list of auxiliar variables (with its metadata) that are present in a certain station. The data includes
    the statuses of the variables of MeteoCat from its public API. Uses the default time-out time and number of retries
    (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :type api_token: str
    :param station_code: Weather station id code
    :type station_code: str
    :return: JSON metadata obtained from the API. The data format can be retrieved from:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-auxiliars/#metadades-de-les-variables-duna-estacio
    :rtype: Union[list[dict], None]
    """
    url = meteocat_urls.STATION_AUXILIAR_VARIABLES.format(station_code)
    return meteocat_api.get_from_api(api_token, url)


def get_measures_of_station_measured_variables(api_token, variable, date, station=None):
    """
    Gets the measured variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    variable_id = str(variable.id)
    year = str(date.year)
    month = "{:02d}".format(date.month)
    day = "{:02d}".format(date.day)
    url = meteocat_urls.VARIABLES_METADATA
    return meteocat_api.get_from_api(api_token, meteocat_urls.VARIABLES_METADATA)

