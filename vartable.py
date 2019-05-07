class VarTable:
  def __init__(self):
    self.vars = {}

  def push(self, varName, varType, varDir, varVisibility):
    self.vars[varName] = [varType, varDir, varVisibility]
  
class ScopeTable:
  def __init__(self):
    self.scopes = {}

  def push(self, scopeName, scopeType, varTable, dir, returnVal, scopeVisibility):
    self.scopes[scopeName] = [scopeType, varTable, dir, returnVal, scopeVisibility]
