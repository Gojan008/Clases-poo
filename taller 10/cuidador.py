class Cuidador:
    def __init__(self, nombre, anios_experiencia):
        self._nombre = nombre
        self._anios_experiencia = anios_experiencia

    def get_nombre(self):
        return self._nombre

    def get_anios_experiencia(self):
        return self._anios_experiencia

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_anios_experiencia(self, anios):
        self._anios_experiencia = anios

    def mostrar_info(self):
        print("Cuidador:", self._nombre)
        print("Experiencia:", self._anios_experiencia, "anios")
