class Jugador:

    def __init__(self, nombre, posicion, edad, numero_camiseta):
        self.__nombre = nombre
        self.__posicion = posicion
        self.__edad = edad
        self.__numero_camiseta = numero_camiseta
        self.__equipo_actual = None

    def get_nombre(self):
        return self.__nombre

    def get_posicion(self):
        return self.__posicion

    def get_edad(self):
        return self.__edad

    def get_numero_camiseta(self):
        return self.__numero_camiseta

    def get_equipo_actual(self):
        return self.__equipo_actual

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_posicion(self, posicion):
        self.__posicion = posicion

    def set_edad(self, edad):
        self.__edad = edad

    def set_numero_camiseta(self, numero_camiseta):
        self.__numero_camiseta = numero_camiseta

    def set_equipo_actual(self, equipo):
        self.__equipo_actual = equipo

    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("Posicion:", self.__posicion)
        print("Edad:", self.__edad)
        print("Numero de camiseta:", self.__numero_camiseta)
        if self.__equipo_actual is None:
            print("Equipo: Sin equipo")
        else:
            print("Equipo:", self.__equipo_actual.get_nombre())
