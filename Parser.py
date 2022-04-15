from Token import *
from Lexer import *
from Eval_Semantic_analysis import *


class Parser:
    def __init__(self, lexer):
        self.lexer = iter(lexer.lexer_tokens)
        self.parser = []
        self.tab_number = 0
        self.block_tab_number = 0
        self.current_token = None
        self.next_token = None
        self.__update()
        self.__update()

    # updates the current token
    def __update(self):
        self.current_token = self.next_token
        try:
            self.next_token = next(self.lexer)
        except StopIteration:
            self.next_token = 'EOF'

    # check if reach end of file
    def __next__(self) -> Statement:
        while self.current_token != 'EOF':
            if statement := self.parse_statement():
                self.parser.append(statement)
            else:
                return self.parser

    # check if the type of the following character corresponds to the given one
    def __get_next_type(self, token_type):
        if self.next_token.token_type != token_type:
            raise AssertionError(f'expected type {token_type}. Got type {self.next_token.token_type}')
        self.__update()

    # parse a statement (logical construction)
    def parse_statement(self) -> Statement:
        self.tab_number = 0
        if self.next_token != 'EOF':
            while self.next_token.token_type == 'TAB':
                self.tab_number += 1
                self.__update()
        return self.__parse_variable_declaration() or \
               self.__parse_assign_statement() or \
               self.__parse_while_expression() or \
               self.__parse_if_expression() or\
               self.__parse_expression_statement()

    # check expressions per lines
    def __parse_expression_statement(self):
        # self.tab_number = 0
        # while self.current_token.token_type == 'TAB':
        #     self.tab_number += 1
        #     self.__update()
        expression = self.__parse_expression(PRIORITY[0])
        if self.next_token.value == NEWLINE:
            self.__update()
            self.__update()
        return expression

    # parse the declared variable
    def __parse_variable_declaration(self) -> Statement:
        declaration_types = ['int', 'float', 'bool', 'string']
        if self.current_token.value in declaration_types:
            variable_type = self.current_token.value
            self.__get_next_type(IDENTIFIER)
            variable = self.current_token.value
            if self.next_token.token_type == OPERATORS[8][0]:
                self.__get_next_type(OPERATORS[8][0])
                self.__update()
                value = self.__parse_expression(PRIORITY[0])
            else:
                value = None
            self.__get_next_type('NEWLINE')
            self.__update()
            return VariableDeclarationStatement(variable_type, variable, value)

    # parse the identifier
    def __parse_identifier(self):
        if self.current_token.token_type == IDENTIFIER:
            return Identifier(self.current_token.value)

    # parse the assignment to a variable
    def __parse_assign_statement(self) -> Statement:
        if self.current_token.token_type == IDENTIFIER:
            variable = self.current_token.value
            self.__get_next_type(OPERATORS[8][0])
            self.__update()
            value = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('NEWLINE')
            self.__update()
            return AssignStatement(variable, value)

    # parse the block of expressions/statements in statement
    def __parse_block_statement(self) -> Statement:
        self.block_tab_number = self.tab_number
        block = []
        while self.block_tab_number == self.tab_number:
            print(self.block_tab_number, self.tab_number, self.current_token, self.next_token)
            statement = self.parse_statement()
            block.append(statement)
        else:
            self.__update()
        return BlockStatement(block)

    # parse any type of expression
    def __parse_expression(self, precedent: PRIORITY) -> Expression:
        expression = self.__parse_datatypes() or \
                     self.__parse_identifier() or \
                     self.__parse_node_expression() or \
                     self.__parse_unary() or \
                     self.__parse_group
        if expression is None:
            raise SyntaxError(f'Operand is not defined')
        while self.next_token.value != NEWLINE and self.next_token.value != COLON \
                and PRIORITY.index(precedent) <= PRIORITY.index(get_precedence(self.next_token)):
            if new_expression := self.__parse_normal_expression(expression):
                expression = new_expression
            else:
                break
        return expression

    # parse datatypes
    def __parse_datatypes(self):
        datatypes = [
            INTEGER,
            FLOAT,
            STRING,
            BOOLEAN,
        ]
        if self.current_token.token_type in datatypes:
            return Literal(self.current_token.token_type, self.current_token.value)

    # parse expressions with two operands
    def __parse_normal_expression(self, left: Expression) -> Expression:
        operators = [
            'PLUS',
            'MINUS',
            'MULTIPLICATION',
            'DIVISION',
            'MODULO',
            'EQUAL',
            'AND',
            'OR',
            'NOT',
            'GREATER', 'GREATER_EQ',
            'LESSER', 'LESSER_EQ',
        ]
        if self.next_token.token_type in operators:
            self.__update()
            operator = self.current_token.value
            precedent = get_precedence(self.current_token)
            self.__update()
            right = self.__parse_expression(precedent)
            return NormalExpression(left, operator, right)

    # parse if statements
    def __parse_if_expression(self) -> Expression:
        self.tab_number = 0
        while self.current_token.token_type == 'TAB':
            self.tab_number += 1
            self.__update()
        if self.current_token.value == 'if':
            self.__update()
            condition = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('COLON')
            self.__update()
            if_condition = self.__parse_block_statement()
            if_not_condition = None
            if self.current_token.value == 'else':
                self.__get_next_type('COLON')
                self.__update()
                if_not_condition = self.__parse_block_statement()
            return IfStatement(condition, if_condition, if_not_condition)

    # parse while statements
    def __parse_while_expression(self) -> Expression:
        self.tab_number = 0
        while self.current_token.token_type == 'TAB':
            self.tab_number += 1
            self.__update()
        if self.current_token.value == 'while':
            self.__update()
            condition = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('COLON')
            self.__update()
            block = self.__parse_block_statement()
            return WhileStatement(condition, block)

    # parse the nodes of the graph
    def __parse_node_expression(self):
        self.tab_number = 0
        while self.current_token.token_type == 'TAB':
            self.tab_number += 1
            self.__update()
        if self.current_token.value == 'FROM':
            self.__update()
            from_node = self.__parse_identifier()
            self.__get_next_type('KEYWORDS[TO]')
            self.__update()
            to_node = self.__parse_identifier()
            action = None
            if self.next_token.token_type == 'KEYWORDS[ACTION]':
                self.__update()
                self.__get_next_type('COLON')
                self.__update()
                action = self.current_token.value
            return NodesExpression(from_node, to_node, action)

    # parse the negative negations and opposite of a number
    def __parse_unary(self):
        if self.current_token.token_type in [OPERATORS[1][0], OPERATORS[7][0]]:
            operator = self.current_token.value
            precedent = get_precedence(self.current_token)
            self.__update()
            right = self.__parse_expression(PRIORITY[4])
            return PrefixExpression(operator, right)
        elif self.current_token.token_type == 'LPARAN':
            self.__update()
            expression = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('RPARAN')
            return expression

    # parse a group of expressions
    def __parse_group(self):
        if self.current_token.token_type == 'LPARAN':
            self.__update()
            expression = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('RPARAN')
            return expression

    # return the list of parsed statements
    def get_parsed(self):
        self.__next__()
        return self.parser
