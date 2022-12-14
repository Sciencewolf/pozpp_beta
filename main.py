from Build import Build
import sys
import os

if __name__ == "__main__":
    WARNING = '\033[93m'
    ENDC = '\033[0m'

    # Here to check and automatically execute file [In future]

    if len(sys.argv) < 2:
        print("Error: Argument is not valid")
        print(WARNING + "Status: --argvnotcorrect" + ENDC)
        exit()
    elif len(sys.argv) > 2:
        print("Error: Too man arguments")
        print(WARNING + "Status: --overexpectedargvs" + ENDC)
    else:
        file_name = sys.argv[1]
        run = Build()
        return_code = Build.combine_all(run, file_name)

        if return_code == 0:
            print("Completed successfully")
            print(WARNING + "Status: --noerror, --completedsuccessfully" + ENDC)
        elif return_code == 1:
            print("Error: Code is not executed")
            print(WARNING + "Status: --error" + ENDC)
