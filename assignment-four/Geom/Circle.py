import math as mth
from Geom import Geom

class Circle(Geom):
  
  def __init__ (self,radius):
    self.radius = radius
    super().__init__()

  # area method  
  def area(self):
     return mth.pi * self.radius **2
