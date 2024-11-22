import pytest
import os
import requests


HOSTNAME = os.getenv('APP_HOSTNAME', 'localhost')
PORT = os.getenv('PORT', '8888')
API_ALL_URL = '/server/info'


def get_all_urls(url):
    req = requests.get(url)
    response = req.json()
    return response['result']['all_urls']


@pytest.fixture(scope="module")
def backend() -> str:
    return f"http://{HOSTNAME}:{PORT}"


@pytest.fixture(scope="module")
def get_all_url(backend):
    api_all_urls = backend + API_ALL_URL
    all_urls = get_all_urls(api_all_urls)
    return all_urls


def test_get_info(backend, get_all_url) -> None:
    host = backend
    pars_url = []
    apis = get_all_url()
    for api in apis[:]:
        if '/printer/' not in api:
            pars_url.append(f"{host}{api}")
    print(pars_url)

def test_server_info():
    r = requests.get(backend + "/server/info")
    assert r.status_code == 200

def test_server_config():
    r = requests.get(backend + "/server/config")
    assert r.status_code == 200
