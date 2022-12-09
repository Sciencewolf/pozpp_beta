import os, sys

print("""
Welcome to Pozakarpatsky++ programming language
Version 0.1
Project started: 11/28/2022

""")


class Interpreter:
    print("""
    Interpreter called
    """)

    def __init__(self):
        self.path = os.getcwd()
        self.KEYWORDS = {
            "chislo": "def",
            "holovna": "main",
            "kity": "if",
            "kity_net": "else",
            "ajbo": "elif",
            "nekaj": "print",
            "vhod": "input"
        }

    def open_pozpp_file(self, file_name: str):
        if not file_name.endswith("pozpp"):
            print("Error: File extension is not correct")
        else:
            file_pozpp = open(f"{self.path}\\{file_name}", 'r')
            ls = file_pozpp.readlines()

        file = open(f"{self.path}\\{file_name}", 'w')

        for line in ls:
            file.write(line)

        return file.name

