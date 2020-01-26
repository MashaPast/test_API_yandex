import requests
from helpers.yandex_API import get_full_url_to_translate_random_word
import pytest
import json
import os

@pytest.fixture()
def get_response_headers(): #--> 'requests.structures.CaseInsensitiveDict'
    response = requests.get(get_full_url_to_translate_random_word())
    if response.ok:
        headers_data = dict(response.headers)
        return headers_data
    else:
        return None

@pytest.fixture()
def get_response_body():
    response = requests.get(get_full_url_to_translate_random_word())
    if response.ok:
        body_dict = response.json()
        print('This is response from yandex: ', body_dict['text'])
        return body_dict
    else:
        return None


def test_headers_equals_headers_asset_json(get_response_headers):
    with open(os.path.abspath('assets/headers_asset.json'), 'r') as f:
        headers_asset_dict = json.load(f)
        assert get_response_headers['Connection'] == headers_asset_dict['Connection']
        assert isinstance(int(get_response_headers['Content-Length']), int) is True
        assert get_response_headers['Keep-Alive'] == headers_asset_dict['Keep-Alive']
        assert get_response_headers['X-Content-Type-Options'] == headers_asset_dict['X-Content-Type-Options']


def test_response_body_equals_body_asset_1_json(get_response_body):
    with open(os.path.abspath('assets/body_asset_1.json'), 'r') as f:
        body_asset_dict = json.load(f)
        pytest.assume(get_response_body['code'] == body_asset_dict['res']['code'])
        pytest.assume(get_response_body['lang'] == body_asset_dict['res']['lang'])


