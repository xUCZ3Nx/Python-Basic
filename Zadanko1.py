import math
class ProstokatWUkadzieKartezjanskim:
    def __init__(self, x1, x2, y1, y2):
        self.changexandy(x1, x2, y1, y2)
    def printall(self):
        print(f"x1={self.x1}, x2={self.x2}, y1={self.y1}, y2={self.y2}")
    def Oblicz_pole_prostokata(self):
        return math.sqrt((self.x2-self.x1)**2)*math.sqrt((self.y2-self.y1)**2)
    def changexandy(self, x1, x2, y1, y2):
        self.x1 = x1 
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 


x = ProstokatWUkadzieKartezjanskim(0,0,1,1)
x.printall()
print(x.Oblicz_pole_prostokata())
x.changexandy(1, 1, 2, 2)
x.printall()
print(x.Oblicz_pole_prostokata())