from jugador import Jugador
from equipo_de_futbol import EquipoDeFutbol

# crear jugadores
jugador1 = Jugador("James Rodriguez",  "Mediocampista", 33, 10)
jugador2 = Jugador("Falcao Garcia",    "Delantero",     38,  9)
jugador3 = Jugador("Davinson Sanchez", "Defensor",      28,  2)
jugador4 = Jugador("David Ospina",     "Portero",       36,  1)

# crear equipos
equipo1 = EquipoDeFutbol("Atletico Nacional", "Medellin", "Jhon Bodmer")
equipo2 = EquipoDeFutbol("Millonarios FC",    "Bogota",   "Alberto Gamero")

# agregar jugadores al equipo1
print("--- Agregando jugadores a", equipo1.get_nombre(), "---")
equipo1.agregar_jugador(jugador1)
equipo1.agregar_jugador(jugador2)
equipo1.agregar_jugador(jugador3)
equipo1.agregar_jugador(jugador4)

# mostrar plantilla
print()
equipo1.mostrar_plantilla()

# remover un jugador y pasarlo al equipo2
print()
print("--- Transferencia ---")
equipo1.remover_jugador("James Rodriguez")
equipo2.agregar_jugador(jugador1)

# mostrar plantillas finales
print()
equipo1.mostrar_plantilla()
print()
equipo2.mostrar_plantilla()

# usar setters
print()
print("--- Actualizando datos ---")
jugador2.set_edad(39)
print("Nueva edad de Falcao:", jugador2.get_edad())

equipo1.set_entrenador("Nuevo Entrenador")
print("Nuevo entrenador de Nacional:", equipo1.get_entrenador())
