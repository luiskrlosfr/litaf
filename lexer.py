# Lexer for defining all Tokens

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
  'COMMENT',              # Comments
  'DOT',                     # Assignation and Calls
  'COMMA',
  'DOUBLE_DOT',
  'SINGLE_QUOTE',            # Strings and Chars
  'DOUBLE_QUOTE'
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
  'main'       : 'MAIN',
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

t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQUAL_EQUAL = r'\=\='
t_MORE_EQUAL = r'\>\='
t_LESS_EQUAL = r'\<\='
t_DIFFERENT_FROM = r'\!\='
t_DOUBLE_QUOTE = r'\"'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LESS_THAN = r'\<'
t_MORE_THAN = r'\>'
t_NOT = r'\!'
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_DOT = r'\.'
t_SINGLE_QUOTE = r'\''
t_COMMA = r'\,'
t_DOUBLE_DOT = r'\:'
t_EQUAL = r'\='
t_UNDERSCORE = r'\_'
t_ignore = r' '

# Define complex terminal tokens
def t_COMMENT(t):
  r"\%[^%]*\%"
  t.type = reserved.get(t.value, 'COMMENT')
  return t
def t_CLASS_ID(t):
  r"([A-Z][a-z]+)+"
  t.type = reserved.get(t.value, 'CLASS_ID')
  return t

def t_FUNCTION_ID(t):
  r"[a-z]+(\_[a-z]+)*"
  t.type = reserved.get(t.value, 'FUNCTION_ID')
  return t

def t_ID(t):
  r"[a-z][a-zA-Z]*[0-9]*"
  t.type = reserved.get(t.value, 'ID')
  return t

def t_CHAR_CONST(t):
  r"\'[a-zA-Z]\'"
  t.type = reserved.get(t.value, 'CHAR_CONST')
  t.value = t.value[1:-1]
  return t

def t_STRING_CONST(t):
  r"\"[^\"]*\""
  t.type = reserved.get(t.value, 'STRING_CONST')
  t.value = t.value[1:-1]
  return t

def t_FLOAT_CONST(t):
  r"\-?[0-9]+\.[0-9]+"
  t.value = float(t.value)
  return t

def t_INT_CONST(t):
  r"\-?[0-9]+"
  t.value = int(t.value)
  return t

def t_error(t):
  print("Undefined character")
  t.lexer.skip(1)

# Combine tokens with reserved words tokens
tokens = tokens + list(reserved.values())

# Build the lexer
lexer = lex.lex()

# Some Tests
# lexer.input("12345") # -> CTE_INT token
# tok = lexer.token()
# print(tok)
# lexer.input("\"1234567.1245\"") # -> CTE_STRING token
# tok = lexer.token()
# print(tok)
# lexer.input("litaf start :  fun main() is int with 0 end end") # -> PROGRAM ID DOUBLEDOT OPENKEY CLOSEKEY tokens
# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)
# lexer.input("+ - * / = , % true false") # -> PLUS MINUS MULTIPLY DIVIDE EQUAL SEMICOLON COMMA tokens
# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)