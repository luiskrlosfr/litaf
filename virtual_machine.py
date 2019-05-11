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
  elif instruction == 'VER':
    verify_list_range(quad.op1, quad.result)
  elif instruction == 'SUM_DIR':
    add_direction(quad)
  elif instruction == '+' or instruction == '-' or instruction == '*' or instruction == '/':
    check_list_data_type(instruction, quad.op1, quad.op2)
    execute_aritmetic_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == '==' or instruction == '!=' or instruction == '>=' or instruction == '>' or instruction == '<=' or instruction == '<':
    check_list_data_type(instruction, quad.op1, quad.op2)
    execute_comparison_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == '&&' or instruction == '||':
    check_list_data_type(instruction, quad.op1, quad.op2)
    execute_logic_operation(instruction, quad.op1, quad.op2, quad.result)
  elif instruction == 'Writing':
    output_msg(quad.result)
  elif instruction == 'Lecture':
    input_variable(quad.result)
  elif instruction == '=':
    execute_assign(quad.op1, quad.result)
  pointer += 1
  return pointer

# Executes aritmetic operation according to operator
def execute_aritmetic_operation(op, left, right, res_direction):
  global vm_memory
  global returnStack
  global pointerStack
  l = get_value(left, left)
  r = get_value(right, right)
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
  var = get_value(left, left)
  check_list_data_type('=', left, res_direction)
  if(res_direction in range(140000, 141999) or res_direction in range(240000, 241999)):
    res_direction = get_value_assign(res_direction, res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, var)

# Executes logical operations according to operator
def execute_comparison_operation(op, left, right, res_direction):
  global vm_memory
  result = compare_operations[op](get_value(left, left), get_value(right, right))
  if not check_existence(res_direction):
    variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, result)

# Execute logical operations according to operator
def execute_logic_operation(op, left, right, res_direction):
  global vm_memory
  result = logic_operations[op](get_value(left, left), get_value(right, right))
  if not check_existence(res_direction):
    variable_in_memory(res_direction)
  vm_memory.real_memory(res_direction).set_value(res_direction, result)

# Evaluates if two values are equal
def evaluate_goto_false(pointer, quadruple):
  global vm_memory
  if evaluate_logic_operation('==', get_value(quadruple.op1, quadruple.op1), False):
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
  value = get_value(direction, direction)
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
    return_val = get_value(quad.result, quad.result)
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
  params.append(get_value(direction, direction))

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

# Add an offset to Base Direction of List
def add_direction(quad):
  global vm_memory
  result = quad.op1 + get_value(quad.op2, quad.op2)
  if not check_existence(result):
      variable_in_memory(result)
  if  (140000 <= quad.result and quad.result <= 141999) or (240000 <= quad.result and quad.result <= 241999):
    if not check_existence(quad.result):
      variable_in_memory(quad.result)
  vm_memory.real_memory(quad.result).set_value(quad.result, result)

def get_value(memory_dir, direction):
  global vm_memory
  dir = vm_memory.real_memory(memory_dir).get_value(direction)
  if((140000 <= direction and direction <= 141999) or (240000 <= direction and direction <= 241999)) and (dir in range(120000, 121999) or dir in range(140000, 141999) or dir in range(220000, 221999) or dir in range(240000, 241999)):
    dir = vm_memory.real_memory(dir).get_value(dir)
  return dir

def get_value_assign(memory_dir, direction):
  global vm_memory
  dir = vm_memory.real_memory(memory_dir).get_value(direction)
  return dir

# Check if value stored in list is compatible with other value to execute Quadruple
def check_list_data_type(operator, operand1, operand2):
  global vm_memory
  type1 = get_type(operand1)
  type2 = get_type(operand2)
  if(operator != '==' and operator != '!=') and (type1 != type2 and (operator != '=' and ((operand2 not in (140000, 141999)) or (operand2 not in (240000, 241999))))):
    if(type1 == 'flo' and type2 != 'int') or (type1 == 'int' and operator == '=') or (type1 == 'int' and type2 != 'flo') or (type1 == 'str' and type2 != 'cha'):
      print("Error: type mismatch between value stored in list and other operand")
      sys.exit(0)

# Check if index is inside limit for list
def verify_list_range(index, limit):
  index = get_value(index, index)
  limit = get_value(limit, limit)
  if (limit <= index) or (index < 0):
    print("Error: index out of range")
    sys.exit(0)

# Get type of data
def get_type(direction):
  global vm_memory
  value = vm_memory.real_memory(direction).get_value(direction)
  if(120000 <= direction and direction <= 121999) or (220000 <= direction and direction <= 221999):
    if(type(value) == type(1)):
      value = 'int'
    elif(type(value) == type(1.1)):
      value = 'flo'
    elif(type(value) == type("s")):
      if(len(value) == 1):
        value = 'cha'
      else:
        value = 'str'
  elif(140000 <= direction and direction <= 141999) or (240000 <= direction and direction <= 241999):
    value = get_type(vm_memory.real_memory(direction).get_value(direction))
  else:
    return vm_memory.real_memory(direction).typ
  return value


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