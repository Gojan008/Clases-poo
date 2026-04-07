from mamifero import Mamifero
from ave import Ave
from cuidador import Cuidador
from jaula import Jaula

# Paso 1: crear cuidadores
cuidador1 = Cuidador("Pedro Ramirez", 10)
cuidador2 = Cuidador("Laura Gomez",    5)

# Paso 2: crear animales
leon   = Mamifero("Leon",   8, "Panthera leo",      "Pelaje corto")
tigre  = Mamifero("Tigre",  5, "Panthera tigris",   "Pelaje rayado")
aguila = Ave("Aguila",      3, "Aquila chrysaetos", 180)
tucan  = Ave("Tucan",       2, "Ramphastos toco",    50)

# Paso 3: crear jaulas y agregar animales
jaula1 = Jaula(1, 2, cuidador1)
jaula2 = Jaula(2, 2, cuidador2)

jaula1.agregar_animal(leon)
jaula1.agregar_animal(tigre)
jaula1.agregar_animal(leon)   # intento cuando esta llena

jaula2.agregar_animal(aguila)
jaula2.agregar_animal(tucan)

# Mostrar info de cada jaula
print()
print("---------- Jaula 1 ----------")
jaula1.mostrar_info()

print()
print("---------- Jaula 2 ----------")
jaula2.mostrar_info()

# Polimorfismo: hacer_sonido() actua diferente segun el tipo
print()
print("Sonidos de todos los animales:")
animales = [leon, tigre, aguila, tucan]
for animal in animales:
    animal.hacer_sonido()

# Metodos especificos de cada subclase
print()
leon.amamantar()
tigre.amamantar()
aguila.volar()
tucan.volar()

# Setters
print()
cuidador1.set_anios_experiencia(12)
print("Experiencia actualizada de Pedro:", cuidador1.get_anios_experiencia(), "anios")
