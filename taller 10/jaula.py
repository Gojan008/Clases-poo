class Jaula:
    def __init__(self, numero, capacidad, cuidador):
        self._numero = numero
        self._capacidad = capacidad
        self._cuidador = cuidador
        self._animales = []

    def get_numero(self):
        return self._numero

    def get_capacidad(self):
        return self._capacidad

    def get_cuidador(self):
        return self._cuidador

    def get_animales(self):
        return self._animales

    def set_numero(self, numero):
        self._numero = numero

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def set_cuidador(self, cuidador):
        self._cuidador = cuidador

    def agregar_animal(self, animal):
        if len(self._animales) < self._capacidad:
            self._animales.append(animal)
            print(animal.get_nombre(), "agregado a la jaula", self._numero)
        else:
            print("La jaula", self._numero, "esta llena")

    def mostrar_info(self):
        print("Jaula numero:", self._numero)
        print("Capacidad:", self._capacidad)
        self._cuidador.mostrar_info()
        print("Animales en la jaula:")
        for animal in self._animales:
            animal.mostrar_info()
            print("  ---")
