FLO_CONS = 2000
STR_CONS = 4000
CHA_CONS = 6000
BOO_CONS = 8000

# Atomic class for Virtual Machine Memory.
class VirtualMemory:
  def __init__(self, offset):
    self.vars = []
    self.offset = offset

  def push(self, data):
    self.vars.append(data)

  def set_value(self, dir, val):
    self.vars[dir] = val

  def get_value(self, dir):
    return self.vars[dir - self.offset]

# Class that has all types of Virtual Memories
class Memories:
  def __init__(self, base_dir):
    self.base_dir = base_dir
    self.int = VirtualMemory(self.base_dir)
    self.flo = VirtualMemory(self.base_dir + FLO_CONS)
    self.str = VirtualMemory(self.base_dir + STR_CONS)
    self.cha = VirtualMemory(self.base_dir + CHA_CONS)
    self.boo = VirtualMemory(self.base_dir + BOO_CONS)

# Class that groups Memories according to Scope | Type relation (i.e. 200000 would set Memory for Global Variables and 110000 for Local Temporals)
class Memory:
  def __init__(self, base_variables, base_temporals):
    self.variables = Memories(base_variables)
    if base_temporals == None:
      self.temporals = None
    else:
      self.temporals = Memories(base_temporals)

  