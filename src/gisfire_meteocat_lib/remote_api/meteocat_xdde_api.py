#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import meteocat_urls
from . import meteocat_api


def get_lightnings(api_token, date, hour):
    """
    Gets the lightnings registered in the MeteoCat agency for the date and hour provided Uses the default time-out time
    and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :param date:
    :type date: datetime.date
    :param hour:
    :type hour: int
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(date.year, date.month, date.day, hour)
    return meteocat_api.get_from_api(api_token, url)
