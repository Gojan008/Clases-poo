from empleado import Empleado

class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, id_empleado, salario_base, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado, salario_base)
        self.__tarifa_hora = tarifa_hora
        self.__horas_trabajadas = horas_trabajadas

    def get_tarifa_hora(self):
        return self.__tarifa_hora

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas

    def set_tarifa_hora(self, tarifa_hora):
        self.__tarifa_hora = tarifa_hora

    def set_horas_trabajadas(self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.__tarifa_hora * self.__horas_trabajadas

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Por horas")
        print("Tarifa por hora:", self.__tarifa_hora)
        print("Horas trabajadas:", self.__horas_trabajadas)
        print("Salario total:", self.calcular_salario())
