from Interpreter import Interpreter


class Preprocess:
    print("""
        Preprocess called
    """)

    def __init__(self):
        self.interpreter = Interpreter()
        # self.path = os.getcwd()
        self.KEYWORDS = {
            "chislo": "def",
            "holovna": "main",
            "kity": "if",
            "kity_net": "else",
            "ajbo": "elif",
            "nekaj": "print",
            "vhod": "input"
        }

    def convert_pozpp_to_py(self, file_name: str):
        var = self.interpreter.open_pozpp_file(file_name)
        pozpp_file = open(f"{var}", 'r')
        print("Var ", var)

        py_file = open(f'{file_name[:-6]}.py', 'w')

        lines = pozpp_file.readlines()
        print(lines)

        words = list(self.KEYWORDS.keys())

        # Implementation of converting pozpp to py, all keywords
        for word in words:
            for line in lines:
                if word in line:
                    line = self.KEYWORDS[word]
                    py_file.write(line)

        print("File name", py_file.name)

        return py_file.name
