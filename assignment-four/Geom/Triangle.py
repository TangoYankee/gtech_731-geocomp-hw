from .Geom import Geom

class Triangle(Geom):
  
  def __init__(self, base, height):
    self.base = base
    self.height = height
    super().__init__()

  def area(self):
    return (self.base * self.height) / 2