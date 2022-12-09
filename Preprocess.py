from Interpreter import Interpreter
import os, sys


class Preprocess:
    def __init__(self):
        self.interpreter = Interpreter()
        self.path = os.getcwd()


    def convert_pozpp_to_py(self, file_name: str):
        var = self.interpreter.open_pozpp_file(file_name)

        pozpp_file = open(f"{var}", 'r')

        py_file = open(self.path + "main.py", 'w')

        ls = pozpp_file.readlines()
        print(ls)
