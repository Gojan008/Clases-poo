from animal import Animal

class Ave(Animal):
    def __init__(self, nombre, edad, especie, envergadura_alas):
        super().__init__(nombre, edad, especie)
        self._envergadura_alas = envergadura_alas

    def get_envergadura_alas(self):
        return self._envergadura_alas

    def set_envergadura_alas(self, envergadura):
        self._envergadura_alas = envergadura

    def volar(self):
        print(self._nombre, "esta volando con alas de", self._envergadura_alas, "cm")

    def hacer_sonido(self):
        print(self._nombre, "esta cantando")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Ave")
        print("Envergadura de alas:", self._envergadura_alas, "cm")
