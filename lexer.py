import re

# Token Types
TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_ID = "ID"
TT_PLUS = "+"
TT_MINUS = "-"
TT_LESS = "<"
TT_GREATER = ">"
TT_LEFTPAREN = "("
TT_RIGHTPAREN = ")"
TT_DIVIDE = "/"
TT_MULTIPLY = "*"
TT_EQUAL = "="
TT_SEMI = ";"
TT_STRING = "STRING"
# Lexer Class
class Lexer:
    def __init__(self, input_code):
        self.code = input_code
    def tokenize(self):
        tokens = []
        words = re.findall(r'\w+|[^\w\s]', self.code)  

        for t in words:
            if t.isdigit():
                tokens.append((TT_INT, int(t)))
            elif t.replace('.', '', 1).isdigit() and t.count('.') < 2:
                tokens.append((TT_FLOAT, float(t)))
            elif t.isidentifier():  
                tokens.append((TT_ID, t))
            elif t == "+":
                tokens.append((TT_PLUS, t))
            elif t == "-":
                tokens.append((TT_MINUS, t))
            elif t == "/":
                tokens.append((TT_DIVIDE, t))
            elif t == "*":
                tokens.append((TT_MULTIPLY, t))
            elif t == "<":
                tokens.append((TT_LESS, t))
            elif t == ">":
                tokens.append((TT_GREATER, t))
            elif t == "(":
                tokens.append((TT_LEFTPAREN, t))
            elif t == ")":
                tokens.append((TT_RIGHTPAREN, t))
            elif t == "=":
                tokens.append((TT_EQUAL, t))
            elif t == ";":
                tokens.append((TT_SEMI, t))
            else:
                print(f"Invalid token: {t}")  
        return tokens

#lexer = Lexer("x = 10 + 20; y = x * 2;")
#print(lexer.tokenize())
