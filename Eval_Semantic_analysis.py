import math
import numpy as np
import networkx as nx
import random
from networkx import nx_pydot
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from typing import List
from copy import deepcopy
from networkx import is_directed_acyclic_graph

from Token import *
from Lexer import *


class Node: ...


class Statement(Node): ...


class Expression(Node): ...


identifiers = {}  # keeps the information about the existing identifiers
nodes = {}  # keeps the information about the existing nodes; frames included
methods = [i[1] for i in METHODS]  # keeps the names of the existing methods
frame_names = set()  # keeps the name of the existing frames
edge_list = []  # keeps the described edges
label_list = []  # keeps the actions of specific edges if exist
node_list = set()  # list of names of existing nodes
section_list = set()  # list of names of existing sections
stage_list = set()  # list of names of existing stages
story_list = set()  # list of names of existing stories
color_map = []  # keeps the color of a specific node
current_dictionary = [nodes]  # define the current frame to be described
current_frame = ['']  # keeps the name of the current frame
frame_count = [0]  # keeps the "depth" of the current frame
G = nx.DiGraph()  # initializing the graph
colors = ['white', 'red', 'blue', 'yellow', 'green', 'black']  # default define colors


# describes literals
class Literal(Expression):
    def __init__(self, token_type: str, value: str):
        self.type = token_type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __get_type(self):
        if self.type == INTEGER:
            return int(self.value)
        elif self.type == FLOAT:
            return float(self.value)
        elif self.type == STRING:
            return str(self.value)
        elif self.type == BOOLEAN:
            if self.value == 'true':
                return True
            else:
                return False
        else:
            return None

    def eval(self):
        try:
            literal_type = self.__get_type()
        except ValueError:
            raise ValueError(f'Error converting {self.value} to {self.type}')
        return literal_type


