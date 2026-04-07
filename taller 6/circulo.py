from forma import Forma
import math

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return math.pi * self.__radio ** 2

    def mostrar_info(self):
        print("Figura: Circulo")
        print("Radio:", self.__radio)
        super().mostrar_info()
