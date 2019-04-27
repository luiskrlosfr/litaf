# Parser for defining all grammar rules
import ply.yacc as yacc
from quad import Quad
from vartable import VarTable, ScopeTable
from lexer import tokens
from collections import deque
scopeTable = ScopeTable()
actualScope = 'global'
actualType = 'void'
funcName = ''
quadCont = 0
contParams = 0
tempCont = 0
quadruples = []
operators = []
types = []
variables = []
jumps = []
ranges = []
conditions = []
patrons = []
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
  global_vars : createGlobal declarations global_vars_A
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]

def p_global_vars_A(p):
  '''
  global_vars_A : declarations global_vars_A
                | empty
  '''
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
  main : MAIN setMain IS INT main_A WITH INT_CONST END
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
  declaration : function_B declaration_A
  '''
  p[0] = p[1] + p[2]
def p_declaration_A(p):
  '''
  declaration_A : ID declaration_A1
  '''
  global actualType
  insert_var(p[1], actualType)
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
  assign : ID EQUAL appendEqual assign_A 
  '''
  global operators
  global quadruples
  global variables
  global quadCont
  quadruples.append(Quad(operators.pop(), "", str(variables.pop()), p[1]))
  quadCont += 1

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
  function : FUN getFunId OPEN_PARENTHESIS function_A CLOSE_PARENTHESIS IS function_B function_C function_D END
  '''
  global actualScope
  scopeTable.scopes[actualScope][0] = p[7]
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_A(p): # Parameters for declaring functions
  '''
  function_A : type ID function_A1
             | empty
  '''
  global actualScope
  global scopeTable
  if len(p) > 2:
    insert_var(p[2], p[1])
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_A1(p):
  '''
  function_A1 : COMMA type ID function_A1
              | empty
  '''
  if len(p) > 2:
    global actualScope
    global scopeTable
    insert_var(p[3], p[2])
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_B(p): # Type of return value (includes void)
  '''
  function_B : type
             | VOID
  '''
  global actualType
  actualType = p[1]
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
  function_call : function_call_name OPEN_PARENTHESIS function_call_A CLOSE_PARENTHESIS
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_call_A(p): # Parameters for function call
  '''
  function_call_A : function_call_hyper_exp function_call_A1 punt_function_call_end
                  | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_function_call_A1(p):
  '''
  function_call_A1 : COMMA function_call_hyper_exp function_call_A1
                   | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]

def p_function_call_name(p):
  '''
  function_call_name : FUNCTION_ID
  '''
  global quadruples
  global funcName
  global quadCont
  funcName = p[1]
  quadruples.append(Quad('era',funcName,'',''))
  quadCont += 1
  p[0] = p[1]
# Statement
def p_function_call_hyper_exp(p):
  '''
  function_call_hyper_exp : hyper_exp
  '''
  global quadCont
  global contParams
  global quadruples
  global variables
  contParams += 1
  quadruples.append(Quad('param',variables.pop(),'','param'+str(contParams)))
  quadCont += 1
  p[0] = p[1]
def p_statement(p):
  '''
  statement : declarations
            | block
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
  mega_exp : super_exp puntAndOr mega_exp_A
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
  global operators
  operators.append(p[1])
  p[0] = p[1]
# Super Exp
def p_super_exp(p):
  '''
  super_exp : exp puntLogical super_exp_A
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
  global operators
  operators.append(p[1])
  p[0] = p[1]
# Exp
def p_exp(p):
  '''
  exp : term puntSum exp_A
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
  global operators
  operators.append(p[1])
  p[0] = p[1]
