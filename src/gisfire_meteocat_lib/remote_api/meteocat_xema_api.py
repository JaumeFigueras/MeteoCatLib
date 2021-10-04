import requests

from gisfire_meteocat_lib.remote_api import meteocat_urls

TIMEOUT = 5
RETRIES = 3


def get_variables_metadata(api_token, api_url=meteocat_urls.VARIABLES_METADATA):
    """
    Gets the variables metadata used in the weather stations of MeteoCat from its public API. Uses the default time-out
    time and retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :param api_url: The URL string to make the API call. It is defaulted to the current v1 URL obtained from MeteoCat
    website as of 2021-09-29
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    retries = 0
    headers = {'x-api-key': '{0:}'.format(api_token)}
    while retries != RETRIES:
        try:
            response = requests.get(api_url, headers=headers, timeout=TIMEOUT)
            data = response.json()
            if response.status_code == 200:
                return data
            else:
                return None
        except Exception:
            retries += 1
    return None


def get_variables_measured_metadata(api_token):
    """
    Gets the measured variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return get_variables_metadata(api_token, meteocat_urls.VARIABLES_METADATA)


def get_variables_multivariate_metadata(api_token):
    """
    Gets the multivariate variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return get_variables_metadata(api_token, meteocat_urls.MULTI_VARIABLES_METADATA)


def get_variables_auxiliary_metadata(api_token):
    """
    Gets the auxiliary variables metadata used in the weather stations of MeteoCat from its public API.
    Uses the default time-out time and number of retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Data contained in dicts can be retrieved from:
    """
    return get_variables_metadata(api_token, meteocat_urls.AUXILIARY_VARIABLES_METADATA)
