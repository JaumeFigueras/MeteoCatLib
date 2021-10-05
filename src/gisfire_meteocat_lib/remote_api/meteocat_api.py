import requests

TIMEOUT = 5
RETRIES = 3


def get_from_api(api_token, api_url):
    """
    Gets the data returned by an API call to the MeteoCat service selected by the URL provided. Uses the default
    time-out time and retries (in case of error in the comms).

    :param api_token: Token string to identify who is doing the request. The token is provided by the MeteoCat agency
    :param api_url: The URL string to make the API call. Can be obtained from MeteoCat website
    :return: JSON metadata obtained from the API
    :rtype: list of dict or None. Dicts contain the data from the requested element
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
