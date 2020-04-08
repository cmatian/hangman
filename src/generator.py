# File for connecting to the merriam-webster dictionary API and generating a word
import json
import requests
import random
from settings import API_KEY, API_ID


class Generator:
    def __init__(self):
        self.word = None
        self.api_id = API_ID.strip('"')
        self.api_key = API_KEY.strip('"')  # strip out stray quotation marks

    # Set word randomly
    def set_random_word(self, list_of_words):
        self.word = random.choice(list_of_words)

    # Return a json representation of the data received from tether()
    def query_word_from_api(self):
        url = f'https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/{self.word}?fields=definitions'
        headers = {
            "app_id": API_ID,
            "app_key": API_KEY
        }
        res = requests.get(url, headers=headers)
        return res.json()

    # Set word manually
    def set_word(self, word):
        self.word = word.lower()
