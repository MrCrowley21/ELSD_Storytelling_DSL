from Token import *
from Lexer import *
from Eval_Semantic_analysis import *


class Parser:
    def __init__(self, lexer):
        self.lexer = iter(lexer.lexer_tokens)  # iterator through the tokens passed by lexer
        self.parser = []  # array with the parsed expressions
        self.tab_number = 0  # number of current tabulations
        self.current_token = None  # current analyzed token
        self.next_token = None  # next token to be analyzed
        self.prev_token = None  # previous analyzed token
        # get the first token to be analyzed
        self.__update()
        self.__update()

    # updates the current token
    def __update(self):
        self.prev_token = self.current_token
        self.current_token = self.next_token
        try:
            self.next_token = next(self.lexer)
        except StopIteration:
            if self.next_token != self.current_token:
                self.next_token = self.next_token
            else:
                self.next_token = Token('EOF', 0, 'EOF')

    # check if reach end of file
    def __next__(self) -> Statement:
        while self.current_token.token_type == NEWLINE \
                and self.next_token.token_type == NEWLINE:
            self.__update()
        while self.current_token.token_type != 'EOF':
            if statement := self.__parse_statement():
                self.parser.append(statement)
            else:
                return self.parser

    # check if the type of the following character corresponds to the given one
    def __get_next_type(self, token_type):
        if self.next_token.token_type != token_type:
            raise MyTypeError(self.current_token.line, token_type, self.next_token.token_type)
        self.__update()

    # parse a statement (logical construction)
    def __parse_statement(self) -> Statement:
        if self.prev_token is None and self.current_token.value == NEWLINE or \
                self.current_token.value == NEWLINE and self.prev_token.value == NEWLINE:
            self.__update()
        return self.__parse_variable_declaration() or \
               self.__parse_assign_statement() or \
               self.__parse_while_expression() or \
               self.__parse_if_expression() or \
               self.__parse_story_expression() or \
               self.__parse_stage_expression() or \
               self.__parse_section_expression() or \
               self.__parse_expression_statement()

    # check expressions per lines
    def __parse_expression_statement(self):
        expression = self.__parse_expression(PRIORITY[0])
        if self.next_token.value == NEWLINE:
            self.__update()
            self.__update()
        elif self.next_token.value == 'EOF':
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
            if self.next_token.token_type == 'EOF':
                pass
            else:
                self.__get_next_type('NEWLINE')
            self.__update()
            return VariableDeclarationStatement(self.current_token.line, variable_type, variable, value)

    # parse the references before the name
    def __parse_node_reference(self):
        if self.current_token.token_type == IDENTIFIER:
            reference = self.current_token.value
            self.__update()
            self.__update()
            return NodeReference(self.current_token.line, reference)

    # parse the identifier
    def __parse_identifier(self):
        if self.current_token.token_type == IDENTIFIER:
            return Identifier(self.current_token.line, self.current_token.value)

    # parse the assignment to a variable
    def __parse_assign_statement(self) -> Statement:
        if self.current_token.token_type == IDENTIFIER:
            variable = self.current_token.value
            self.__get_next_type(OPERATORS[8][0])
            self.__update()
            value = self.__parse_expression(PRIORITY[0])
            if self.next_token.token_type == 'EOF':
                self.__update()
            else:
                self.__get_next_type('NEWLINE')
                self.__update()
            return AssignStatement(self.current_token.line, variable, value)

    # helping functions: parse the number of tabs to know if block statement is currently defined
    def __parse_tabs(self):
        if self.prev_token.token_type != 'TAB':
            self.tab_number = 0
        while self.current_token.token_type == 'TAB':
            self.__update()
            self.tab_number += 1

    # parse the block of expressions/statements in statement
    def __parse_block_statement(self) -> Statement:
        self.tab_number += 1
        block_tab_number = self.tab_number
        block = []
        while block_tab_number == self.tab_number:
            self.__parse_tabs()
            if self.tab_number == block_tab_number:
                statement = self.__parse_statement()
                block.append(statement)
            if self.tab_number > block_tab_number:
                raise MySyntaxError(self.current_token.line, "Indentation required")
        return BlockStatement(block)

    # parse the block statement for the story frame
    def __parse_block_story_statement(self) -> Statement:
        self.tab_number += 1
        block_tab_number = self.tab_number
        block = []
        while block_tab_number == self.tab_number:
            self.__parse_tabs()
            if self.tab_number == block_tab_number:
                if self.current_token.value in ['FROM', 'STAGE', 'SECTION']:
                    statement = self.__parse_node_expression() or \
                                self.__parse_section_expression() or \
                                self.__parse_stage_expression()
                    block.append(statement)
                else:
                    raise MySyntaxError(self.current_token.line, 'Not a flow description')
            if self.tab_number > block_tab_number:
                raise MySyntaxError(self.current_token.line, 'Too much indented text')
        return BlockStatement(block)

    # parse the block statement for the section frame
    def __parse_block_section_statement(self) -> Statement:
        self.tab_number += 1
        block_tab_number = self.tab_number
        block = []
        while block_tab_number == self.tab_number:
            self.__parse_tabs()
            if self.tab_number == block_tab_number:
                if self.current_token.value == 'FROM':
                    statement = self.__parse_node_expression()
                    block.append(statement)
                else:
                    raise MySyntaxError(self.current_token.line, 'Not a flow description')
            if self.tab_number > block_tab_number:
                raise MySyntaxError(self.current_token.line, 'Too much indented text')
        return BlockStatement(block)

    # parse the block statement for the stage frame
    def __parse_block_stage_statement(self) -> Statement:
        self.tab_number += 1
        block_tab_number = self.tab_number
        block = []
        while block_tab_number == self.tab_number:
            self.__parse_tabs()
            if self.tab_number == block_tab_number:
                if self.current_token.value in ['FROM', 'SECTION']:
                    statement = self.__parse_node_expression() or \
                                self.__parse_section_expression()
                    block.append(statement)
                else:
                    raise MySyntaxError(self.current_token.line, 'Not a flow description')
            if self.tab_number > block_tab_number:
                raise MySyntaxError(self.current_token.line, 'Too much indented text')
        return BlockStatement(block)

    # parse any type of expression
    def __parse_expression(self, precedent: PRIORITY) -> Expression:
        expression = self.__parse_datatypes() or \
                     self.__parse_nr_nodes_method() or \
                     self.__parse_nr_sections_method() or \
                     self.__parse_nr_stages_method() or \
                     self.__parse_color_method() or \
                     self.__parse_identifier() or \
                     self.__parse_node_expression() or \
                     self.__parse_unary() or \
                     self.__parse_group()
        if expression is None:
            raise MySyntaxError(self.current_token.line, 'Operand is not defined')
        while self.next_token.value != NEWLINE and self.next_token.value != COLON \
                and self.current_token.value != 'EOF' and self.next_token.value != 'EOF' \
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
            return Literal(self.current_token.line, self.current_token.token_type, self.current_token.value)

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
            return NormalExpression(self.current_token.line, left, operator, right)

    # parse the story frame declaration
    def __parse_story_expression(self) -> Expression:
        if self.current_token.value == 'STORY':
            frame_type = 'STORY'
            self.__update()
            name = self.__parse_identifier()
            self.__get_next_type('COLON')
            self.__get_next_type('NEWLINE')
            self.__update()
            if self.current_token.token_type != 'TAB':
                raise MySyntaxError(self.current_token.line, 'Indentation required')
            flow = self.__parse_block_story_statement()
            return FlowFrame(self.current_token.line, frame_type, name, flow)

    # parse the section frame declaration
    def __parse_section_expression(self) -> Expression:
        if self.current_token.value == 'SECTION':
            frame_type = 'SECTION'
            self.__update()
            name = self.__parse_identifier()
            self.__get_next_type('COLON')
            self.__get_next_type('NEWLINE')
            self.__update()
            if self.current_token.token_type != 'TAB':
                raise MySyntaxError(self.current_token.line, 'Indentation required')
            flow = self.__parse_block_section_statement()
            return FlowFrame(self.current_token.line, frame_type, name, flow)

    # parse the stage frame declaration
    def __parse_stage_expression(self) -> Expression:
        if self.current_token.value == 'STAGE':
            frame_type = 'STAGE'
            self.__update()
            name = self.__parse_identifier()
            self.__get_next_type('COLON')
            self.__get_next_type('NEWLINE')
            self.__update()
            if self.current_token.token_type != 'TAB':
                raise MySyntaxError(self.current_token.line, 'Indentation required')
            flow = self.__parse_block_stage_statement()
            return FlowFrame(self.current_token.line, frame_type, name, flow)

    # parse if statements
    def __parse_if_expression(self) -> Expression:
        block_expression = 'if'
        if self.current_token.value == 'if':
            self.__update()
            condition = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('COLON')
            self.__get_next_type('NEWLINE')
            self.__update()
            if self.current_token.token_type != 'TAB':
                raise MySyntaxError(self.current_token.line, 'Indentation required')
            if_condition = self.__parse_block_statement()
            if_not_condition = None
            if self.current_token.token_type == 'TAB':
                self.__update()
            if self.current_token.value == 'else':
                block_expression = 'else'
                self.__get_next_type('COLON')
                self.__get_next_type('NEWLINE')
                self.__update()
                if_not_condition = self.__parse_block_statement()
            return IfStatement(condition, if_condition, if_not_condition)

    # parse while statements
    def __parse_while_expression(self) -> Expression:
        if self.current_token.value == 'while':
            self.__update()
            condition = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('COLON')
            self.__get_next_type('NEWLINE')
            self.__update()
            if self.current_token.token_type != 'TAB':
                raise MySyntaxError(self.current_token.line, 'Indentation required')
            block = self.__parse_block_statement()
            return WhileStatement(condition, block)

    # parse the nodes of the graph
    def __parse_node_expression(self) -> Expression:
        if self.current_token.value == 'FROM':
            self.__update()
            from_node_reference = []
            to_node_reference = []
            while self.next_token.value == DOT:
                from_node_reference += [self.__parse_node_reference()]
            from_node = self.__parse_identifier()
            self.__get_next_type('KEYWORDS[TO]')
            self.__update()
            while self.next_token.value == DOT:
                to_node_reference += [self.__parse_node_reference()]
            to_node = self.__parse_identifier()
            action = None
            if self.next_token.token_type == 'KEYWORDS[ACTION]':
                self.__update()
                self.__get_next_type('COLON')
                self.__get_next_type('STRING')
                action = self.current_token.value
            self.__update()
            self.__update()
            return NodesExpression(self.current_token.line, from_node, from_node_reference,
                                   to_node, to_node_reference, action)

    # parse the method "nr_nodes()"
    def __parse_nr_nodes_method(self) -> Expression:
        if self.current_token.token_type == 'IN_BUILT_FUN[NR_NODES]':
            self.__get_next_type('LPARAN')
            self.__update()
            reference = []
            while self.next_token.value == DOT:
                reference += [self.__parse_node_reference()]
            variable = self.__parse_identifier()
            self.__get_next_type('RPARAN')
            return NrNodeMethod(self.current_token.line, reference, variable)

    # parse the method "nr_sections()"
    def __parse_nr_sections_method(self) -> Expression:
        if self.current_token.token_type == 'IN_BUILT_FUN[NR_SECTIONS]':
            self.__get_next_type('LPARAN')
            self.__update()
            reference = []
            while self.next_token.value == DOT:
                reference += [self.__parse_node_reference()]
            variable = self.__parse_identifier()
            self.__get_next_type('RPARAN')
            return NrSectionMethod(self.current_token.line, reference, variable)

    # parse the method "nr_stages()"
    def __parse_nr_stages_method(self) -> Expression:
        if self.current_token.token_type == 'IN_BUILT_FUN[NR_STAGES]':
            self.__get_next_type('LPARAN')
            self.__update()
            reference = []
            while self.next_token.value == DOT:
                reference += [self.__parse_node_reference()]
            variable = self.__parse_identifier()
            self.__get_next_type('RPARAN')
            return NrStageMethod(self.current_token.line, reference, variable)

    # parse the method "color()"
    def __parse_color_method(self) -> Expression:
        if self.current_token.token_type == 'IN_BUILT_FUN[COLOR]':
            self.__get_next_type('LPARAN')
            self.__update()
            reference = []
            while self.next_token.value == DOT:
                reference += [self.__parse_node_reference()]
            variable = self.__parse_identifier()
            self.__get_next_type('COMMA')
            self.__update()
            color = self.__parse_expression(PRIORITY[0])
            self.__get_next_type('RPARAN')
            return ColorMethod(self.current_token.line, reference, variable, color)

    # parse the negative negations and opposite of a number
    def __parse_unary(self):
        if self.current_token.token_type in [OPERATORS[1][0], OPERATORS[7][0]]:
            operator = self.current_token.value
            precedent = get_precedence(self.current_token)
            self.__update()
            right = self.__parse_expression(PRIORITY[4])
            return PrefixExpression(self.current_token.line, operator, right)
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
