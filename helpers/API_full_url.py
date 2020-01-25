from random_word import RandomWords
from config import config_data

r = RandomWords()

# Return a single random word
text = r.get_random_word()
translate_config = config_data['YandexTranslateEndpoint']
full_url = '{}?key={}&text={}&lang=en-ru'.format(translate_config['url'], translate_config['key'], text)

