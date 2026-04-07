from empleado_tiempo_completo import EmpleadoTiempoCompleto
from empleado_por_horas import EmpleadoPorHoras

# crear empleados
emp1 = EmpleadoTiempoCompleto("Ana Garcia",    "E001", 1000000, 3500000)
emp2 = EmpleadoTiempoCompleto("Luis Martinez", "E002", 1000000, 4200000)
emp3 = EmpleadoPorHoras("Maria Rodriguez", "E003", 500000, 25000, 80)
emp4 = EmpleadoPorHoras("Carlos Perez",    "E004", 500000, 30000, 60)

# mostrar info de cada empleado
empleados = [emp1, emp2, emp3, emp4]

for emp in empleados:
    print("--------------------")
    emp.mostrar_info()

# polimorfismo: calcular_salario() actua diferente segun el tipo
print()
print("Resumen de salarios:")
for emp in empleados:
    print(emp.get_nombre(), "->", emp.calcular_salario())

# usar setters
print()
print("Actualizando datos:")
emp1.set_nombre("Ana Garcia Lopez")
emp1.set_salario_mensual_fijo(3800000)
print("Nuevo nombre:", emp1.get_nombre())
print("Nuevo salario:", emp1.calcular_salario())
