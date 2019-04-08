class Quad:
  def __init__(self, operator, op1, op2, result):
    self.operator = operator
    self.op1 = op2 
    self.op2 = op1
    self.result = result

  def print(self):
    print("Quad: " + self.operator + ", " + self.op1 + ", " + self.op2 + ", " + self.result)
  
    

