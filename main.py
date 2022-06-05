from Lexer import *
from Parser import *
from Interpreter import *

# read the program from file and split in lines
# program = open('Parser_tester.txt', 'r')
program = open('Program_1.txt', 'r')
# program = open('Program_2.txt', 'r')
# program = open('Program_3.txt', 'r')

lines = program.readlines()

lexer = Lexer(lines)
parser = Parser(lexer)
interpreter = Interpreter(parser)
# print the tokens
# print(lexer.lexer_tokens)
# print parser
# print(parser.get_parsed())
interpreter.interpret_parse()

