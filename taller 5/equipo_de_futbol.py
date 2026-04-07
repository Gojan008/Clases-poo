from jugador import Jugador

class EquipoDeFutbol:

    def __init__(self, nombre, ciudad, entrenador):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__entrenador = entrenador
        self.__jugadores = []

    def get_nombre(self):
        return self.__nombre

    def get_ciudad(self):
        return self.__ciudad

    def get_entrenador(self):
        return self.__entrenador

    def get_jugadores(self):
        return self.__jugadores

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def set_entrenador(self, entrenador):
        self.__entrenador = entrenador

    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)
        jugador.set_equipo_actual(self)
        print(jugador.get_nombre(), "agregado al equipo", self.__nombre)

    def remover_jugador(self, nombre):
        for j in self.__jugadores:
            if j.get_nombre() == nombre:
                self.__jugadores.remove(j)
                j.set_equipo_actual(None)
                print(nombre, "removido del equipo", self.__nombre)
                return
        print("No se encontro al jugador", nombre)

    def mostrar_plantilla(self):
        print("Equipo:", self.__nombre)
        print("Ciudad:", self.__ciudad)
        print("Entrenador:", self.__entrenador)
        print("Jugadores:")
        for j in self.__jugadores:
            print(" -", j.get_nombre(), j.get_posicion(), j.get_numero_camiseta())