# descries identifiers
class Identifier(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def eval(self):
        if self.name in identifiers:
            return identifiers[self.name][0]
        else:
            raise NameError(f'{self.name} is not defined')


# describes node references
class NodeReference(Expression):
    def __init__(self, reference):
        self.reference = reference

    def __repr__(self) -> str:
        return self.reference

    def eval(self):
        if self.reference in identifiers:
            return identifiers[self.reference][0]
        else:
            raise NameError(f'{self.name} is not defined')


# describes variable declaration statements
class VariableDeclarationStatement(Statement):
    def __init__(self, variable_type: str, name: Identifier, value: Expression):
        self.variable_type = variable_type
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f'({self.variable_type} {self.name} {self.value})'

    def eval(self):
        if self.name in identifiers or self.name in frame_names or str(self.name) in methods:
            raise NameError(f'"{self.name}" is already defined')
        if self.value is not None:
            identifiers[self.name] = [self.value.eval(), self.variable_type]
        else:
            identifiers[self.name] = [None, self.variable_type]


# describes flow description
class NodesExpression(Statement):
    def __init__(self, from_node: Identifier, from_node_reference,
                 to_node: Identifier, to_node_reference, action: str):
        self.from_node = str(from_node)
        self.to_node = str(to_node)
        self.action = action
        self.from_node_reference = from_node_reference
        self.to_node_reference = to_node_reference

    def __repr__(self) -> str:
        return f'(nodes ({self.from_node}) ({self.to_node}) (description ({self.action})))'

    # check if one of possible node names is in a given list
    def __check_node(self, first_list, second_list):
        is_node = False
        for i in first_list:
            if i in second_list:
                is_node = True
        return is_node

    # check and name the node with refference if the case
    def __define_node_reference(self, node, node_reference, reference):
        i = 0
        length = len(node_reference)
        while i < length:
            reference[0] = reference[0][str(node_reference[i])]
            i += 1
        if node not in reference[0]:
            if str(node_reference[-1]) + '.' + str(node) not in reference[0]:
                raise SyntaxError('Not a valid node')
            else:
                node = str(node_reference[-1]) + '.' + str(node)
        return node

    # define the node name and check where it belongs
    def __define_node(self, node, node_reference, possible_names, reference):
        if self.__check_node(possible_names, node_list) and \
                not self.__check_node([str(node), str(current_frame[0]) + '.' + str(node)], current_dictionary[0]):
            try:
                if len(node_reference) > 0:
                    node = self.__define_node_reference(node, node_reference, reference)
                else:
                    node = str(current_frame[0]) + '.' + str(node)
            except KeyError:
                raise KeyError('Not a valid path')
        elif len(node_reference) > 0 and self.__check_node(possible_names, node_list) and \
                not self.__check_node([str(node), str(node_reference[-1]) + '.' + str(node)], current_dictionary[0]):
            try:
                node = self.__define_node_reference(node, node_reference, reference)
            except KeyError:
                raise ValueError('Not a valid path')
        elif self.__check_node([str(node), str(current_frame[0]) + '.' + str(node)], current_dictionary[0]):
            if node not in current_dictionary[0]:
                node = str(current_frame[0]) + '.' + str(node)
        return node

    def eval(self):
        reference = [nodes]  # define evaluated frame
        # define possible name of the source node
        possible_names = [str(self.from_node), str(current_frame[0]) + '.' + str(self.from_node)]
        # define possible name of the destination node
        possible_to_names = [str(self.to_node), str(current_frame[0]) + '.' + str(self.to_node)]

        # define all possible name for source and destination nodes
        if len(self.from_node_reference) > 0:
            possible_names.append(str(self.from_node_reference[-1]) + '.' + str(self.from_node))
        if len(self.to_node_reference) > 0:
            possible_to_names.append(str(self.to_node_reference[-1]) + '.' + str(self.to_node))

        # determine the name for the source and destination nodes
        self.from_node = self.__define_node(self.from_node, self.from_node_reference, possible_names, reference)
        self.to_node = self.__define_node(self.to_node, self.to_node_reference, possible_to_names, reference)

        # append the source node to the frame it belongs
        # initialize the name in dictionary if new name
        if self.from_node not in current_dictionary[0] and len(self.from_node_reference) == 0:
            current_dictionary[0][self.from_node] = {}
            color_map.append('white')
        # check the path not to be already described
        if self.from_node in current_dictionary[0] and self.to_node in current_dictionary[0][self.from_node]:
            raise SyntaxError(f'This path is already described')
        # do not append node to the current frame if belongs to another frame
        elif len(self.from_node_reference) != 0:
            G.add_edge(self.from_node, self.to_node)
            edge_list.append((self.from_node, self.to_node))
            if self.action is not None:
                label_list.append(((self.from_node, self.to_node), self.action))
        # append the node to the current frame if the case
        else:
            current_dictionary[0][self.from_node][self.to_node] = self.action
            G.add_edge(self.from_node, self.to_node)
            edge_list.append((self.from_node, self.to_node))
            if self.action is not None:
                label_list.append(((self.from_node, self.to_node), self.action))

        # append the destination node to the frame it belongs
        # initialize the name in dictionary if new name
        if self.to_node not in current_dictionary[0] and len(self.to_node_reference) == 0:
            current_dictionary[0][self.to_node] = {}
            color_map.append('white')
        # check the path not to be already described
        if self.to_node in current_dictionary[0] and self.from_node in current_dictionary[0][self.to_node]:
            raise SyntaxError(f'This path is already described')
        # do not append node to the current frame if belongs to another frame
        elif len(self.to_node_reference) != 0 and self.to_node not in node_list:
            pass
        # append the node to the current frame if the case
        elif len(self.to_node_reference) == 0:
            current_dictionary[0][self.to_node][self.from_node] = self.action

        # add the nodes to the list of nodes
        node_list.add(self.from_node)
        node_list.add(self.to_node)


# describes variable assignment statement
class AssignStatement(Statement):
    def __init__(self, name: str, value: Expression):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f'({self.name} {self.value})'

    def eval(self):
        instances = {
            'int': int,
            'bool': bool,
            'float': float,
            'string': str
        }

        if self.name not in identifiers:
            raise NameError(f' "{self.name}" is not defined')
        result = self.value.eval()
        if (type(result) == type(True) or type(result) == type(False)) and identifiers[self.name][1] != 'bool':
            raise ValueError(f'Error converting {result} to {identifiers[self.name][1]}')
        elif isinstance(result, (instances[identifiers[self.name][1]])):
            identifiers[self.name][0] = result
        else:
            raise ValueError(f'Error converting {result} to {identifiers[self.name][1]}')


# describes the block of more expressions/statements in a statement
class BlockStatement(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def __repr__(self) -> str:
        data = ''
        for x in self.statements:
            data += x.__repr__()
        return f'({data})'

    def eval(self):
        for x in self.statements:
            data = x.eval()


# describes the block of statements that describes flows from the given frame
class FlowFrame(Statement):
    def __init__(self, frame_type, name, flow: BlockStatement):
        self.frame_type = frame_type
        self.name = name
        self.flow = flow

    def __repr__(self) -> str:
        return f'({self.frame_type} ({self.name} ({self.flow})))'

    def eval(self):
        if str(self.name) not in frame_names and str(self.name) not in identifiers:
            if self.frame_type == 'SECTION':
                section_list.add(str(self.name))
            elif self.frame_type == 'STAGE':
                stage_list.add(str(self.name))
            elif self.frame_type == 'STORY':
                story_list.add(str(self.name))
            frame_names.add(str(self.name))
            new_dictionary = [current_dictionary[0]]
            prev_frame = [current_frame[0]]
            current_frame[0] = str(self.name)
            if self.name not in current_dictionary[0]:
                current_dictionary[0][str(self.name)] = {}
                current_dictionary[0] = current_dictionary[0][str(self.name)]
            self.flow.eval()
            current_dictionary[0] = new_dictionary[0]
            current_frame[0] = prev_frame[0]
            frame_count[0] += 1
        else:
            raise NameError(f'"{self.name}" is already defined')


# describes if statements
class IfStatement(Statement):
    def __init__(self, condition, if_condition: BlockStatement, if_not_condition: BlockStatement):
        self.condition = condition
        self.if_condition = if_condition
        self.if_not_condition = if_not_condition

    def __repr__(self) -> str:
        return f'(if ({self.condition}) ({self.if_condition}) ({self.if_not_condition}))'

    def eval(self):
        if self.condition.eval():
            self.if_condition.eval()
        else:
            self.if_not_condition.eval() if self.if_not_condition else None


# describes while statements
class WhileStatement(Statement):
    def __init__(self, condition: Expression, action: Statement):
        self.condition = condition
        self.action = action

    def __repr__(self) -> str:
        return f'(while ({self.condition}) ({self.action}))'

    def eval(self):
        while self.condition.eval():
            self.action.eval()


# describes "nr_nodes()" method
class NrNodeMethod(Expression):
    def __init__(self, reference, variable: Identifier):
        self.reference = reference
        self.variable = variable

    def __repr__(self):
        return f'(nr_nodes ({self.variable}))'

    # count the nodes in the current frame
    def __count_nodes(self, location, node_count):
        for entity in location:
            if str(entity) in node_list:
                node_count += 1
            # count the nodes from the frame in the current frame
            else:
                node_count = self.__count_nodes(location[str(entity)], node_count)
        return node_count

    def eval(self):
        node_count = 0
        location = [nodes]
        if str(self.variable) in node_list or \
                len(self.reference) > 0 and str(self.reference[-1]) + '.' + str(self.variable) in node_list:
            raise SyntaxError('Argument must be of frame type')
        try:
            for ref in self.reference:
                location[0] = location[0][str(ref)]
        except KeyError:
            raise KeyError('Not a valid reference')
        try:
            node_count = self.__count_nodes(location[0][str(self.variable)], 0)
        except KeyError:
            raise KeyError('Not a valid reference')
        return node_count


# describes "nr_sections()" method
class NrSectionMethod(Expression):
    def __init__(self, reference, variable: Identifier):
        self.reference = reference
        self.variable = variable

    def __repr__(self):
        return f'(nr_nodes ({self.variable}))'

    # count the sections in the current frame
    def __count_sections(self, location, section_count):
        for entity in location:
            if str(entity) in section_list:
                section_count += 1
            # count the sections from the frame in the current frame
            elif str(entity) in stage_list or str(entity) in story_list:
                section_count = self.__count_sections(location[str(entity)], section_count)
        return section_count

    def eval(self):
        section_count = 0
        location = [nodes]
        if str(self.variable) in section_list or str(self.variable) in node_list:
            raise SyntaxError('Argument must be of type "STAGE" or "STORY"')
        try:
            for ref in self.reference:
                location[0] = location[0][str(ref)]
        except KeyError:
            raise KeyError('Not a valid reference')
        try:
            section_count = self.__count_sections(location[0][str(self.variable)], 0)
        except KeyError:
            raise KeyError('Not a valid reference')
        return section_count


# describes "nr_stages()" method
class NrStageMethod(Expression):
    def __init__(self, reference, variable: Identifier):
        self.reference = reference
        self.variable = variable

    def __repr__(self):
        return f'(nr_nodes ({self.variable}))'

    # count the stages in the current frame
    def __count_stages(self, location, stage_count):
        for entity in location:
            if str(entity) in stage_list:
                stage_count += 1
            elif str(entity) in story_list:
                stage_count = self.__count_stages(location[str(entity)], stage_count)
        return stage_count

    def eval(self):
        stage_count = 0
        location = [nodes]
        if str(self.variable) in stage_list or str(self.variable) in section_list or str(self.variable) in node_list:
            raise SyntaxError('Argument must be of type "STORY"')
        try:
            for ref in self.reference:
                location[0] = location[0][str(ref)]
        except KeyError:
            raise KeyError('Not a valid reference')
        try:
            stage_count = self.__count_stages(location[0][str(self.variable)], 0)
        except KeyError:
            raise KeyError('Not a valid reference')
        return stage_count


# describes "color()" method
class ColorMethod(Expression):
    def __init__(self, reference, variable: Identifier, color):
        self.reference = reference
        self.variable = variable
        self.color = color

    def __repr__(self):
        return f'(color ({self.variable} {self.color}))'

    # assign the chosen color to the specified node/s
    def __color_node(self, location, graph_nodes, color):
        for node in location:
            # assign the color to the current node
            if node in node_list:
                color_map[graph_nodes.index(str(node))] = color
            # assign the color to all the nodes in the frame of the curent frame
            else:
                self.__color_node(location[str(node)], graph_nodes, color)

    def eval(self):
        if not isinstance(self.color, str):
            color = self.color.eval()
        new_color = ""
        if isinstance(color, int):
            new_color = colors[color % 6]
        else:
            new_color = color
        location = [nodes]
        try:
            for ref in self.reference:
                location[0] = location[0][str(ref)]
        except KeyError:
            raise KeyError('Not a valid reference')
        if str(self.variable) not in location[0]:
            self.variable = str(self.reference[-1]) + '.' + str(self.variable)
        try:
            graph_nodes = list(G.nodes())
            if str(self.variable) in node_list:
                color_map[graph_nodes.index(str(self.variable))] = new_color
            else:
                self.__color_node(location[0][str(self.variable)], graph_nodes, new_color)
        except KeyError:
            raise KeyError('Not a valid reference')


# describes negation or opposite number usage
class PrefixExpression(Expression):
    def __init__(self, operator: Statement, right: Expression):
        self.operator = operator
        self.right = right

    def __get_type(self) -> str:
        return self.type.right

    def __repr__(self) -> str:
        return f'({self.operator}{self.right})'

    def eval(self):
        operator = {
            '!': lambda a: not a,
            '-': lambda a: -a,
            '+': lambda a: a,
        }
        try:
            return operator[self.operator](self.right.eval())
        except TypeError:
            raise TypeError(f'Operator {self.operator} is not used in this scope')


# describes expressions with two operands
class NormalExpression(Expression):
    def __init__(self, left: Expression, operator: Statement, right: Expression):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self) -> str:
        return f'({self.left} {self.operator} {self.right})'

    def eval(self):
        operator = {

            # arithmetic operations
            '//': lambda a, b: a % b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '&&': lambda a, b: a and b,
            '||': lambda a, b: a or b,

            #  conditional operations
            '==': lambda a, b: a == b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
        }

        try:
            return operator[self.operator](self.left.eval(), self.right.eval())
        except TypeError:
            raise TypeError(f'Cannot perform "{self.operator}" between '
                            f'{identifiers[str(self.left)][1]} and {identifiers[str(self.right)][1]}')


# describes the graph representation of the described flow
class GraphRepresentation:
    def __init__(self):
        if is_directed_acyclic_graph(G):
            self.__drawGraph()
        else:
            raise SyntaxError('There are cycles in your storytelling')

    # define the size of the node according to its name
    def __node_size(self, i):
        return len(i) ** 1.7 * 60

    # define the positions of the nodes according to the frames they belongs
    def __define_node_positions(self, frame, position, pos, rad, rad_dividing_coeff, first_coef, second_coef):
        graph_nodes = G.nodes()
        angs = np.linspace(first_coef, second_coef * np.pi, frame_count[0] + 2)
        repos = []
        for i in angs:
            if i > 0:
                repos.append(np.array([(rad / rad_dividing_coeff) * np.cos(i), (rad / rad_dividing_coeff) * np.sin(i)]))
        for entity in frame:
            if str(entity) in graph_nodes:
                pos[entity] = (pos[entity] + repos[position]) * rad
            else:
                if entity in nodes:
                    position += 1
                pos = deepcopy(self.__define_node_positions
                               (frame[str(entity)], position, pos, rad / 1.35, rad_dividing_coeff / 0.02,
                                first_coef - 1, second_coef + 0.5))
        return pos

    # define the color for the nodes border
    def __define_edgecolors(self):
        edgecolor = []
        for i in range(len(G.nodes())):
            edgecolor.append("black")
        edgecolor[0] = "red"
        return edgecolor

    # draw the graph that represents te described flow
    def __drawGraph(self):
        # f, ax = plt.subplots(1, 1)
        # pos = nx.spring_layout(G, k=10 / math.sqrt(G.order()))
        # pos = nx.circular_layout(G, scale=0.1)
        initial_pos = nx.circular_layout(G, scale=0.35, center=(0, 0))
        pos = self.__define_node_positions(nodes, 0, initial_pos, 60, 55, 3, 1.25)
        options = {"node_color": color_map,
                   "node_size": [self.__node_size(i) for i in pos], "alpha": 0.8, "font_size": 7}
        edgecolor = self.__define_edgecolors()
        nx.draw_networkx(G, pos, edgelist=edge_list, width=1, edgecolors=edgecolor, **options)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=dict(label_list), font_size=7, font_family='sans-serif',
                                     label_pos=0.5)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
