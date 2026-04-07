from empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre, id_empleado, salario_base, salario_mensual_fijo):
        super().__init__(nombre, id_empleado, salario_base)
        self.__salario_mensual_fijo = salario_mensual_fijo

    def get_salario_mensual_fijo(self):
        return self.__salario_mensual_fijo

    def set_salario_mensual_fijo(self, salario_mensual_fijo):
        self.__salario_mensual_fijo = salario_mensual_fijo

    def calcular_salario(self):
        return self.__salario_mensual_fijo

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo: Tiempo completo")
        print("Salario mensual fijo:", self.__salario_mensual_fijo)
        print("Salario total:", self.calcular_salario())
