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
        self.path = os.getcwd()  # Get current working directory
        self.ls = []  # List

    def open_pozpp_file(self, file_name: str):
        if not file_name.endswith("pozpp"):
            print("Error: File extension is not correct")
        else:
            file_pozpp = open(f"{self.path}\\{file_name}", 'r')
            self.ls = file_pozpp.readlines()

        file = open(f"{self.path}\\{file_name}", 'w')

        for line in self.ls:
            file.write(line)

        return file.name
