import requests
from requests.exceptions import RequestException

TIMEOUT = 5
RETRIES = 3


def get_from_api(api_token, api_url):
    """
    Gets the data returned by an API call to the MeteoCat service selected by the URL provided. Uses the default
    time-out time and retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :param api_url: The URL string to make the API call. Can be obtained from MeteoCat website
    :return: JSON metadata obtained from the API
    :rtype: (requests.Response, RequestException)
    """
    retries = 0
    headers = {'X-Api-Key': '{0:}'.format(api_token)}
    response = None
    xcpt = None
    while retries != RETRIES:
        try:
            response = requests.get(api_url, headers=headers, timeout=TIMEOUT)
            break
        except RequestException as e:
            retries += 1
            xcpt = e
    return response, xcpt
