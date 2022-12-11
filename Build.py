from Interpreter import Interpreter
from Preprocess import Preprocess


class Build:
    print("""
        Run called
    """)

    def __init__(self):
        self.interpreter = Interpreter()
        self.preprocess = Preprocess()

    def combine_all(self, file_name) -> int:
        path = self.interpreter.open_pozpp_file(file_name)
        result = self.preprocess.convert_pozpp_to_py(path)
        # Debug
        print("path: ", path)
        print("result", result)
        print("-"*20)
        print("Expected errors below")
        # End

        if exec(open(f'{result}').read()):
            print("Inside exec if")
            return 0

        return 1
