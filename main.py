from Build import Build
import sys

if __name__ == "__main__":
    ''' print("""
    # main called
    # """, end="") '''

    file_name = sys.argv[1]
    print("Main: file_name", file_name)

    run = Build()
    return_code = Build.combine_all(run, file_name)

    if return_code == 0:
        print("Completed successfully")
        print("Status: --noerror")
    elif return_code == 1:
        print("Error: Code is not executed")
        print("Status: --error")