# Term
def p_term(p):
  '''
  term : factor puntMul term_A
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
  global operators
  operators.append(p[1])
  p[0] = p[1]
# Factor
def p_factor(p):
  '''
  factor : value
         | OPEN_PARENTHESIS puntOP hyper_exp CLOSE_PARENTHESIS puntCP
  '''
  global variables
  if p[1] != '(':
    variables.append(p[1])
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
  loop : LOOP FROM puntLoopID loop_to loop_value built_block BY patron
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_loop_to(p):
  '''
  loop_to : UPTO puntLoopUp
          | DOWNTO puntLoopDown
  '''
  p[0] = p[1] + p[2]
def p_loop_value(p):
  '''
  loop_value : hyper_exp
  '''
  global variables
  global conditions
  global quadruples
  global quadCont
  global jumps
  global ranges
  global tempCont
  up = variables.pop()
  low = ranges[-1]
  quadruples.append(Quad(conditions.pop(), up, low, "t"+str(tempCont)))
  variables.append("t"+str(tempCont))
  jumps.append(quadCont)
  tempCont += 1
  quadCont += 1
  jumps.append(quadCont)
  quadruples.append(Quad('GoToF', variables.pop(), None, None))
  quadCont += 1
  p[0] = p[1]

def p_patron(p):
  '''
  patron : patron_A hyper_exp
  '''
  global quadruples
  global variables
  global quadCont
  global ranges
  global patrons
  global tempCont
  quadruples.append(Quad(patrons.pop(), variables.pop(), ranges[-1],  "t"+str(tempCont)))
  variables.append("t"+str(tempCont))
  tempCont += 1
  quadCont += 1
  quadruples.append(Quad('=', None, variables.pop(), ranges.pop()))
  quadCont += 1
  returning = jumps.pop()
  goto = jumps.pop()
  quadruples.append(Quad('GoTo', None, None, goto))
  quadCont += 1
  quadruples[returning].result = quadCont
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
  global patrons
  patrons.append(p[1])
  p[0] = p[1]
def p_until(p):
  '''
  until : UNTIL puntUntilJump hyper_exp IS bool_values_cycle puntUntil DO built_block puntUntilEnd
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
# Condition
def p_condition(p):
  '''
  condition : IF condition_exp puntIF built_block condition_A condition_B END puntIfEnd
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
  condition_A : puntElseIfGOTO ELSIF condition_exp puntElseIfGoToF built_block puntElseIfEnd condition_A
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]
def p_condition_B(p):
  '''
  condition_B : puntElse ELSE built_block
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
  global quadruples
  global quadCont
  quadruples.append(Quad('lecture', "", "", str(p[1])))
  quadCont += 1
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
  global quadruples
  global variables
  global quadCont
  quadruples.append(Quad('Writing', "", "", str(variables.pop())))
  quadCont += 1

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
  class : CLASS getClassId heritance IS class_attributes class_methods END
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
  insert_var(p[3], p[2])
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
#-------------------------------------------------------------------------------------------------------------------------------------------
#                           General Real Value Grammars (These are used or called by many different grammar rules)
#-------------------------------------------------------------------------------------------------------------------------------------------
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
def p_bool_values_cycle(p):
  '''
  bool_values_cycle : TRUE
                    | FALSE
  '''
  global quadruples
  global quadCont
  global variables
  global tempCont
  quadruples.append(Quad('==', str(variables.pop()), p[1], "t"+str(tempCont)))
  variables.append("t"+str(tempCont))
  tempCont += 1
  quadCont += 1
  p[0] = p[1]
# Empty
def p_empty(p):
  '''
  empty : 
  '''
  p[0] = ""
# Simple Error
def p_error(p):
  print("Grammar error, line {}".format(p.lexer.lineno))
#-------------------------------------------------------------------------------------------------------------------------------------------
#                                                             Puntos Neuralgicos
#-------------------------------------------------------------------------------------------------------------------------------------------
# Create Global Scope
def p_createGlobal(p):
  '''
  createGlobal : empty
  '''
  create_scope("global", "void")
  p[0] = p[1]

# Get Scope of Function
def p_getFunId(p):
  '''
  getFunId : FUNCTION_ID
  '''
  create_scope(p[1], None)
  p[0] = p[1]

def p_getClassId(p):
  '''
  getClassId : CLASS_ID
  '''
  create_scope(p[1], "class")
  p[0] = p[1]
# Set Main scope
def p_setMain(p):
  '''
  setMain : empty
  '''
  create_scope("main", "int")
  p[0] = p[1]

def p_puntSum(p):
  '''
  puntSum : empty
  '''
  global operators
  global quadruples
  global quadCont
  global variables
  global tempCont
  if len(operators) > 0:
    if operators[-1] == '+' or operators[-1] == '-':   
      quadruples.append(Quad(operators.pop(), str(variables.pop()), str(variables.pop()), "t"+str(tempCont)))
      variables.append("t"+str(tempCont))
      tempCont += 1
      quadCont += 1
  p[0] = p[1]
  
def p_puntMul(p):
  '''
  puntMul : empty
  '''
  global operators
  global quadruples
  global quadCont
  global variables
  global tempCont
  if len(operators) > 0:
    if operators[-1] == '*' or operators[-1] == '/':   
      quadruples.append(Quad(operators.pop(), str(variables.pop()), str(variables.pop()), "t"+str(tempCont)))
      variables.append("t"+str(tempCont))
      tempCont += 1
      quadCont += 1
  p[0] = p[1]

def p_appendEqual(p):
  '''
  appendEqual : empty
  '''
  global operators
  operators.append('=')
  p[0] = p[1]

def p_puntLogical(p):
  '''
  puntLogical : empty
  '''
  global operators
  global quadruples
  global quadCont
  global variables
  global tempCont
  if len(operators) > 0:
    if operators[-1] == '>' or operators[-1] == '<' or operators[-1] == '>=' or operators[-1] == '<=' or operators[-1] == '==' or operators[-1] == '!=':   
      quadruples.append(Quad(operators.pop(), str(variables.pop()), str(variables.pop()), "t"+str(tempCont)))
      variables.append("t"+str(tempCont))
      tempCont += 1
      quadCont += 1
def p_puntAndOr(p):
  '''
  puntAndOr : empty
  '''
  global operators
  global quadruples
  global quadCont
  global variables
  global tempCont
  if len(operators) > 0:
    if operators[-1] == '||' or operators[-1] == '&&':   
      quadruples.append(Quad(operators.pop(), str(variables.pop()), str(variables.pop()), "t"+str(tempCont)))
      variables.append("t"+str(tempCont))
      tempCont += 1
      quadCont += 1
