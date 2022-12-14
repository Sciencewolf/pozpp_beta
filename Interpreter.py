print("""
    Welcome to Pozakarpatskiy++ Programming Language
    Version 0.5 beta
    Project started: 11/28/2022
""")


class Interpreter:
    """print(
        "Interpreter called"
    , end="")"""

    def __init__(self):
        # self.path = os.getcwd()   Get current working directory
        self.ls = []  # List
        self.file_pozpp = ""

        self.WARNING = '\033[93m'
        self.ENDC = '\033[0m'
        self.BLUE = '\033[94m'

    def open_pozpp_file(self, file_name: str):
        if not file_name.endswith("pozpp"):
            print("Error: File extension is not correct")
            print(self.WARNING + "Status: --fileextnotcorrect" + self.ENDC)
        else:
            self.file_pozpp = open(f"{file_name}", 'r')
            self.ls = self.file_pozpp.readlines()

        self.file_pozpp.close()

        return self.file_pozpp.name
