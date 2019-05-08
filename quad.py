# Structure for Quadruples
class Quad:
  def __init__(self, operator, op1, op2, result):
    self.operator = operator
    self.op1 = op2 
    self.op2 = op1
    self.result = result

  def print(self, num):
    print("Quad {}: ".format(num) + str(self.operator) + ", " + str(self.op1) + ", " + str(self.op2) + ", " + str(self.result))
  
    

