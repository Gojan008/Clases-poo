from vehiculo import Vehiculo

class VehiculoAcuatico(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, tipo_propulsion):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self._tipo_propulsion = tipo_propulsion

    def get_tipo_propulsion(self):
        return self._tipo_propulsion

    def set_tipo_propulsion(self, tipo_propulsion):
        self._tipo_propulsion = tipo_propulsion

    def anclar(self):
        print("El barco esta anclado")

    def mover(self):
        print("El vehiculo acuatico navega por el agua con propulsion:", self._tipo_propulsion)

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Acuatico")
        print("Tipo de propulsion:", self._tipo_propulsion)
