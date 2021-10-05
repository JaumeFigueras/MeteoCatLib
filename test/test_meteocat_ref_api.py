import requests
from src.gisfire_meteocat_lib.remote_api import meteocat_ref_api
from src.gisfire_meteocat_lib.remote_api import meteocat_urls
from src.gisfire_meteocat_lib.remote_api import meteocat_api


def test_ref_01(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the comarques MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.COMARQUES, json=meteocat_invalid_token, status_code=403)
    result = meteocat_ref_api.get_comarques('1234')
    assert result is None


def test_ref_02(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.COMARQUES, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_ref_api.get_comarques('2406')
    assert result is None
    # Return to previous state
    meteocat_api.TIMEOUT = 5


def test_ref_03(requests_mock, meteocat_comarques):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_comarques: Fixture that simulates the return data from a real request obtained
    from MeteoCat API
    """
    requests_mock.get(meteocat_urls.COMARQUES, json=meteocat_comarques, status_code=200)
    result = meteocat_ref_api.get_comarques('2406')
    assert result == meteocat_comarques


def test_ref_04(requests_mock, meteocat_invalid_token):
    """
    Tests the invalid token (or not token) in the comarques MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_invalid_token: Fixture that simulates the return data from a requests with an invalid token
    """
    requests_mock.get(meteocat_urls.MUNICIPIS, json=meteocat_invalid_token, status_code=403)
    result = meteocat_ref_api.get_municipis('1234')
    assert result is None


def test_ref_05(requests_mock):
    """
    Tests a no response in the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    """
    # Set small timeout time to save testing execution time
    meteocat_api.TIMEOUT = 0.1
    requests_mock.get(meteocat_urls.MUNICIPIS, exc=requests.exceptions.ConnectTimeout)
    result = meteocat_ref_api.get_municipis('2406')
    assert result is None
    # Return to previous state
    meteocat_api.TIMEOUT = 5


def test_ref_06(requests_mock, meteocat_municipis):
    """
    Tests a correct response of the measured variables metadata MeteoCat api call

    :param requests_mock: Requests mock for pytest. Allows change behaviour change of HTTP requests
    :param meteocat_municipis: Fixture that simulates the return data from a real request obtained
    from MeteoCat API
    """
    requests_mock.get(meteocat_urls.MUNICIPIS, json=meteocat_municipis, status_code=200)
    result = meteocat_ref_api.get_municipis('2406')
    assert result == meteocat_municipis


