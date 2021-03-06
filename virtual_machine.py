import operator
import sys
from parser import quadruples, memory
from virtual_memory import BigMemory, Memory

memoryStack = []
pointerStack = []
returnStack = []
params = []
vm_memory = BigMemory()

arithmetic_operations = { '+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv }
compare_operations = { '==' : operator.eq,  '!=' : operator.ne, '>=' : operator.ge, '>' : operator.gt, '<=' : operator.le, '<' : operator.lt }
logic_operations = { '&&' : operator.and_, '||' : operator.or_ }

# Decides what the Quadrupe is suposed to do
def execute_quadruple(quad, ip):
  global memoryStack
  global pointerStack
  global vm_memory
  instruction = quad.operator
  pointer = ip
  if instruction == 'GoTo':
    return quad.result
  elif instruction == 'GoToF':
    return evaluate_goto_false(pointer, quad)
  elif instruction == 'ERA':
    # memoryStack.append(vm_memory.locals)
    # create_local_memory()
    global params
    params = []
  elif instruction == 'PARAM':
    insert_params(quad)
  elif instruction == 'GoSub':
    pointerStack.append(pointer)
    memoryStack.append(vm_memory.locals)
    create_local_memory()
    fill_params()
    return quad.result
  elif instruction == 'return':
    return_value(quad)
  elif instruction == 'EndProc':
    pointer = pointerStack.pop()
  elif instruction == 'SetReturnValue':
    assign_return_value(quad.result)
  elif instruction == '+' or instruction == '-' or instruction == '*' or instruction == '/':
    execute_aritmetic_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == '==' or instruction == '!=' or instruction == '>=' or instruction == '>' or instruction == '<=' or instruction == '<':
    execute_comparison_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == '&&' or instruction == '||':
    execute_logic_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == 'Writing':
    output_msg(quad.result)
  elif instruction == 'Lecture':
    input_variable(quad.result)
  elif instruction == '=':
    execute_assign(vm_memory.real_memory(quad.op1).get_value(quad.op1), quad.result)
  pointer += 1
  return pointer

# Executes aritmetic operation according to operator
def execute_aritmetic_operation(op, left, right, res_direction):
  global vm_memory
  global returnStack
  global pointerStack
  l = vm_memory.real_memory(left).get_value(left)
  r = vm_memory.real_memory(right).get_value(right)
  if op == '/' and r == 0 or r == '0':
    print('Error: cannot divide by 0')
    sys.exit(0)
  result =  arithmetic_operations[op](l, r)
  if op == '/' and vm_memory.real_memory(left).typ == 'int' and vm_memory.real_memory(right).typ == 'int':
    result = int(result)
  if not check_existence(res_direction):
    variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, result)

# Executes assign operation
def execute_assign(left, res_direction):
  global vm_memory
  variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, left)

# Executes logical operations according to operator
def execute_comparison_operation(op, left, right, res_direction):
  global vm_memory
  result = compare_operations[op](vm_memory.real_memory(left).get_value(left), vm_memory.real_memory(right).get_value(right))
  if not check_existence(res_direction):
    variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, result)

# Execute logical operations according to operator
def execute_logic_operation(op, left, right, res_direction):
  global vm_memory
  result = logic_operations[op](vm_memory.real_memory(left).get_value(left), vm_memory.real_memory(right).get_value(right))
  if not check_existence(res_direction):
    variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, result)

# Evaluates if two values are equal
def evaluate_goto_false(pointer, quadruple):
  global vm_memory
  if evaluate_logic_operation('==', vm_memory.real_memory(quadruple.op1).get_value(quadruple.op1), False):
    return quadruple.result
  else:
    return pointer + 1

# Evaluates a logic operation and returns result
def evaluate_logic_operation(op, left, right):
  return compare_operations[op](left, right)

# Creates local Memory for function
def create_local_memory():
  global vm_memory
  vm_memory.set_local(Memory(100000, 110000))

# Print function for Writing quad instruction
def output_msg(direction):
  global vm_memory
  value = vm_memory.real_memory(direction).get_value(direction)
  if value == "n/":
    print('')
  else:
    print(value, end = '')

# Inputs from user to variable
def input_variable(direction):
  global vm_memory
  value = input("insert {} > ".format(vm_memory.real_memory(direction).typ))
  typ = vm_memory.real_memory(direction).typ 
  if not check_existence(direction):
    variable_in_memory(direction)
  if typ == 'int':
    value = int(value)
  elif typ == 'flo':
    value = float(value)
  vm_memory.real_memory(direction).set_value(direction, value)

# Create empty slots of memory if variable doesn't exists in it
def variable_in_memory(direction):
  global vm_memory
  while(0 <= direction - (len(vm_memory.real_memory(direction).vars) + vm_memory.real_memory(direction).offset)):
    vm_memory.real_memory(direction).push(None)

# Verify if variable exists in memory
def check_existence(direction):
  global vm_memory
  if(0 <= direction - (len(vm_memory.real_memory(direction).vars) + vm_memory.real_memory(direction).offset)):
    return False
  else:
    return True

# Appends returned value to stack if function is not void and changes actual local memory to top of memory stack
def return_value(quad):
  global vm_memory
  global memoryStack
  global returnStack
  if quad.result != None:
    return_val = vm_memory.real_memory(quad.result).get_value(quad.result)
    returnStack.append(return_val)
  vm_memory.set_local(memoryStack.pop())

# If function had return value, assigns it to corresponding temporal in actual local memory
def assign_return_value(direction):
  global returnStack
  global quadruples
  global vm_memory
  if len(returnStack) > 0 :
    value = returnStack.pop()
    if not check_existence(direction):
      variable_in_memory(direction)
    vm_memory.real_memory(direction).set_value(direction, value)

# Inserts param real value into array so the new function can set values to its variables
def insert_params(quad):
  global params
  global vm_memory
  direction = quad.op1
  params.append(direction)
  params.append(vm_memory.real_memory(direction).get_value(direction))

# Creates local variables from function parameters
def fill_params():
  global vm_memory
  global params
  params.reverse()
  while len(params) > 0:
    direction = params.pop()
    value = params.pop()
    no_temporal = vm_memory.real_memory(direction).base_dir_by_type(direction)
    local_dir = vm_memory.real_memory(no_temporal).get_dir_as_local(no_temporal)
    vm_memory.real_memory(local_dir).push(value)

# Fill Constant Memory with Constant Memory from Parser
pointer = 0
if len(memory) > 0:
  for var in memory:
    vm_memory.real_memory(var).push(memory[var])

create_local_memory()

# Print Quadruples
# counter = 0
# for quad in quadruples:
#   quad.print(counter)
#   counter += 1

# Execute Quadruples list until Program Ends
while(pointer < len(quadruples)):
  pointer = execute_quadruple(quadruples[pointer], pointer)