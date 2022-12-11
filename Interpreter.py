import os

print("""
Welcome to Pozakarpatsky++ programming language
Version 0.5
Project started: 11/28/2022
""")


class Interpreter:
    '''print("""
        Interpreter called
    """, end="")'''

    def __init__(self):
        # self.path = os.getcwd()   Get current working directory
        self.ls = []  # List
        self.file_pozpp = ""

    def open_pozpp_file(self, file_name: str):
        if not file_name.endswith("pozpp"):
            print("Error: File extension is not correct")
        else:
            self.file_pozpp = open(f"{file_name}", 'r')
            self.ls = self.file_pozpp.readlines()
            # print("File is good")

        print("File_pozpp name Interpreter", self.file_pozpp.name)

        self.file_pozpp.close()

        return self.file_pozpp.name
