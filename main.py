from Interpreter import Interpreter
from Preprocess import Preprocess
import sys, os

if __name__ == "__main__":
    path_of_input_file = sys.argv[1]

    interpreter = Interpreter()
    interpreter.open_pozpp_file(path_of_input_file)

    preprocess = Preprocess()
