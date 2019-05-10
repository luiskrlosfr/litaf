# Structure for Variables able
class VarTable:
  def __init__(self):
    self.vars = {}

  def push(self, varName, varType, varDir, varSize):
    self.vars[varName] = [varType, varDir, varSize]
  
# Structure for Scopes Table
class ScopeTable:
  def __init__(self):
    self.scopes = {}

  def push(self, scopeName, scopeType, varTable, dir, returnVal):
    self.scopes[scopeName] = [scopeType, varTable, dir, returnVal]