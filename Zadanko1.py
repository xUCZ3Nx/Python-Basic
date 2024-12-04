import math
class ProstokatWUkadzieKartezjanskim:
    def __init__(self, x1, x2, y1, y2):
        self.changexandy(x1, x2, y1, y2)
    def __str__(self):
        return f"x1={self.x1}, x2={self.x2}, y1={self.y1}, y2={self.y2}"
    def printall(self):
        return f"x1={self.x1}, x2={self.x2}, y1={self.y1}, y2={self.y2}"
    def Oblicz_pole_prostokata(self):
        return math.sqrt((self.x2-self.x1)**2)*math.sqrt((self.y2-self.y1)**2)
    def changexandy(self, x1, x2, y1, y2):
        self.x1 = x1 
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 
    def Obwod(self):
        return 2*((self.x2-self.x1)+(self.y2-self.y1))
    def Czy_w_srodku(self, a, b):
        amin = min(self.x1, self.x2)
        amax = max(self.x1, self.x2)
        bmin = min(self.y1, self.y2)
        bmax = max(self.y1, self.y2)
        if a > amin and a < amax and b > bmin and b < bmax:
            print("Punkt znajduje sie w prostokacie")
        else:
            print("Punkt nie znajduje sie w prostokacie")
    def wszystkie_informacje(self):
        print(f"Polecenie 6\nWspolrzedne wierzcholkow: {x.printall()}")
        x.printall() # nie zwraca bo jest return zamiast print
        print("Pole prostokata:")
        print(x.Oblicz_pole_prostokata())
        print("Obwod prostokata:")
        print(x.Obwod())

x = ProstokatWUkadzieKartezjanskim(0,1,0,1)
# x.printall()
# print(x.Oblicz_pole_prostokata())
x.changexandy(1, 2, 1, 2) # 5. zmiana wymiarow
# x.printall()
# print(x.Oblicz_pole_prostokata())
# print(x.Obwod())
x.Czy_w_srodku(1.5, 1.5) # 4. Sprawdz czy punkt znajduje sie w srodku
x.wszystkie_informacje() # 6. wszystkie informajce
print(x)
