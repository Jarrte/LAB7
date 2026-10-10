#rectangulo
def calcular_area_rectangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_area_circulo(radio):
    return 3.1416 * radio * radio


print("=== AREAS DE FIGURAS GEOMETRICAS ===")
print("1. Rectangulo")
print("2. Triangulo")
print("3. Circulo")

opcion = int(input("Elige una figura: "))

if opcion == 1:
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    print("Area del rectangulo:", calcular_area_rectangulo(base, altura))

elif opcion == 2:
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    print("Area del triangulo:", calcular_area_triangulo(base, altura))

elif opcion == 3:
    radio = float(input("Ingresa el radio: "))
    print("Area del circulo:", calcular_area_circulo(radio))

else:
    print("Opcion no valida")
