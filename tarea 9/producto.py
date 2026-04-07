class Producto:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def mostrar_info(self):
        print("Producto:", self.__nombre)
        print("Codigo:", self.__codigo)
