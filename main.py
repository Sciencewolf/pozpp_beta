from Build import Build
from Interpreter import Interpreter
import sys

if __name__ == "__main__":
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    interpreter = Interpreter()

    # Here to check and automatically execute file [In future]

    if len(sys.argv) < 2:
        print("Error: Argument is not valid")
        print(WARNING + "Status: --argvnotcorrect" + ENDC)
        exit()
    elif len(sys.argv) > 2:
        print("Error: Too man arguments")
        print(WARNING + "Status: --overexpectedargvs" + ENDC)
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print(interpreter.get_syntax())
    else:
        file_name = sys.argv[1]
        run = Build()
        return_code = Build.combine_all(run, file_name)

        if return_code == 0:
            print(WARNING + "Status: --noerror, --codeexecuted" + ENDC)
        elif return_code == 1:
            print(WARNING + "Status: --error, --codenotexecuted" + ENDC)
