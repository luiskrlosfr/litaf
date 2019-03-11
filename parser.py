# Parser for defining all grammar rules

import ply.yacc as yacc
from lexer import tokens

# Define the grammar rules. The first function is the initial state
def p_start(p):
  '''
  start : LITAF START DOUBLEDOT programa END
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5]