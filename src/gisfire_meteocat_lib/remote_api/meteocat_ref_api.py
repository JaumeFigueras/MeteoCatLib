import requests

from . import meteocat_urls
from . import meteocat_api

TIMEOUT = 5
RETRIES = 3


def get_comarques(api_token):
    """
    Gets the measured variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.COMARQUES)


def get_municipis(api_token):
    """
    Gets the measured variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return meteocat_api.get_from_api(api_token, meteocat_urls.MUNICIPIS)
