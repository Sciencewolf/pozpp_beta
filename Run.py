from Interpreter import Interpreter
from Preprocess import Preprocess

import sys
import os


# On dev
class Run:
    print("""
        Run called
    """)

    def __init__(self):
        self.interpreter = Interpreter()
        self.preprocess = Preprocess()

    def combine_all(self, file_name) -> int:
        path = self.interpreter.open_pozpp_file(file_name)
        result = self.preprocess.convert_pozpp_to_py(path)

        if exec(open(f'{result}').read()):
            return 0

        return 1
