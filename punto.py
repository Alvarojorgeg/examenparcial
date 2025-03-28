import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.x != 0 and self.y == 0:
            return "Eje X"
        else:
            return "Origen"


    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)



    def distancia(self, otro):
        return math.sqrt((otro.x - self.x)**2 + (otro.y - self.y)**2)
