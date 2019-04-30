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
actual_value = ''
quadruples = []
operators = []
types = []
variables = []
jumps = []
ranges = []
conditions = []
patrons = []
funcType = ''

#---------------------------Variables MEMORIAS-------------------------------
loc_int = 100000
loc_flo = 102000
loc_str = 104000
loc_cha = 106000
loc_boo = 108000
loc_tem_int = 110000
loc_tem_flo = 112000
loc_tem_str = 114000
loc_tem_cha = 116000
loc_tem_boo = 118000
glo_int = 200000
glo_flo = 202000
glo_str = 204000
glo_cha = 206000
glo_boo = 208000
glo_tem_int = 210000
glo_tem_flo = 212000
glo_tem_str = 214000
glo_tem_cha = 216000
glo_tem_boo = 218000
con_int = 300000
con_flo = 302000
con_str = 304000
con_cha = 306000

#-------------------------------------------------------------------------------------------------------------------------------------------
#                                                        Syntax Rules with Nerve Points
#-------------------------------------------------------------------------------------------------------------------------------------------
# Declaration

def p_punt_start_litaf(p):
  '''
  punt_start_litaf : empty
  '''
  global quadCont
  global quadruples
  create_scope('constants', 'void')
  quadruples.append(Quad('GoTo',None,None,None))
  quadCont += 1
  p[0] = p[1]

def p_punt_Go_main(p):
  '''
  punt_Go_main : empty
  '''
  reset_locals()
  global quadCont
  global quadruples
  quadruples[0].result = quadCont
  p[0] = p[1]

def p_declaration_A(p):
  '''
  declaration_A : ID declaration_A1
  '''
  global actualType
  insert_var(p[1], actualType)
  p[0] = p[1] + p[2]

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

# Function
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
  global actualScope
  global scopeTable
  global actualType
  actualType = p[1]
  scopeTable.scopes[actualScope][0] = p[1]
  p[0] = p[1]

def p_function_type(p):
  '''
  function_type : type
                | VOID  
  '''
  global funcType
  funcType = p[1]
  p[0] = p[1]

def p_function_D(p): # Return value for function
  '''
  function_D : WITH hyper_exp
             | empty
  '''
  global actualScope
  global scopeTable
  global quadruples
  global quadCont
  global funcType
  if funcType != 'void':
    quadruples.append(Quad('return',None,None,str(variables.pop())))
  else:
    quadruples.append(Quad('return',None,None,None))
  quadCont += 1
  quadruples.append(Quad('EndProc',None,None,None))
  quadCont += 1
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]

# Function Call
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

# Mega Exp
def p_mega_exp_A1(p):
  '''
  mega_exp_A1 : AND
              | OR
  '''
  global operators
  operators.append(p[1])
  p[0] = p[1]

# Super Exp
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
def p_exp_A1(p):
  '''
  exp_A1 : PLUS 
         | MINUS 
  '''
  global operators
  operators.append(p[1])
  p[0] = p[1]

# Term
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
  global scopeTable
  global actualScope
  global actual_value
  if p[1] != '(' and check_if_exist(p[1]):
    variables.append(actual_value)
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += str(p[x])
  p[0]

# Loop Cycle
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

# Lecture
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

# Writing
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

#-------------------------------------------------------------------------------------------------------------------------------------------
#                      General Real Value Grammars with Nerve Points (These are used or called by many different grammar rules)
#-------------------------------------------------------------------------------------------------------------------------------------------

# Bool Values
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

# Constants
def p_int_const(p):
  '''
  int_const : INT_CONST
  '''
  global scopeTable
  global glo_int
  global actual_value
  if not check_if_exist(p[1]):
    dir = glo_int
    glo_int += 1
  else:
    dir = actual_value
  scopeTable.scopes['constants'][1].push(p[1], 'int', dir)
  p[0] = p[1]
def p_char_const(p):
  '''
  char_const : CHAR_CONST
  '''
  global scopeTable
  global glo_cha
  global actual_value
  if not check_if_exist(p[1]):
    dir = glo_cha
    glo_cha += 1
  else:
    dir = actual_value
  scopeTable.scopes['constants'][1].push(p[1], 'cha', dir)
  p[0] = p[1]

