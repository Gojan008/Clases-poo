from vehiculo_terrestre import VehiculoTerrestre
from vehiculo_acuatico import VehiculoAcuatico

auto1   = VehiculoTerrestre("Toyota",    "Corolla",              5,  4)
auto2   = VehiculoTerrestre("Chevrolet", "Bus Intermunicipal",  40,  6)
barco1  = VehiculoAcuatico("Yamaha",    "Lancha 200",            8, "Motor fuera de borda")
barco2  = VehiculoAcuatico("Ferretti",  "Yate 500",             20, "Motor diesel")

vehiculos = [auto1, auto2, barco1, barco2]

for v in vehiculos:
    print("--------------------")
    v.mostrar_info()

print()
print("Probando mover() - polimorfismo:")
for v in vehiculos:
    v.mover()

print()
print("Frenando vehiculos terrestres:")
auto1.frenar()
auto2.frenar()

print()
print("Anclando vehiculos acuaticos:")
barco1.anclar()
barco2.anclar()

print()
print("Usando setters:")
auto1.set_marca("Toyota Actualizado")
barco1.set_tipo_propulsion("Electrico")
print("Nueva marca auto1:", auto1.get_marca())
print("Nueva propulsion barco1:", barco1.get_tipo_propulsion())
