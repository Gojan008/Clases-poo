from forma import Forma

class Rectangulo(Forma):
    def __init__(self, color, largo, ancho):
        super().__init__(color)
        self.__largo = largo
        self.__ancho = ancho

    def get_largo(self):
        return self.__largo

    def get_ancho(self):
        return self.__ancho

    def set_largo(self, largo):
        self.__largo = largo

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def calcular_area(self):
        return self.__largo * self.__ancho

    def mostrar_info(self):
        print("Figura: Rectangulo")
        print("Largo:", self.__largo)
        print("Ancho:", self.__ancho)
        super().mostrar_info()
