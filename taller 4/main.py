from automovil import Automovil

# ══════════════════════════════════════════════════════
#   EJERCICIO 4 - AUTOMÓVIL Y MOTOR (COMPOSICIÓN)
# ══════════════════════════════════════════════════════

print("=" * 60)
print("        SISTEMA DE AUTOMÓVILES - COMPOSICIÓN")
print("=" * 60)

# ─── Creación de 4 objetos Automovil ──────────────────────
# IMPORTANTE: Solo se instancia Automovil, NUNCA Motor directamente.
# El Motor se crea automáticamente dentro del constructor de Automovil.
auto1 = Automovil("Toyota",   "Corolla",   2022, "Blanco",  1.8, "Gasolina", 140)
auto2 = Automovil("Mazda",    "CX-5",      2023, "Rojo",    2.5, "Gasolina", 187)
auto3 = Automovil("Chevrolet","Spark",     2021, "Azul",    1.0, "Gasolina",  69)
auto4 = Automovil("Tesla",    "Model 3",   2024, "Negro",   0.0, "Eléctrico",283)

# ─── Mostrar información inicial ──────────────────────────
print("\n🚗 AUTOMÓVILES REGISTRADOS:")
print("-" * 60)
for auto in [auto1, auto2, auto3, auto4]:
    print(auto.mostrar_info())
    print("-" * 60)

# ─── Probar encender / apagar ─────────────────────────────
print("\n ENCENDIDO Y APAGADO:")
print(auto1.encender())
print(auto1.encender())    # Intentar encender un auto ya encendido
print(auto3.encender())

# ─── Probar acelerar ──────────────────────────────────────
print("\n  ACELERAR:")
print(auto2.acelerar(50))  # Auto apagado, no debe acelerar
print(auto1.acelerar(60))
print(auto1.acelerar(40))
print(auto3.acelerar(30))

# ─── Probar frenar ────────────────────────────────────────
print("\n FRENAR:")
print(auto1.frenar(30))
print(auto1.frenar(200))   # Frena más de lo que lleva → queda en 0
print(auto4.frenar(10))    # Auto que nunca se encendió

# ─── Intentar apagar en movimiento ────────────────────────
print("\n APAGAR:")
print(auto3.apagar())      # Auto3 está en movimiento
print(auto3.frenar(100))   # Primero frenamos
print(auto3.apagar())      # Ahora sí se puede apagar

# ─── Usar setters ─────────────────────────────────────────
print("\n  ACTUALIZACIÓN DE DATOS:")
auto2.set_color("Gris Metalizado")
print(f"Nuevo color de {auto2.get_marca()} {auto2.get_modelo()}: {auto2.get_color()}")

# ─── Acceder a datos del motor mediante el getter ─────────
print("\n  DATOS DEL MOTOR (acceso desde fuera):")
motor_auto1 = auto1.get_motor()
print(f"Motor del {auto1.get_marca()}: "
      f"{motor_auto1.get_cilindrada()}L, "
      f"{motor_auto1.get_potencia()} HP, "
      f"{motor_auto1.get_tipo_combustible()}")

# ─── Validación de error ──────────────────────────────────
print("\n PRUEBA DE VALIDACIÓN:")
try:
    auto_invalido = Automovil("", "X5", 2020, "Negro", 3.0, "Gasolina", 265)
except ValueError as e:
    print(f"Error capturado: {e}")
