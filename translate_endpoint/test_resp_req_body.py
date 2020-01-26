import requests
import json
import pytest
from config import config_data
import os

YANDEX_API_CONFIG = config_data['YandexTranslateEndpoint']



@pytest.mark.parametrize(('file_path'), [('assets/body_asset_1.json'),  ('assets/body_asset_2.json')])
def test_yandex_api_word_translate(file_path):

    with open(os.path.abspath(file_path), 'r') as f:
        body_asset = json.load(f)
        text = body_asset['req']['word']

#chenge to func
    full_url = '{}?key={}&text={}&lang=en-ru'.format(YANDEX_API_CONFIG['url'], YANDEX_API_CONFIG['key'], text)
    response = requests.get(full_url)
    body_response = response.json()

    assert (body_response['text'] == body_asset['res']['text'])


