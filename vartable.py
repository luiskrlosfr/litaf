class VarTable:
  def __init__(self):
    self.vars = {}

  def push(self, varName, varType, varVisibility):
    self.vars[varName] = [varType, varVisibility]

class ScopeTable:
  def __init__(self):
    self.scopes = {}

  def push(self, scopeName, scopeType, varTable, scopeVisibility):
    self.scopes[scopeName] = [scopeType, varTable, scopeVisibility]