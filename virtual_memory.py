FLO_CONS = 2000
STR_CONS = 4000
CHA_CONS = 6000
BOO_CONS = 8000

# Atomic class for Virtual Machine Memory.
class VirtualMemory:
  def __init__(self, offset, typ):
    self.vars = []
    self.offset = offset
    self.typ = typ

  def push(self, data):
    self.vars.append(data)

  def set_value(self, dir, val):
    self.vars[dir - self.offset] = val

  def set_direct_value(self, dir, val):
    self.vars[dir] = val

  def get_value(self, dir):
    return self.vars[dir - self.offset]

  def base_dir_by_type(self, dir):
    if 110000 <= dir and dir < 200000:
      return dir - 10000
    else:
      return dir

  def get_dir_as_local(self, dir):
    if 100000 <= dir and dir < 200000:
      return dir
    elif 200000 <= dir and dir < 300000:
      return dir - 100000
    elif 300000 <= dir:
      return dir - 200000

# Class that has all types of Virtual Memories
class Memories:
  def __init__(self, base_dir):
    self.base_dir = base_dir
    self.int = VirtualMemory(self.base_dir, 'int')
    self.flo = VirtualMemory(self.base_dir + FLO_CONS, 'flo')
    self.str = VirtualMemory(self.base_dir + STR_CONS, 'str')
    self.cha = VirtualMemory(self.base_dir + CHA_CONS, 'cha')
    self.boo = VirtualMemory(self.base_dir + BOO_CONS, 'boo')

  def get_type_by_direction(self, direction):
    if(self.base_dir <= direction and direction < self.base_dir + 2000):
      return self.int
    elif(self.base_dir + FLO_CONS <= direction and direction < self.base_dir + 4000):
      return self.flo
    elif(self.base_dir + STR_CONS <= direction and direction < self.base_dir + 6000):
      return self.str
    elif(self.base_dir + CHA_CONS <= direction and direction < self.base_dir + 8000):
      return self.cha
    elif(self.base_dir + BOO_CONS <= direction and direction < self.base_dir + 10000):
      return self.boo

# Class that groups Memories according to Scope | Type relation (i.e. 200000 would set Memory for Global Variables and 110000 for Local Temporals)
class Memory:
  def __init__(self, base_variables, base_temporals):
    self.base_variables = base_variables
    self.base_temporals = base_temporals
    self.variables = Memories(base_variables)
    if base_temporals == None:
      self.temporals = None
    else:
      self.temporals = Memories(base_temporals)

  # Return Memories according to direction (variables or temporals)
  def get_memory_by_direction(self, direction):
    if(self.base_variables <= direction and (self.base_temporals == None or direction < self.base_temporals)):
      return self.variables.get_type_by_direction(direction)
    elif(self.base_temporals <= direction and direction < self.base_temporals + 10000):
      return self.temporals.get_type_by_direction(direction)
    else:
      return None

  # def get_direct_memory_by_direction(self, direction):
  #   if(self.base_variables <= direction and (self.base_temporals == None or direction < self.base_temporals)):
  #     return self.variables.get_type_by_direction(direction)
  #   elif(self.base_temporals <= direction and direction < self.base_temporals + 10000):
  #     return self.temporals.get_type_by_direction(direction)
  #   else:
  #     return None

class BigMemory:
  def __init__(self):
    self.locals = None
    self.globals = Memory(200000, 201000)
    self.constants = Memory(300000, None)

  def set_local(self, memory):
    self.locals = memory

  # Get from what Memory direction should search for value
  def get_real_memory_by_direction(self, direction):
    if(300000 <= direction and direction < 400000):
      return self.constants.get_memory_by_direction(direction)
    elif(100000 <= direction and direction < 200000):
      return self.locals.get_memory_by_direction(direction)
    elif(200000 <= direction and direction < 300000):
      return self.globals.get_memory_by_direction(direction)
    else:
      return None

  # Return real value of direction
  def real_memory(self, direction):
    return self.get_real_memory_by_direction(direction)

  # def real_direct_memory(self, direction):
  #   return self.get_direct_memory_by_direction(direction)
  