from Interpreter import Interpreter
import os, sys


class Preprocess:
    def __init__(self):
        self.interpreter = Interpreter()
        self.path = os.getcwd()
        self.KEYWORDS = {
            "chislo": "def",
            "holovna": "main",
            "kity": "if",
            "kity_net": "else",
            "ajbo": "elif",
            "nekaj": "print",
            "vhod": "input"
        }

    def convert_pozpp_to_py(self, file_name: str):
        var = self.interpreter.open_pozpp_file(file_name)
        pozpp_file = open(f"{var}", 'r')

        py_file = open(f'{self.path}\\{file_name}', 'w')

        lines = pozpp_file.readlines()
        print(lines)

        words = list(self.KEYWORDS.keys())

        for word in words:
            for line in lines:
                if word in line:
                    line = self.KEYWORDS[word]
                    py_file.write(line)

        return py_file.name