def p_float_const(p):
  '''
  float_const : FLOAT_CONST
  '''
  global scopeTable
  global glo_flo
  global actual_value
  if not check_if_exist(p[1]):
    dir = glo_flo
    glo_flo += 1
  else:
    dir = actual_value
  scopeTable.scopes['constants'][1].push(p[1], 'flo', dir)
  p[0] = p[1]

def p_string_const(p):
  '''
  string_const : STRING_CONST
  '''
  global scopeTable
  global glo_str
  global actual_value
  if not check_if_exist(p[1]):
    dir = glo_str
    glo_str += 1
  else:
    dir = actual_value
  scopeTable.scopes['constants'][1].push(p[1], 'str', dir)
  p[0] = p[1]

#-------------------------------------------------------------------------------------------------------------------------------------------
#                                                             Nerve Points
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
  reset_locals()
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
    dir = calc_dir(typ)
    scopeTable.scopes[actualScope][1].push(var, typ, dir)
# Function for setting actual scope
def create_scope(scope, typ):
  global scopeTable
  global actualScope
  actualScope = scope
  if actualScope in scopeTable.scopes:
    print("Error: Función '{}' ya existe".format(actualScope))
  else:
    scopeTable.push(scope, typ, VarTable())
# Function for resetting local directions
def reset_locals():
  global loc_int
  global loc_flo
  global loc_str
  global loc_cha
  global loc_tem_int
  global loc_tem_flo
  global loc_tem_str
  global loc_tem_cha 
  loc_int = 100000
  loc_flo = 102000
  loc_str = 104000
  loc_cha = 106000
  loc_tem_int = 110000
  loc_tem_flo = 112000
  loc_tem_str = 114000
  loc_tem_cha = 116000 

def calc_dir(typ):
  global actualScope
  dir = 0
  if actualScope == 'global':
    if typ == 'int':
      global glo_int
      dir = glo_int
      glo_int += 1
    elif typ == 'flo':
      global glo_flo
      dir = glo_flo
      glo_flo += 1
    elif typ == 'str':
      global glo_str
      dir = glo_str
      glo_str += 1
    elif typ == 'cha':
      global glo_cha
      dir = glo_cha
      glo_cha += 1
    elif typ == 'boo':
      global glo_boo
      dir = glo_boo
      glo_boo += 1
  if actualScope == 'constants':
    if typ == 'int':
      global con_int
      dir = con_int
      con_int += 1
    elif typ == 'flo':
      global con_flo
      dir = con_flo
      con_flo += 1
    elif typ == 'str':
      global con_str
      dir = con_str
      con_str += 1
    elif typ == 'cha':
      global con_cha
      dir = con_cha
      con_cha += 1
    elif typ == 'boo':
      global con_boo
      dir = con_boo
      con_boo += 1
  else:
    if typ == 'int':
      global loc_int
      dir = loc_int
      loc_int += 1
    elif typ == 'flo':
      global loc_flo
      dir = loc_flo
      loc_flo += 1
    elif typ == 'str':
      global loc_str
      dir = loc_str
      loc_str += 1
    elif typ == 'cha':
      global loc_cha
      dir = loc_cha
      loc_cha += 1
    elif typ == 'boo':
      global loc_boo
      dir = loc_boo
      loc_boo += 1
  return dir

def check_if_exist(var):
  global scopeTable
  global actualScope
  global actual_value
  if var in scopeTable.scopes[actualScope][1].vars:
    actual_value = scopeTable.scopes[actualScope][1].vars[var][1]
    return True
  elif var in scopeTable.scopes['global'][1].vars:
    actual_value = scopeTable.scopes['global'][1].vars[var][1]
    return True
  elif var in scopeTable.scopes['constants'][1].vars:
    actual_value = scopeTable.scopes['constants'][1].vars[var][1]
    return True
  else:
    return False
print(scopeTable.scopes)
