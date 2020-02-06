import pytest
import requests
from helpers.yandex_API import get_full_url_to_translate_random_word
from typing import Dict, Union
from helpers.logger import appLogger

@pytest.fixture()
def get_response_headers() -> Union[Dict, None]:
    response = requests.get(get_full_url_to_translate_random_word())
    if response.ok:
        headers_data: Dict = dict(response.headers)
        appLogger.debug('Getting response headers from Yandex Translator API')
        return headers_data
    else:
        return None

@pytest.fixture()
def get_response_body() -> Union[Dict, None]:
    response = requests.get(get_full_url_to_translate_random_word())
    if response.ok:
        body: Dict = response.json()
        appLogger.debug('Getting response body from Yandex Translator API')
        return body
    else:
        return None