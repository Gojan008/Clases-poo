from vehiculo import Vehiculo

class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, numero_ruedas):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self.__numero_ruedas = numero_ruedas

    def get_numero_ruedas(self):
        return self.__numero_ruedas

    def set_numero_ruedas(self, numero_ruedas):
        self.__numero_ruedas = numero_ruedas

    def frenar(self):
        print("El vehiculo terrestre esta frenando")

    def mover(self):
        print("El vehiculo terrestre se mueve por la carretera con", self.__numero_ruedas, "ruedas")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Terrestre")
        print("Numero de ruedas:", self.__numero_ruedas)
