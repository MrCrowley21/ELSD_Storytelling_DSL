# IDENTIFIERS
IDENTIFIER = 'IDENTIFIER'

# TYPES
STRING = 'STRING'
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
BOOLEAN = 'BOOLEAN'

# DELIMITERS
COMMA = ','
LPARAN = '('
RPARAN = ')'
LBRACE = '{'
RBRACE = '}'
COLON = ':'
DOT = '.'
NEWLINE = '\n'
TAB = '\t'

# OPERATORS
OPERATORS = [

    # ARITHMETIC
    ('PLUS', '+'),
    ('MINUS', '-'),
    ('MULTIPLICATION', '*'),
    ('DIVISION', '/'),
    ('MODULO', '//'),

    # LOGICAL
    ('AND', '&&'),
    ('OR', '||'),
    ('NOT', '!!'),

    # RELATIONAL
    ('ASSIGN', '='),
    ('EQUAL', '=='),
    ('NOT_EQUAL', '!='),
    ('GREATER', '>'),
    ('LESSER', '<'),
    ('GREATER_EQ', '>='),
    ('LESSER_EQ', '<=')
]

# KEYWORDS
KEYWORDS = [
    ('STORY', 'STORY'),
    ('STAGE', 'STAGE'),
    ('SECTION', 'SECTION'),
    ('FROM', 'FROM'),
    ('TO', 'TO'),
    ('ACTION', 'ACTION'),
    ('IN', 'in'),
    ('IF', 'if'),
    ('ELSE', 'else'),
    ('FOR', 'for'),
    ('WHILE', 'while'),
    ('INT', 'int'),
    ('STR', 'string'),
    ('BOOL', 'bool'),
]

# IN BUILT methods
METHODS = [
    ('NR_NODES', 'nr_nodes'),
    ('NR_SECTIONS', 'nr_sections'),
    ('NR_STAGES', 'nr_stages'),
    ('COLOR', 'color'),
    ('STYLE', 'style'),
]

# Define priority

PRIORITY = [
    'LOWEST',  # PRIORITY[0]
    'LOWER',  # PRIORITY[1]
    'LOW',  # PRIORITY[2]
    'HIGH',  # PRIORITY[3]
    'HIGHER',  # PRIORITY[4]
    'HIGHEST'  # PRIORITY[5]
]

# Define precedence

precedence = {
    OPERATORS[0][0]: PRIORITY[3],  # PLUS
    OPERATORS[1][0]: PRIORITY[3],  # MINUS
    OPERATORS[2][0]: PRIORITY[4],  # MULTIPLICATION
    OPERATORS[3][0]: PRIORITY[4],  # DIVISION
    OPERATORS[4][0]: PRIORITY[4],  # MODULO
    OPERATORS[9][0]: PRIORITY[1],  # EQUAL
    OPERATORS[10][0]: PRIORITY[1],  # NOT_EQUAL
    OPERATORS[11][0]: PRIORITY[2],  # GREATER
    OPERATORS[12][0]: PRIORITY[2],  # LESSER
    OPERATORS[13][0]: PRIORITY[2],  # GREATER_EQ
    OPERATORS[14][0]: PRIORITY[2],  # LESSER_EQ
    LPARAN: PRIORITY[5],  # LPARAN
}


def get_precedence(token) -> PRIORITY:
    return precedence.get(token, PRIORITY[0])

# match the token and its type


class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    # specifies output format of tokens
    def __repr__(self):
        if self.value:
            return f'\n{self.token_type} : {self.value}'
        return f'\n{self.token_type}'
