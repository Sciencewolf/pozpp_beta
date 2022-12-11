from Interpreter import Interpreter


class Preprocess:
    '''print("""
        Preprocess called
    """, end="")'''

    def __init__(self):
        self.interpreter = Interpreter()
        self.KEYWORDS = {
            "chislo": "def",
            "holovna": "main",
            "kity": "if",
            "kity_net": "else",
            "ajbo": "elif",
            "nekaj": "print",
            "vhod": "input"
        }
        self.pozpp_file = ""
        self.py_file = ""
        self.ln = ''

    def convert_pozpp_to_py(self, file_name: str):
        var = self.interpreter.open_pozpp_file(file_name)
        self.pozpp_file = open(f"{var}", 'r')
        #print("Var ", var)

        self.py_file = open(f'{file_name[:-6]}.py', 'w')

        lines = self.pozpp_file.readlines()
        #print(lines)

        words = list(self.KEYWORDS.keys())
        #print("Words: ", words)

        # Implementation of converting pozpp to py, all keywords
        for line in lines:
            for word in words:
                if word in line:
                    # print(word, 'Add', 'line:', line, end=' ')
                    self.ln = line.replace(word, self.KEYWORDS[word])
                    self.py_file.write(self.ln)
                    # print(self.ln)
            if line.startswith("#"):
                self.ln = line
                self.py_file.write(self.ln)
                # print(self.ln)
            if line.startswith("\n"):
                self.ln = line
                self.py_file.write(self.ln)

        print("File name", self.py_file.name)

        self.pozpp_file.close()
        self.py_file.close()

        return self.py_file.name
