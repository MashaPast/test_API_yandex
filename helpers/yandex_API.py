from random_word import RandomWords
from config import config_data

YANDEX_API_CONFIG = config_data['YandexTranslateEndpoint']

def get_full_url_to_translate_random_word() -> str:
    r = RandomWords()

    # Return a single random word
    text: str = r.get_random_word()
    translate_config = config_data['YandexTranslateEndpoint']
    full_url: str = '{}?key={}&text={}&lang=en-ru'.format(translate_config['url'], translate_config['key'], text)
    return full_url


def get_full_url_to_translate_from_asset(text) -> str:
    full_url:str = '{}?key={}&text={}&lang=en-ru'.format(YANDEX_API_CONFIG['url'], YANDEX_API_CONFIG['key'], text)
    return full_url
