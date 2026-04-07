from circulo import Circulo
from rectangulo import Rectangulo

c1 = Circulo("Rojo",   5)
c2 = Circulo("Azul",  10)
r1 = Rectangulo("Verde",  4,  8)
r2 = Rectangulo("Amarillo", 3, 6)

formas = [c1, c2, r1, r2]

for forma in formas:
    print("--------------------")
    forma.mostrar_info()

# Polimorfismo: calcular_area() actua diferente segun la figura
print()
print("Resumen de areas:")
for forma in formas:
    print("Area:", round(forma.calcular_area(), 2))

# Setters
print()
c1.set_color("Morado")
c1.set_radio(7)
print("Nuevo color del circulo 1:", c1.get_color())
print("Nuevo radio del circulo 1:", c1.get_radio())
print("Nueva area:", round(c1.calcular_area(), 2))
