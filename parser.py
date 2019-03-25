# Parser for defining all grammar rules
import ply.yacc as yacc
from lexer import tokens

# Start
def p_start(p):
  '''
  start : LITAF START DOUBLE_DOT classes global_vars functions main END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Classes
def p_classes(p):
  '''
  classes : class classes
          | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Global Vars
def p_global_vars(p):
  '''
  global_vars : declarations global_vars
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Declarations
def p_declarations(p):
  '''
  declarations : declaration
               | declaration_class
               | declaration_list
  '''
  p[0] = p[1]
# Main
def p_main(p):
  '''
  main : MAIN IS INT main_A WITH INT_CONST END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_main_A(p):
  '''
  main_A : statement main_A
         | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Functions
def p_functions(p):
  '''
  functions : function functions
            | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Declaration
def p_declaration(p):
  '''
  declaration : type declaration_A
  '''
  p[0] = p[1] + p[2]
def p_declaration_A(p):
  '''
  declaration_A : ID declaration_A1
  '''
  p[0] = p[1] + p[2]
def p_declaration_A1(p):
  '''
  declaration_A1 : COMMA declaration_A
                | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Assign
def p_assign(p):
  '''
  assign : ID EQUAL assign_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_assign_A(p):
  '''
  assign_A : hyper_exp
           | CLASS_ID DOT NEW OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
           | list
  '''
  p[0] = p[1]
# Function
def p_function(p):
  '''
  function : FUN FUNCTION_ID OPEN_PARENTHESIS function_A CLOSE_PARENTHESIS IS function_B function_C function_D END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_A(p): # Parameters for declaring functions
  '''
  function_A : type ID function_A1
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_A1(p):
  '''
  function_A1 : COMMA type ID function_A1
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_B(p): # Type of return value (includes void)
  '''
  function_B : type
             | VOID
  '''
  p[0] = p[1]
def p_function_C(p): # Statements inside function
  '''
  function_C : statement function_C
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_D(p): # Return value for function
  '''
  function_D : WITH hyper_exp
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Function Call
def p_function_call(p):
  '''
  function_call : FUNCTION_ID OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_call_A(p): # Parameters for function call
  '''
  function_call_A : hyper_exp function_call_A1
                  | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_call_A1(p):
  '''
  function_call_A1 : COMMA hyper_exp function_call_A1
                   | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Statement
def p_statement(p):
  '''
  statement : declaration
            | block
            | declaration_class
            | declaration_list
  '''
  p[0] = p[1]
# Block
def p_block(p):
  '''
  block : assign
        | hyper_exp
        | cycle
        | condition
        | lecture
        | writing
        | list_methods
        | COMMENT
  '''
  p[0] = p[1]
# Hyper Exp
def p_hyper_exp(p):
  '''
  hyper_exp : mega_exp hyper_exp_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_hyper_exp_A(p):
  '''
  hyper_exp_A : NOT hyper_exp
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Mega Exp
def p_mega_exp(p):
  '''
  mega_exp : super_exp mega_exp_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_mega_exp_A(p):
  '''
  mega_exp_A : mega_exp_A1 mega_exp
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_mega_exp_A1(p):
  '''
  mega_exp_A1 : AND
              | OR
  '''
  p[0] = p[1]
# Super Exp
def p_super_exp(p):
  '''
  super_exp : exp super_exp_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_super_exp_A(p):
  '''
  super_exp_A : super_exp_A1 super_exp
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_super_exp_A1(p):
  '''
  super_exp_A1 : LESS_THAN
               | MORE_THAN
               | EQUAL_EQUAL
               | LESS_EQUAL
               | MORE_EQUAL
               | DIFFERENT_FROM
  '''
  p[0] = p[1]
# Exp
def p_exp(p):
  '''
  exp : term exp_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_exp_A(p):
  '''
  exp_A : exp_A1 exp
        | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_exp_A1(p):
  '''
  exp_A1 : PLUS
         | MINUS
  '''
  p[0] = p[1]
# Term
def p_term(p):
  '''
  term : factor term_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_term_A(p):
  '''
  term_A : term_A1 term
         | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_term_A1(p):
  '''
  term_A1 : MULTIPLY
          | DIVIDE
  '''
  p[0] = p[1]
# Factor
def p_factor(p):
  '''
  factor : value
         | OPEN_PARENTHESIS hyper_exp CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Cycle call
def p_cycle(p):
  '''
  cycle : cycle_A END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_cycle_A(p):
  '''
  cycle_A : loop
          | until
  '''
  p[0] = p[1]
def p_loop(p): # Loop Cycle structure
  '''
  loop : LOOP FROM ID TO loop_value BY patron built_block
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_loop_value(p):
  '''
  loop_value : hyper_exp
  '''
  p[0] = p[1]
def p_patron(p):
  '''
  patron : patron_A loop_value
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_patron_A(p):
  '''
  patron_A : PLUS
           | MINUS
           | MULTIPLY
           | DIVIDE
  '''
  p[0] = p[1]
