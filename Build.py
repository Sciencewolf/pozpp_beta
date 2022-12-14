from Interpreter import Interpreter
from Preprocess import Preprocess
import os


class Build:
    """ print(
        "Build called"
    , end="") """

    def __init__(self):
        self.interpreter = Interpreter()
        self.preprocess = Preprocess()

        self.WARNING = '\033[93m'
        self.ENDC = '\033[0m'
        self.BLUE = '\033[94m'

    def combine_all(self, file_name) -> int:
        path = self.interpreter.open_pozpp_file(file_name)
        result = self.preprocess.convert_pozpp_to_py(path)

        print(self.BLUE + "-" * 20 + self.ENDC)
        print(self.WARNING + "Expected errors below" + self.ENDC)

        if os.system(f'python {result}') == 0:
            return 0
        else:
            return 1
