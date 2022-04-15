from Lexer import *
from Parser import *
from Token import *
from Errors import *

class Interpreter:
    def __init__(self, parser):
        self.parsed = parser.get_parsed()

    def interpret_parse(self):
        for p in self.parsed:
            p.eval()
