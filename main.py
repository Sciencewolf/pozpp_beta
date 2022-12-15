from Interpreter import Interpreter
from Preprocess import Preprocess
import sys
import os


def execute():
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    interpreter = Interpreter()
    preprocess = Preprocess()

    if len(sys.argv) < 2:
        print("Error: Argument is not valid")
        print(WARNING + "Status: --argvnotcorrect" + ENDC)
        exit()
    elif len(sys.argv) > 2:
        print("Error: Too man arguments")
        print(WARNING + "Status: --overexpectedargvs" + ENDC)
        exit()
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print(interpreter.get_syntax())
    else:
        file_name = sys.argv[1]
        path = interpreter.open_pozpp_file(file_name)
        result = preprocess.convert_pozpp_to_py(path)
        if os.system(f'python {result}') == 0:
            print(WARNING + "Status: --noerror, --codeexecuted" + ENDC)
        else:
            print(WARNING + "Status: --error, --codenotexecuted" + ENDC)


if __name__ == "__main__":
    execute()
