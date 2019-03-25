class VarTable:
  def __init__(self):
    self.vars = []

  def push(self, varType, varName):
    self.vars.append([varType, varName])