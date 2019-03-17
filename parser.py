# Parser for defining all grammar rules
import ply.yacc as yacc
from lexer import tokens

# Start
def p_start(p):
  '''
  start : LITAF START DOUBLEDOT program END
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5]
# Program
def p_program(p):
  '''
  program : program_A MAIN
  '''
  p[0] = p[1] + p[2] + " "
def p_program_A(p):
  '''
  program_A : program_A1
            | program_A program_A1
  '''
def p_program_A1(p):
  '''
  program_A1 : declaration
            | assign_simple
            | function
            | class
            | empty
  '''
# Main
def p_main(p):
  '''
  main : FUN MAIN OPEN_PARENTHESIS CLOSE_PARENTHESIS IS INT main_A main_B END
  '''
def p_main_A(p):
  '''
  main_A : statement main_A
         | empty
  '''
def p_main_B(p):
  '''
  main_B : WITH 0
         | empty
  '''
# Declaration
def p_declaration(p):
  '''
  declaration : type declaration_A
  '''
def p_declaration_A(p):
  '''
  declaration_A : ID declaration_A1
  '''
def p_declaration_A1(p):
  '''
  declaration_A1 : COMMA declaration_A
                | empty
  '''
# Assign Simple (for global variables)
def p_assign_simple(p):
  '''
  assign_simple : ID EQUAL assign_simple_A
  '''
def p_assign_simple_A(p):
  '''
  assign_simple_A : value
                  | list_values
  '''
# Function
def p_function(p):
  '''
  function : FUN FUNCTION_ID OPEN_PARENTHESIS function_A CLOSE_PARENTHESIS IS function_B function_C function_D END
  '''
def function_A(p): # Parameters for functions
  '''
  function_A : type ID function_A1
  '''
def function_A1(p):
  '''
  function_A1 : COMMA function_A
              | empty
  '''
def function_B(p): # Type of return value (includes void)
  '''
  function_B : type
             | VOID
  '''
def function_C(p): # Statements inside function
  '''
  function_C : statement
             | statement function_C
  '''
def function_D(p): # Return value for function
  '''
  function_D : WITH value
             | empty
  '''
# Function Call
def function_call(p):
  '''
  function_call : FUNCTION_ID OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
def function_call_A(p): # Parameters for function call
  '''
  function_call_A : hyper_exp 
                  | hyper_exp COMMA function_call_A
  '''
# Statement
def statement(p):
  '''
  statement : declaration
            | block
            | declaration_obj
  '''
# Block
def block(p):
  '''
  block : assign
        | hyper_exp
        | cycle
        | condition
        | function_call
        | lecture
        | writing
        | obj_action
        | list_action
  '''
# Assign
def assign(p):
  '''
  assign : ID EQUAL assign_A
  '''
def assign_A(p):
  '''
  assign_A : hyper_exp
           | function_call
           | obj_values
           | list_values
  '''
# Hyper Exp
def hyper_exp(p):
  '''
  hyper_exp : mega_exp hyper_exp_A
  '''
def hyper_exp_A(p):
  '''
  hyper_exp_A : NOT hyper_exp
              | empty
  '''
# Mega Exp
def mega_exp(p):
  '''
  mega_exp : super_exp mega_exp_A
  '''
def mega_exp_A(p):
  '''
  mega_exp_A : mega_exp_A1 mega_exp
             | empty
  '''
def mega_exp_A1(p):
  '''
  mega_exp_A1 : AND
              | OR
  '''
# Super Exp
def super_exp(p):
  '''
  super_exp : exp super_exp_A
  '''
def super_exp_A(p):
  '''
  super_exp_A : super_exp_A1 super_exp
              | empty
  '''
def super_exp_A1(p):
  '''
  super_exp_A1 : LESS_THAN
               | MORE_THAN
               | EQUAL_EQUAL
               | LESS_EQUAL
               | MORE_EQUAL
               | NOT_EQUAL
  '''
# Exp
def exp(p):
  '''
  exp : term exp_A
  '''
def exp_A(p):
  '''
  exp_A : exp_A1 exp
        | empty
  '''
def exp_A1(p):
  '''
  exp_A1 : PLUS
         | MINUS
  '''
# Empty
def p_empty(p):
  '''
  empty : 
  '''
  p[0] = ""