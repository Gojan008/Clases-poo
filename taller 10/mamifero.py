from animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, especie, tipo_pelaje):
        super().__init__(nombre, edad, especie)
        self._tipo_pelaje = tipo_pelaje

    def get_tipo_pelaje(self):
        return self._tipo_pelaje

    def set_tipo_pelaje(self, tipo_pelaje):
        self._tipo_pelaje = tipo_pelaje

    def amamantar(self):
        print(self._nombre, "esta amamantando a sus crias")

    def hacer_sonido(self):
        print(self._nombre, "hace un sonido de mamifero")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Mamifero")
        print("Tipo de pelaje:", self._tipo_pelaje)
