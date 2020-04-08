# File for connecting to the merriam-webster dictionary API and generating a random word
import json
import requests
from settings import API_KEY


class Generator:
    def __init__(self, word):
        self.word = word
        self.api_key = API_KEY.strip('"')  # strip out stray quotation marks
        self.url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{self.word}?key={self.api_key}'

    def query_word(self):
        res = self.tether()
        return res.json()

    def tether(self):
        return requests.get(self.url)

    def set_word(self, word):
        self.word = word
