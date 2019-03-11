# Lexer for defininf all Tokens

import ply.lex as lex
import sys

# Tokens of Symbols and Regex Patterns
tokens = [
  'ID',                     # ID's
  'CLASS_ID',
  'FUNCTION_ID',
  'UNDERSCORE',             # Underscore
  'INT_CONST',              # Constant Values
  'FLOAT_CONST',
  'CHAR_CONST',
  'STRING_CONST',
  'MINUS',                  # Arithmetic Operators
  'MULTIPLY',
  'PLUS',
  'DIVIDE',
  'AND',                    # Logic Operators
  'OR',
  'EQUAL_EQUAL',
  'DIFFERENT_FROM',
  'MORE_EQUAL',
  'LESS_EQUAL',
  'MORE_THAN',
  'LESS_THAN',
  'EQUAL',
  'NOT',
  'OPEN_PARENTHESIS',        # Parenthesis
  'CLOSE_PARENTHESIS',             
  'OPEN_BRACKET',
  'CLOSE_BRACKET',
  'PERCENTAGE',              # Comments
  'DOT',                     # Assignation and Calls
  'COMMA',
  'DOUBLE_DOT',
  'SINGLE_QUOTE',            # Strings and Chars
  'DOUBLE_QUOTE',
]

# Tokens of Reserved Words
reserved = {
  'int'        : 'INT',
  'flo'        : 'FLO',
  'boo'        : 'BOO',
  'cha'        : 'CHA',
  'str'        : 'STR',
  'fun'        : 'FUN',
  'is'         : 'IS',
  'void'       : 'VOID',
  'true'       : 'TRUE',
  'false'      : 'FALSE',
  'with'       : 'WITH',
  'end'        : 'END',
  'in'         : 'IN',
  'out'        : 'OUT',
  'if'         : 'IF',
  'elsif'      : 'ELSIF',
  'else'       : 'ELSE',
  'lis'        : 'LIS',
  'pop'        : 'POP',
  'push'       : 'PUSH',
  'empty'      : 'EMPTY',
  'flip'       : 'FLIP',
  'join'       : 'JOIN',
  'size'       : 'SIZE',
  'litaf'      : 'LITAF',
  'start'      : 'START',
  'loop'       : 'LOOP',
  'from'       : 'FROM',
  'to'         : 'TO',
  'by'         : 'BY',
  'until'      : 'UNTIL',
  'do'         : 'DO',
  'new'        : 'NEW',
  'public'     : 'PUBLIC',
  'private'    : 'PRIVATE',
  'class'      : 'CLASS',
  'attributes' : 'ATTRIBUTES',
  'methods'    : 'METHODS'
}

# Define simple terminal tokens

t_COMMA = r'\,'
t_DOUBLEDOT = r'\:'
t_EQUAL = r'\='
t_DIFFERENT_FROM = r'\!\='
t_LESS_THAN = r'\<'
t_MORE_THAN = r'\>'
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'

t_ignore = r' '