def p_until(p):
  '''
  until : UNTIL hyper_exp IS bool_values DO built_block
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Condition
def p_condition(p):
  '''
  condition : IF condition_exp built_block condition_A condition_B END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_condition_exp(p):
  '''
  condition_exp : OPEN_PARENTHESIS hyper_exp CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_condition_A(p):
  '''
  condition_A : ELSIF condition_exp built_block condition_A
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_condition_B(p):
  '''
  condition_B : ELSE built_block
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Lecture
def p_lecture(p):
  '''
  lecture : IN OPEN_PARENTHESIS lecture_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_lecture_A(p):
  '''
  lecture_A : ID lecture_A1
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_lecture_A1(p):
  '''
  lecture_A1 : COMMA lecture_A
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Writing
def p_writing(p):
  '''
  writing : OUT OPEN_PARENTHESIS writing_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_writing_A(p):
  '''
  writing_A : hyper_exp writing_A1
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_writing_A1(p):
  '''
  writing_A1 : COMMA writing_A
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
############################### Class Related Grammar
# Class
def p_class(p):
  '''
  class : CLASS CLASS_ID heritance IS class_attributes class_methods END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_heritance(p):
  '''
  heritance : FROM CLASS_ID
            | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Attributes
def p_class_attributes(p):
  '''
  class_attributes : ATTRIBUTES DOUBLE_DOT attributes END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_attributes(p):
  '''
  attributes : attributes_A attributes
             | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_attributes_A(p):
  '''
  attributes_A : visibility type ID
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Methods
def p_class_methods(p):
  '''
  class_methods : METHODS DOUBLE_DOT methods END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_methods(p):
  '''
  methods : constructor methods_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_methods_A(p):
  '''
  methods_A : visibility function methods_A
            | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Constructor
def p_constructor(p):
  '''
  constructor : visibility CLASS_ID OPEN_PARENTHESIS function_A CLOSE_PARENTHESIS IS CLASS_ID constructor_A END
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_constructor_A(p):
  '''
  constructor_A : statement constructor_A
                | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_visibility(p):
  '''
  visibility : PUBLIC
             | PRIVATE
  '''
  p[0] = p[1]
# Class Declaration
def p_declaration_class(p):
  '''
  declaration_class : CLASS_ID ID declaration_class_A
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_declaration_class_A(p):
  '''
  declaration_class_A : COMMA ID declaration_class_A
                      | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Class Values
def p_class_values(p):
  '''
  class_values : call_method
               | call_attribute
  '''
  p[0] = p[1]
# Call Attribute
def p_call_attribute(p):
  '''
  call_attribute : ID DOT ID
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Call Method
def p_call_method(p):
  '''
  call_method : ID DOT FUNCTION_ID OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
############################### Lists (Vectors) Related Grammars
# List
def p_list(p):
  '''
  list : OPEN_BRACKET function_call_A CLOSE_BRACKET
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Declaration
def p_declaration_list(p):
  '''
  declaration_list : LIS ID declaration_list_A1
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_declaration_list_A1(p):
  '''
  declaration_list_A1 : COMMA ID declaration_list_A1
                      | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Values
def p_list_values(p):
  '''
  list_values : list_val
              | list_pop
  '''
  p[0] = p[1]
# List Value (Single)
def p_list_val(p):
  '''
  list_val : ID OPEN_BRACKET INT_CONST CLOSE_BRACKET
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Methods
def p_list_methods(p):
  '''
  list_methods : list_push
               | list_size
               | list_concat
               | list_empty
               | list_reverse
  '''
  p[0] = p[1]
# List Pop
def p_list_pop(p):
  '''
  list_pop : ID DOT POP OPEN_PARENTHESIS CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Push
def p_list_push(p):
  '''
  list_push : ID DOT PUSH OPEN_PARENTHESIS hyper_exp CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Size
def p_list_size(p):
  '''
  list_size : ID DOT SIZE OPEN_PARENTHESIS CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Concat
def p_list_concat(p):
  '''
  list_concat : ID DOT JOIN OPEN_PARENTHESIS list_concat_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_list_concat_A(p):
  '''
  list_concat_A : ID
                | list
  '''
  p[0] = p[1]
# List Empty
def p_list_empty(p):
  '''
  list_empty : ID DOT EMPTY OPEN_PARENTHESIS CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# List Reverse
def p_list_reverse(p):
  '''
  list_reverse : ID DOT FLIP OPEN_PARENTHESIS CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
############################### General Real Value Grammars (These are used or called by many different grammar rules)
# Block for Condition and Cycles
def p_built_block(p):
  '''
  built_block : block built_block
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Type Val
def p_type(p):
  '''
  type : INT
       | FLO
       | BOO
       | CHA
       | STR
  '''
  p[0] = p[1]
# Value
def p_value(p):
  '''
  value : ID
        | constants
        | list_values
        | class_values
        | function_call
  '''
  p[0] = p[1]
# Constants
def p_constants(p):
  '''
  constants : INT_CONST
            | CHAR_CONST
            | FLOAT_CONST
            | STRING_CONST
            | bool_values
  '''
  p[0] = p[1]
# Bool Values
def p_bool_values(p):
  '''
  bool_values : TRUE
              | FALSE
  '''
  p[0] = p[1]
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

# Read file as an input and evaluate if the grammar is acceptable or not. Print a message if it finds an error
# in the grammar.
print("Teclea el nombre del archivo de texto")
name = input('parser >> ')

with open(name, 'r') as myfile:
  line = myfile.read().replace('\n', '')
  result = parser.parse(line)
  print(result)