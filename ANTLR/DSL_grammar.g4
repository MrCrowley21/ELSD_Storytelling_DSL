grammar DSL_grammar;

source_code
    : variables_declaration (WHITESPACE)* set_of_affirmations (WHITESPACE)* ('#' comments)*
    | set_of_affirmations
    ;

variables_declaration
    : variable_declaration (WHITESPACE)*
    | variable_declaration (WHITESPACE)* variables_declaration
    ;

variable_declaration
    : TYPE (WHITESPACE)+ variable
    ;

TYPE
    : 'int'
    | 'float'
    | 'string'
    | 'char'
    | 'bool'
    ;

variable
    : identifier
    ;

identifier
    : letter (letter | digit | '_')*
    | '_' (letter | digit | '_')*
    ;

LETTERS
    : [a-z]
    | [A-Z]
    ;

DIGITS
    : [0-9]
    ;

NENULE_DIGITS
    : [1-9]
    ;

letter
    : LETTERS
    ;

digit
    : DIGITS
    ;

nenule_digit
    : NENULE_DIGITS
    ;

set_of_affirmations
    : set_of_affirmation (WHITESPACE)*
    | set_of_affirmation (WHITESPACE)* set_of_affirmations
    ;

set_of_affirmation
    : (act_description (WHITESPACE)*)+ flow_description (WHITESPACE)*
    | variable_attribution (WHITESPACE | set_of_affirmations)*
    | 'if' (WHITESPACE)+ conditions (WHITESPACE)* ':' (WHITESPACE)* set_of_affirmations
    | 'if' (WHITESPACE)+ conditions (WHITESPACE)* ':'(WHITESPACE)* set_of_affirmations 'else' (WHITESPACE)* set_of_affirmations
    | ('while' | 'for') (WHITESPACE)+ conditions (WHITESPACE)* ':' (WHITESPACE)* set_of_affirmations
    | function (WHITESPACE)*
    ;

variable_attribution
    : variable (WHITESPACE)* '=' (WHITESPACE)* (operand | composed_operand) (WHITESPACE)*
    | variable operation (WHITESPACE)* '=' (WHITESPACE)* (operand | composed_operand) (WHITESPACE)*
    ;

act_description
    : 'STORY' (WHITESPACE)+ story ':'
    | 'STAGE' (WHITESPACE)+ stage ':'
    | 'SECTION' (WHITESPACE)+ section ':'
    ;

story
    : variable
    ;

stage
    : variable
    ;

section
    : variable
    ;

flow_description
    : 'FROM' (WHITESPACE)+ ((story | stage | section) '.')* node (WHITESPACE)+ 'TO' (WHITESPACE)* ((story | stage | section) '.')* node (WHITESPACE | flow_description)*
    | 'FROM' (WHITESPACE)+ ((story | stage | section) '.')* node (WHITESPACE)+ 'TO' (WHITESPACE)* ((story | stage | section) '.')* node
    (WHITESPACE)*  'ACTION' ':' (WHITESPACE)* string (flow_description)*
    ;


node
    : variable
    ;

conditions
    : (operand | composed_operand) (WHITESPACE)* condition (WHITESPACE)* (operand | composed_operand) (WHITESPACE)* (('&&' | '||') (WHITESPACE)* conditions)*
    ;

operand
    : variable
    | string
    | nenule_digit (digit)*
    | function
    ;

composed_operand
    : operand ((WHITESPACE)* operation (WHITESPACE)* operand)+
    ;

operation
    : '+'
    | '-'
    | '*'
    | '**'
    | '/'
    | '//'
    | '%'
    ;

function
    : 'nr_nodes' '(' (story | stage | section) ')' (WHITESPACE)*
    | 'nr_sections' '(' (story | stage) ')' (WHITESPACE)*
    | 'nr_stages' '(' story ')' (WHITESPACE)*
    | 'nr_of_interactions' '(' node ')' (WHITESPACE)*
    | 'color' '(' node ')' (WHITESPACE)*
    | 'width' '(' node ')' (WHITESPACE)*
    | 'style' '(' node ')' (WHITESPACE)*
    ;

condition
    : SIGNS
    ;

SIGNS
    : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    | '!='
    | 'in'
    | 'not'
    ;

string
    : characters
    ;

characters
    : '"' ~('"' | '#')* '"'
    ;

comments
    : '#' ~(NEWLINE)
    ;

NEWLINE
    : [\r\n\t]+ -> skip
    ;

WHITESPACE
    : (' ')+
    ;