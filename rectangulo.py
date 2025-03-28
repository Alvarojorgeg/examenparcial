from punto import Punto

class Rectangulo:
    def __init__(self, p1=Punto(), p2=Punto()):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p2.x - self.p1.x)

    def altura(self):
        return abs(self.p2.y - self.p1.y)

    def area(self):
        return self.base() * self.altura()
