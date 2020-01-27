import requests
import json
import pytest
import os
from helpers.yandex_API import get_full_url_to_translate_from_asset
from helpers.logger import appLogger
from typing import Dict

@pytest.mark.parametrize(('file_path'), [('assets/body_asset_1.json'),  ('assets/body_asset_2.json')])
def test_yandex_api_word_translate(file_path):
    appLogger.debug('Getting text from body request from file')
    with open(os.path.abspath(file_path), 'r') as f:
        body_asset: Dict = json.load(f)
        text: str = body_asset['req']['word']

    appLogger.debug('Getting  full_url and response')
    full_url: str = get_full_url_to_translate_from_asset(text)
    response = requests.get(full_url)
    appLogger.debug('Getting body response')
    body_response: Dict = response.json()

    appLogger.debug('Checking asserts')
    assert (body_response['text'] == body_asset['res']['text'])


