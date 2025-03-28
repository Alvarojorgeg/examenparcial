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

if input("\n¿Ver vectores AB y BA? (s/n): ").lower() == "s":
    print("Vector AB:", A.vector(B))
    print("Vector BA:", B.vector(A))

if input("\n¿Ver distancias A-B y B-A? (s/n): ").lower() == "s":
    print("Distancia A-B:", round(A.distancia(B), 2))
    print("Distancia B-A:", round(B.distancia(A), 2))

    if input("\n¿Saber qué punto está más lejos del origen? (s/n): ").lower() == "s":
        origen = Punto(0, 0)
        distancias = {
            "A": A.distancia(origen),
            "B": B.distancia(origen),
            "C": C.distancia(origen)
        }
        mas_lejos = max(distancias, key=distancias.get)
        print("El punto más lejano al origen es:", mas_lejos)



    if input("\n¿Crear un rectángulo con A y B? (s/n): ").lower() == "s":
        r = Rectangulo(A, B)
        print("Base:", r.base())
        print("Altura:", r.altura())
        print("Área:", r.area())
