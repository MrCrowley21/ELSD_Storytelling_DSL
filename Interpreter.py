from Lexer import *
from Parser import *
from Token import *
from Errors import *


class Interpreter:
    def __init__(self, parser):
        self.parsed = parser.get_parsed()

    def interpret_parse(self):
        for p in self.parsed:
            # evaluate entities passed by parser
            p.eval()
        # show the graphical representation of the described flow
        return GraphRepresentation()
