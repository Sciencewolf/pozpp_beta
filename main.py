from Run import Run
import sys

if __name__ == "__main__":
    print("""
        main called
    """)

    file_name = sys.argv[1]

    run = Run()
    return_code = Run.combine_all(run, file_name)

    if return_code == 0:
        print("Completed successfully")
    elif return_code == 1:
        print("Error: Code is not executed")
