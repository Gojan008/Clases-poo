class Forma:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def calcular_area(self):
        return 0

    def mostrar_info(self):
        print("Color:", self._color)
        print("Area:", self.calcular_area())
