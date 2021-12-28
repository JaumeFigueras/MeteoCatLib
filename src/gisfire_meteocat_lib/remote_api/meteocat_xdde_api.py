#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import meteocat_urls
from . import meteocat_api
from ..classes.lightning import Lightning
from ..classes.lightning import LightningAPIRequest
import json


def get_lightnings(api_token, date):
    """
    Gets the lightnings registered in the MeteoCat agency for the date and hour provided Uses the default time-out time
    and number of retries (in case of error in the communications).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :param date: Date and hour of the request to perform
    :type date: datetime.datetime
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    url = meteocat_urls.LIGHTNINGS_DATA.format(date.year, date.month, date.day, date.hour)
    response = meteocat_api.get_from_api(api_token, url)
    lightning_api_request = LightningAPIRequest(date, response.status_code)
    lightnings = list()
    if response.status_code == 200:
        lightnings = json.loads(response.text, object_hook=Lightning.object_hook)
        lightning_api_request.number_of_lightnings = len(lightnings)
    return {
        'lightnings': lightnings,
        'lightning_api_request': lightning_api_request
    }
