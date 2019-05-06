class VarTable:
  def __init__(self):
    self.vars = {}

<<<<<<< HEAD
  def push(self, varName, varType, varVisibility):
    self.vars[varName] = [varType, varVisibility]

=======
  def push(self, varName, varType, varDir):
    self.vars[varName] = [varType, varDir]
  
>>>>>>> 249da5f6b52b244a70497f7ff216da37b80d0a31
class ScopeTable:
  def __init__(self):
    self.scopes = {}

<<<<<<< HEAD
  def push(self, scopeName, scopeType, varTable, scopeVisibility):
    self.scopes[scopeName] = [scopeType, varTable, scopeVisibility]
=======
  def push(self, scopeName, scopeType, varTable, dir, returnVal):
    self.scopes[scopeName] = [scopeType, varTable, dir, returnVal]
>>>>>>> 249da5f6b52b244a70497f7ff216da37b80d0a31
