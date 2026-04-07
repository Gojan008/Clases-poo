class Vehiculo:
    def __init__(self, marca, modelo, capacidad_pasajeros):
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad_pasajeros = capacidad_pasajeros

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_capacidad_pasajeros(self):
        return self.__capacidad_pasajeros

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_capacidad_pasajeros(self, capacidad):
        self.__capacidad_pasajeros = capacidad

    def mover(self):
        print("El vehiculo se esta moviendo")

    def mostrar_info(self):
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Capacidad de pasajeros:", self.__capacidad_pasajeros)
