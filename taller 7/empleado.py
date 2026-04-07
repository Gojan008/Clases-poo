class Empleado:

    def __init__(self, nombre, id_empleado, salario_base):
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__salario_base = salario_base

    def get_nombre(self):
        return self.__nombre

    def get_id_empleado(self):
        return self.__id_empleado

    def get_salario_base(self):
        return self.__salario_base

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self):
        return self.__salario_base

    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("ID:", self.__id_empleado)
        print("Salario base:", self.__salario_base)
