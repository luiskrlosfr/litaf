class VarTable:
  def __init__(self):
    self.vars = {}

  def push(self, varName, varType, varDir):
    self.vars[varName] = [varType, varDir]
  
class ScopeTable:
  def __init__(self):
    self.scopes = {}

  def push(self, scopeName, scopeType, varTable, dir, returnVal):
    self.scopes[scopeName] = [scopeType, varTable, dir, returnVal]