def p_puntOP(p):
  '''
  puntOP : empty
  '''
  global operators
  operators.append('(')
  p[0] = p[1]

def p_puntCP(p):
  '''
  puntCP : empty
  '''
  global operators
  operators.pop()
  p[0] = p[1]

def p_puntIF(p):
  '''
  puntIF : empty
  '''
  global quadruples
  global variables
  global quadCont
  global jumps
  quadruples.append(Quad('GoToF',str(variables.pop()),'',''))
  jumps.append(quadCont)
  quadCont += 1
  p[0] = p[1]

def p_puntElse(p):
  '''
  puntElse : empty
  '''
  global quadruples
  global variables
  global quadCont
  global jumps
  quadruples.append(Quad('GoTo','','',''))
  false = jumps.pop()
  jumps.append(quadCont)
  quadCont += 1
  quadruples[false].result = str(quadCont)
  p[0] = p[1]

def p_puntIfEnd(p):
  '''
  puntIfEnd : empty
  '''
  global quadruples
  global quadCont
  global jumps
  end = jumps.pop()
  quadruples[end].result = str(quadCont)
  p[0] = p[1]

def p_puntElseIfGOTO(p):
  '''
  puntElseIfGOTO : empty
  '''
  global quadruples
  global variables
  global quadCont
  global jumps
  returning = jumps.pop()
  jumps.append(quadCont)
  quadruples.append(Quad('GoTo', '', '', '',))
  quadCont += 1
  quadruples[returning].result = str(quadCont-1)
  p[0] = p[1]

def p_puntElseIfGoToF(p):
  '''
  puntElseIfGoToF : empty
  '''
  global quadruples
  global variables
  global quadCont
  global jumps
  jumps.append(quadCont)
  quadruples.append(Quad('GoToF','',str(variables.pop()),''))
  quadCont += 1
  
  p[0] = p[1]

def p_puntElseIfEnd(p):
  '''
  puntElseIfEnd : empty
  '''
  global jumps
  global quadruples
  returning = jumps.pop()
  quadruples[returning].result = str(quadCont)
  p[0] = p[1]

def p_puntUntilJump(p):
  '''
  puntUntilJump : empty
  '''
  global quadCont
  global jumps
  jumps.append(quadCont)
  p[0] = p[1]

def p_puntUntil(p):
  '''
  puntUntil : empty
  '''
  global quadruples
  global quadCont
  global jumps
  result = variables.pop()
  quadruples.append(Quad('GoToF',str(result),'',''))
  jumps.append(quadCont)
  quadCont += 1
  p[0] = p[1]

def p_puntUntilEnd(p):
  '''
  puntUntilEnd : empty
  '''
  global quadruples
  global quadCont
  global jumps
  end = jumps.pop()                           # Pops GOTOF QUAD and fills the missing jump with actual counter quadruple
  quadCont += 1
  quadruples[end].result = str(quadCont)
  returning = jumps.pop()                     # Pops QUAD for generating GOTO QUAD to re evaluation of the conditional exp of the cycle
  quadruples.append(Quad('GOTO','','',str(returning)))
  p[0] = p[1]
def p_puntLoopID(p):
  '''
  puntLoopID :  ID
  '''
  global variables
  global ranges
  global operators
  variables.append(p[1])
  ranges.append(p[1])
  p[0] = p[1]

def p_puntLoopUp(p):
  '''
  puntLoopUp : empty
  '''
  global conditions
  conditions.append('<=')
  p[0] = p[1]
def p_punt_function_call_end(p):
  '''
  punt_function_call_end : empty
  '''
  global quadruples
  global quadCont
  global funcName
  quadruples.append(Quad('gosub',funcName,None,None))
  quadCont += 1
  p[0] = p[1]
def p_puntLoopDown(p):
  '''
  puntLoopDown : empty
  '''
  global conditions
  conditions.append('>=')
  p[0] = p[1]
#-------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 Functions
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function for inserting variable in scope table
def insert_var(var, typ):
  global actualScope
  global scopeTable
  if var in scopeTable.scopes[actualScope][1].vars:
    print("Error: Variable '{}' ya definida").format(var)
  else:
    scopeTable.scopes[actualScope][1].push(var, typ)
# Function for setting actual scope
def create_scope(scope, typ):
  global scopeTable
  global actualScope
  actualScope = scope
  if actualScope in scopeTable.scopes:
    print("Error: Función '{}' ya existe".format(actualScope))
  else:
    scopeTable.push(scope, typ, VarTable())

# Build the parser
parser = yacc.yacc()

# Read file as an input and evaluate if the grammar is acceptable or not. Print a message if it finds an error
# in the grammar.
print("Teclea el nombre del archivo de texto")
name = input('parser >> ')

with open(name, 'r') as myfile:
  line = myfile.read().replace('\n', '')
  result = parser.parse(line)
  # print(result)
# print(scopeTable.scopes)
# for scope in scopeTable.scopes.values():
#   print(scope[1].vars)
cont = 0
for quad in quadruples:
  print(str(cont) + " ", end = '')
  quad.print()
  cont += 1