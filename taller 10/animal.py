class Animal:
    def __init__(self, nombre, edad, especie):
        self._nombre = nombre
        self._edad = edad
        self._especie = especie

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_especie(self):
        return self._especie

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

    def set_especie(self, especie):
        self._especie = especie

    def hacer_sonido(self):
        print("El animal hace un sonido")

    def comer(self):
        print(self._nombre, "esta comiendo")

    def mostrar_info(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad, "anios")
        print("Especie:", self._especie)
