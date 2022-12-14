print(
    """
        Welcome to Pozakarpatskiy++ Programming Language
        Version 0.5 
        Project started: 11/28/2022
    """)
print('\033[93m' + "Get help python main.py --help" + '\033[0m')
print('\033[93m' + "Get help python main.py -h" + '\033[0m')


class Interpreter:

    def __init__(self):
        self.ls = []  # List
        self.file_pozpp = ""

        self.WARNING = '\033[93m'
        self.ENDC = '\033[0m'
        self.BLUE = '\033[94m'

    def open_pozpp_file(self, file_name: str):
        if not file_name.endswith("pozpp"):
            print(self.WARNING + "Status: --fileextnotcorrect" + self.ENDC)
        else:
            self.file_pozpp = open(f"{file_name}", 'r')
            self.ls = self.file_pozpp.readlines()

        self.file_pozpp.close()

        return self.file_pozpp.name

    def get_syntax(self):
        text = """
        Pozakarpatskiy programming language is based on Python programming language
        Syntax of Pozakarpatskiy(pozpp) is similar to Python(py), but keywords(not all already) is changed
            
        KEYWORDS
            In Python -> def, main(), if, elif, else, print, input
            In Pozakarpatskiy -> chislo, holovna, kity, kity_net, ajbo, nekaj, vhod
            
        In pozpp this code below is required to write
            |
            kity __name__ == "__main__":
                # methods, fields is here 
            
        Python version
            |
            if __name__ == "__main__":
                # calling methods here
                # fields here
                
        Hello, World! Program
            |
            kity __name__ == "__main__":
                nekaj("Hello, World!")
                
                
        List of status strings(Errors)
            |
            Zero issue
                |
            --noerror
            [Definition soon]
            --codeexecuted
            []
                |
            Issues
                |
            --fileextnotcorrect
            []
            --argvnotcorrect
            []
            --overexpectedargvs
            []
            --error
            []
            --codenotexecuted
            []
    """

        return text
