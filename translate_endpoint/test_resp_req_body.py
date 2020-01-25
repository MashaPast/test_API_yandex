import requests
import json
import pytest
from config import config_data




@pytest.mark.parametrize(('file_path'), [('/home/krab/PycharmProjects/tests_API_yandex/translate_endpoint/assets/body_asset_1.json'),  ('/home/krab/PycharmProjects/tests_API_yandex/translate_endpoint/assets/body_asset_2.json')])
def test_resp_req_body_equals_body_asset_1_and_body_asset_2(file_path):
    with open(file_path, 'r') as f:
        body_asset_dict = json.load(f)
        text = body_asset_dict['req']['word']
    translate_config = config_data['YandexTranslateEndpoint']
    full_url = '{}?key={}&text={}&lang=en-ru'.format(translate_config['url'], translate_config['key'], text)
    response = requests.get(full_url)
    body_dict = response.json()
    print(body_dict['text'])
    assert (body_dict['text'] == body_asset_dict['res']['text'])


