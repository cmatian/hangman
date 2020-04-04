# File for connecting to the merriam-webster dictionary API and generating a random word
import json
import requests
from settings import API_KEY


class Generator:
    def __init__(self, word):
        self.word = word
        self.api_key = API_KEY.strip('"')  # strip out
        self.url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{self.word}?key={self.api_key}'

    def tether(self):
        res = requests.get(self.url)
        print(res.json())
