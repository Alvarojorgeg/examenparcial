# Hecho por Alvaro Jorge Gonzalez

from punto import Punto
from rectangulo import Rectangulo

def pedir_punto(nombre):
    print(f"\nPunto {nombre}")
    x = float(input("Coordenada X: "))
    y = float(input("Coordenada Y: "))
    return Punto(x, y)

print("Introduce los 4 puntos:")
A = pedir_punto("A")
B = pedir_punto("B")
C = pedir_punto("C")
D = pedir_punto("D")

print(f"\nA = {A}, B = {B}, C = {C}, D = {D}")

if input("\n¿Ver cuadrantes de A, C y D? (s/n): ").lower() == "s":
    print("A:", A.cuadrante())
    print("C:", C.cuadrante())
    print("D:", D.cuadrante())
