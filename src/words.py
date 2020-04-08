import easygui


class Words:
    def __init__(self):
        self.word_list = []

    def select_file(self):
        return easygui.fileopenbox(msg="Select a text file to import", title="File Selection",
                                       default='*', filetypes=["*.txt"])

    def read_file(self):
        text_file = self.select_file()

        if not text_file or not text_file.endswith(".txt"):
            print(f'Error Code -1: Invalid file or file type: {text_file}')
            return -1

        with open(text_file) as file:
            for line in file:
                line = line.strip()
                if line:
                    self.word_list.append(line)

    def get_word_list(self):
        return self.word_list
