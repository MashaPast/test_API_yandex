import pytest
import json
import os
from helpers.logger import appLogger
from typing import Dict




def test_headers_equals_headers_asset_json(get_response_headers):
    appLogger.debug('Getting headers_asset from file')
    with open(os.path.abspath('assets/headers_asset.json'), 'r') as f:
        headers_asset: Dict = json.load(f)
        appLogger.debug('Checking asserts')
        assert get_response_headers['Connection'] == headers_asset['Connection']
        assert isinstance(int(get_response_headers['Content-Length']), int) is True
        assert get_response_headers['Keep-Alive'] == headers_asset['Keep-Alive']
        assert get_response_headers['X-Content-Type-Options'] == headers_asset['X-Content-Type-Options']


def test_response_body_equals_body_asset_1_json(get_response_body):
    appLogger.debug('Getting body_asset from file')
    with open(os.path.abspath('assets/body_asset_1.json'), 'r') as f:
        body_asset: Dict = json.load(f)
        appLogger.debug('Checking asserts')
        pytest.assume(get_response_body['code'] == body_asset['res']['code'])
        pytest.assume(get_response_body['lang'] == body_asset['res']['lang'])


