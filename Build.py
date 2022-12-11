from Interpreter import Interpreter
from Preprocess import Preprocess
import os


class Build:
    '''print("""
        Build called
    """, end="")'''

    def __init__(self):
        self.interpreter = Interpreter()
        self.preprocess = Preprocess()

    def combine_all(self, file_name) -> int:
        path = self.interpreter.open_pozpp_file(file_name)
        result = self.preprocess.convert_pozpp_to_py(path)
        # Debug
        #print("path: ", path)
        #print("result", result)
        print("-" * 20)
        print("Expected errors below")
        # End

        if os.system(f'python {result}') == 0:
            return 0
        else:
            return 1
