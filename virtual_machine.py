from parser import quadruples, memory
from virtual_memory import Memory
import operator

memoryStack = []
actualMemory = Memory(100000, 110000)
Memory(300000, 310000)
globalMemory = Memory(200000, 210000)
constantMemory = Memory(300000, None)

arithmetic_operations = { '+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv }

def execute_quadruple(quad, ip):
  global memoryStack
  global actualMemory
  instruction = quad.operator
  pointer = ip
  if instruction == 'GoTo':
    create_local_memory()
    return quad.result
  elif instruction == 'ERA':
    memoryStack.append(actualMemory)
    create_local_memory()
  elif instruction == 'GoSub':
    actualMemory = memoryStack.pop()
  elif instruction == '+' or instruction == '-' or instruction == '*' or instruction == '/':
    execute_aritmetic_operation(instruction, get_quad_value(quad.op1), get_quad_value(quad.op2), quad.result)
  elif instruction == 'Writing':
    output_msg(quad.result)
  pointer += 1
  return pointer

# Executes aritmetic operation according to operator
def execute_aritmetic_operation(op, left, right, res_direction):
  result =  arithmetic_operations[op](left, right)
  insert_into_corresponding_direction(res_direction, result)

# Creates local Memory for function
def create_local_memory():
  global actualMemory
  actualMemory = Memory(100000, 110000)

# Print function for Writing quad instruction
def output_msg(message):
  print(get_quad_value(message))

# Inserts value into corresponding memory direction
def insert_into_corresponding_direction(direction, value):
  global actualMemory
  global constantMemory
  global globalMemory
  if 100000 <= direction and direction <= 101999:   # LOCALS
    actualMemory.variables.int.push(value)
  elif 102000 <= direction and direction <= 103999:
    actualMemory.variables.flo.push(value)
  elif 104000 <= direction and direction <= 105999:
    actualMemory.variables.str.push(value)
  elif 106000 <= direction and direction <= 107999:
    actualMemory.variables.cha.push(value)
  elif 108000 <= direction and direction <= 109999:
    actualMemory.variables.boo.push(value)
  elif 110000 <= direction and direction <= 111999:
    actualMemory.temporals.int.push(value)
  elif 112000 <= direction and direction <= 113999:
    actualMemory.temporals.flo.push(value)
  elif 114000 <= direction and direction <= 115999:
    actualMemory.temporals.str.push(value)
  elif 116000 <= direction and direction <= 117999:
    actualMemory.temporals.cha.push(value)
  elif 118000 <= direction and direction <= 119999:
    actualMemory.temporals.boo.push(value)
  elif 200000 <= direction and direction <= 201999: # GLOBAL
    globalMemory.variables.int.push(value)
  elif 202000 <= direction and direction <= 203999:
    globalMemory.variables.flo.push(value)
  elif 204000 <= direction and direction <= 205999:
    globalMemory.variables.str.push(value)
  elif 206000 <= direction and direction <= 207999:
    globalMemory.variables.cha.push(value)
  elif 208000 <= direction and direction <= 209999:
    globalMemory.variables.boo.push(value)
  elif 210000 <= direction and direction <= 211999:
    globalMemory.temporals.int.push(value)
  elif 212000 <= direction and direction <= 213999:
    globalMemory.temporals.flo.push(value)
  elif 214000 <= direction and direction <= 215999:
    globalMemory.temporals.str.push(value)
  elif 216000 <= direction and direction <= 217999:
    globalMemory.temporals.cha.push(value)
  elif 218000 <= direction and direction <= 219999:
    globalMemory.temporals.boo.push(value)
  elif 300000 <= direction and direction <= 301999: # CONSTANTS
    constantMemory.variables.int.push(value)
  elif 302000 <= direction and direction <= 303999:
    constantMemory.variables.flo.push(value)
  elif 304000 <= direction and direction <= 305999:
    constantMemory.variables.str.push(value)
  elif 306000 <= direction and direction <= 307999:
    constantMemory.variables.cha.push(value)
  elif 308000 <= direction and direction <= 309999:
    constantMemory.variables.boo.push(value)
  
def get_quad_value(direction):
  global actualMemory
  global constantMemory
  global globalMemory
  if 100000 <= direction and direction <= 101999:           # LOCALS
    return actualMemory.variables.int.get_value(direction)
  elif 102000 <= direction and direction <= 103999:
    return actualMemory.variables.flo.get_value(direction)
  elif 104000 <= direction and direction <= 105999:
    return actualMemory.variables.str.get_value(direction)
  elif 106000 <= direction and direction <= 107999:
    return actualMemory.variables.cha.get_value(direction)
  elif 108000 <= direction and direction <= 109999:
    return actualMemory.variables.boo.get_value(direction)
  elif 110000 <= direction and direction <= 111999:
    return actualMemory.temporals.int.get_value(direction)
  elif 112000 <= direction and direction <= 113999:
    return actualMemory.temporals.flo.get_value(direction)
  elif 114000 <= direction and direction <= 115999:
    return actualMemory.temporals.str.get_value(direction)
  elif 116000 <= direction and direction <= 117999:
    return actualMemory.temporals.cha.get_value(direction)
  elif 118000 <= direction and direction <= 119999:
    return actualMemory.temporals.boo.get_value(direction)
  elif 200000 <= direction and direction <= 201999:         # GLOBAL
    return globalMemory.variables.int.get_value(direction)
  elif 202000 <= direction and direction <= 203999:
    return globalMemory.variables.flo.get_value(direction)
  elif 204000 <= direction and direction <= 205999:
    return globalMemory.variables.str.get_value(direction)
  elif 206000 <= direction and direction <= 207999:
    return globalMemory.variables.cha.get_value(direction)
  elif 208000 <= direction and direction <= 209999:
    return globalMemory.variables.boo.get_value(direction)
  elif 210000 <= direction and direction <= 211999:
    return globalMemory.temporals.int.get_value(direction)
  elif 212000 <= direction and direction <= 213999:
    return globalMemory.temporals.flo.get_value(direction)
  elif 214000 <= direction and direction <= 215999:
    return globalMemory.temporals.str.get_value(direction)
  elif 216000 <= direction and direction <= 217999:
    return globalMemory.temporals.cha.get_value(direction)
  elif 218000 <= direction and direction <= 219999:
    return globalMemory.temporals.boo.get_value(direction)
  elif 300000 <= direction and direction <= 301999:         # CONSTANTS
    return constantMemory.variables.int.get_value(direction)
  elif 302000 <= direction and direction <= 303999:
    return constantMemory.variables.flo.get_value(direction)
  elif 304000 <= direction and direction <= 305999:
    return constantMemory.variables.str.get_value(direction)
  elif 306000 <= direction and direction <= 307999:
    return constantMemory.variables.cha.get_value(direction)
  elif 308000 <= direction and direction <= 309999:
    return constantMemory.variables.boo.get_value(direction)

pointer = 0
if len(memory) > 0:
  for var in memory:
    insert_into_corresponding_direction(var, memory[var])
    
while(pointer < len(quadruples)):
  pointer = execute_quadruple(quadruples[pointer], pointer)