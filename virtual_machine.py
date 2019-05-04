from parser import quadruples, memory
from virtual_memory import BigMemory, Memory
import operator

memoryStack = []
vm_memory = BigMemory()
# actualMemory = Memory(100000, 110000)
# Memory(300000, 310000)
# globalMemory = Memory(200000, 210000)
# constantMemory = Memory(300000, None)

arithmetic_operations = { '+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv }

def execute_quadruple(quad, ip):
  global memoryStack
  global vm_memory
  instruction = quad.operator
  pointer = ip
  if instruction == 'GoTo':
    create_local_memory()
    return quad.result
  elif instruction == 'ERA':
    memoryStack.append(vm_memory.locals)
    create_local_memory()
  elif instruction == 'GoSub':
    vm_memory.set_local(memoryStack.pop())
  elif instruction == '+' or instruction == '-' or instruction == '*' or instruction == '/':
    execute_aritmetic_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == 'Writing':
    output_msg(quad.result)
  elif instruction == '=':
    execute_assign(vm_memory.real_memory(quad.op1).get_value(quad.op1), quad.result)
  pointer += 1
  return pointer

# Executes aritmetic operation according to operator
def execute_aritmetic_operation(op, left, right, res_direction):
  global vm_memory
  result =  arithmetic_operations[op](vm_memory.real_memory(left).get_value(left), vm_memory.real_memory(right).get_value(right))
  vm_memory.real_memory(res_direction).push(result)

# Executes assign operation
def execute_assign(left, res_direction):
  global vm_memory
  variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, left)

# Creates local Memory for function
def create_local_memory():
  global vm_memory
  vm_memory.set_local(Memory(100000, 110000))

# Print function for Writing quad instruction
def output_msg(direction):
  global vm_memory
  print(vm_memory.real_memory(direction).get_value(direction))

# Check if variable direction exists in memory
def variable_in_memory(direction):
  global vm_memory
  while(0 <= direction - (len(vm_memory.real_memory(direction).vars) + vm_memory.real_memory(direction).offset)):
    vm_memory.real_memory(direction).push(None)

pointer = 0
if len(memory) > 0:
  for var in memory:
    vm_memory.real_memory(var).push(memory[var])
    
while(pointer < len(quadruples)):
  pointer = execute_quadruple(quadruples[pointer], pointer)