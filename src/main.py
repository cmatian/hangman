import json
import sys
from PyQt5.QtWidgets import QApplication
from words import Words
from generator import Generator
from app import App


def main():
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec_())

    # def main():
    #     # Initialize core utilities
    #     gen = Generator()
    #     words = Words()

    #     # get the word list using user selection
    #     words.read_file()

    #     # select a word randomly from the list
    #     gen.set_random_word(words.word_list)

    #     # Query the word from the dictionary API
    #     data = gen.query_word_from_api()
    #     definitions = data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]

    #     print(gen.get_word())
    #     print(definitions)


if __name__ == "__main__":
    main()
