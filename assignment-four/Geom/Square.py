from .Geom import Geom

class Square(Geom):
  
  def __init__ (self,side):
    self.side = side
    super().__init__()
  # area method  
  def area(self):
     return self.side **2
