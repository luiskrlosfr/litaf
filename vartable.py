class VarTable:
  def __init__(self):
    self.vars = {}

  def push(self, varName, varType):
    self.vars[varName] = varType

class ScopeTable:
  def __init__(self):
    self.scopes = {}

  def push(self, scopeName, scopeType, varTable):
    self.scopes[scopeName] = [scopeType, varTable]