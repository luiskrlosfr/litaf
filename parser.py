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
            | class_
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
  declaration : type_val declaration_A
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
def function_A(p): # Parameters for declaring functions
  '''
  function_A : type_val ID function_A1
  '''
def function_A1(p):
  '''
  function_A1 : COMMA function_A
              | empty
  '''
def function_B(p): # Type of return value (includes void)
  '''
  function_B : type_val
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
  function_call_A : hyper_exp function_call_A1
                  | empty
  '''
def function_call_A1(p):
  '''
  function_call_A1 : COMMA hyper_exp function_call_A1
                   | empty
  '''
# Statement
def statement(p):
  '''
  statement : declaration
            | block
            | declaration_class
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
        | class_actions
        | list_actions
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
           | class_values
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
# Term
def term(p):
  '''
  term : factor term_A
  '''
def term_A(p):
  '''
  term_A : term_A1 term
         | empty
  '''
def term_A1(p):
  '''
  term_A1 : MULTIPLY
          | DIVIDE
  '''
# Factor
def factor(p):
  '''
  factor : value
         | OPEN_PARENTHESIS hyper_exp CLOSE_PARENTHESIS
  '''
# Cycle call
def cycle(p):
  '''
  cycle : cycle_A END
  '''
def cycle_A(p):
  '''
  cycle_A : loop
          | until
  '''
def loop(p): # Loop Cycle structure
  '''
  loop : LOOP FROM ID TO loop_value BY patron built_block
  '''
def loop_value(p):
  '''
  loop_value : ID
             | INT_CONST
             | list_val
             | class_values
  '''
def patron(p):
  '''
  patron : patron_A loop_value
  '''
def patron_A(p):
  '''
  patron_A : PLUS
           | MINUS
           | MULTIPLY
           | DIVIDE
  '''
def until(p):
  '''
  until : UNTIL hyper_exp IS bool_values DO built_block
  '''
# Condition
def condition(p):
  '''
  condition : IF condition_exp built_block condition_A condition_B END
  '''
def condition_exp(p):
  '''
  condition_exp : OPEN_PARENTHESIS hyper_exp CLOSE_PARENTHESIS
  '''
def condition_A(p):
  '''
  condition_A : ELSIF condition_exp built_block condition_A
              | empty
  '''
def condition_B(p):
  '''
  condition_B : ELSE built_block
  '''
# Lecture
def lecture(p):
  '''
  lecture : IN OPEN_PARENTHESIS lecture_A CLOSE_PARENTHESIS
  '''
def lecture_A(p):
  '''
  lecture_A : ID lecture_A1
  '''
def lecture_A1(p):
  '''
  lecture_A1 : COMMA lecture_A
             | empty
  '''
# Writing
def writing(p):
  '''
  writing : OUT OPEN_PARENTHESIS writing_A CLOSE_PARENTHESIS
  '''
def writing_A(p):
  '''
  writing_A : hyper_exp writing_A1
  '''
def writing_A1(p):
  '''
  writing_A1 : COMMA writing_A
             | empty
  '''
############################### Class Related Grammar
# Class
def class_(p):
  '''
  class_ : CLASS_ID heritance IS class_attributes class_methods END
  '''
def heritance(p):
  '''
  heritance : FROM CLASS_ID
            | empty
  '''
# Attributes
def class_attributes(p):
  '''
  class_attributes : ATTRIBUTES DOUBLE_DOT attributes END
  '''
def attributes(p):
  '''
  attributes : attributes_A attributes
             | empty
  '''
def attributes_A(p):
  '''
  attributes_A : visibility type_val ID
  '''
# Methods
def class_methods(p):
  '''
  class_methods : METHODS DOUBLE_DOT methods END
  '''
def methods(p):
  '''
  methods : constructor methods_A
  '''
def methods_A(p):
  '''
  methods_A : visibility function methods_A
            | empty
  '''
# Constructor
def constructor(p):
  '''
  constructor : visibility CLASS_ID OPEN_PARENTHESIS function_A CLOSE_PARENTHESIS IS CLASS_ID constructor_A END
  '''
def constructor_A(p):
  '''
  constructor_A : statement constructor_A
                | empty
  '''
def visibility(p):
  '''
  visibility : PUBLIC
             | PRIVATE
  '''
# Class Declaration
def declaration_class(p):
  '''
  declaration_class : CLASS_ID ID declaration_class_A
  '''
def declaration_class_A(p):
  '''
  declaration_class_A : COMMA ID declaration_class_A
                      | empty
  '''
# Assign class to variable
def assign_class(p):
  '''
  assign_class : ID EQUAL assign_class_A
  '''
def assign_class_A(p):
  '''
  assign_class_A : ID
                 | CLASS_ID DOT NEW OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
# Class Values
def class_values(p):
  '''
  class_values : call_method
               | call_attribute
  '''
# Class Actions
def class_actions(p):
  '''
  class_actions : declaration_class
                | assign_class
  '''
# Call Attribute
def call_attribute(p):
  '''
  call_attribute : ID DOT ID
  '''
# Call Method
def call_method(p):
  '''
  call_method : ID DOT FUNCTION_ID OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
############################### General Real Value Grammars
# Block for Condition and Cycles
def built_block(p):
  '''
  built_block : block built_block
              | empty
  '''
# Type Val
def type_val(p):
  '''
  type_val : INT
           | FLO
           | BOO
           | CHA
           | STR
  '''
# Value
def value(p):
  '''
  value : ID
        | constants
        | list_values
        | class_values
        | function_call
  '''
# Constants
def constants(p):
  '''
  constants : INT_CONST
            | CHAR_CONST
            | FLOAT_CONST
            | STRING_CONST
            | bool_values
  '''
# Bool Values
def bool_values(p):
  '''
  bool_values : TRUE
              | FALSE
  '''
# Empty
def p_empty(p):
  '''
  empty : 
  '''
  p[0] = ""

# Simple Error
def p_error(p):
  print("Error en la gramática")

# Build the parser
parser = yacc.yacc()