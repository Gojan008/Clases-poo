from datetime import date
from cuenta_bancaria import CuentaBancaria

#   EJERCICIO 2 - SISTEMA DE CUENTA BANCARIA

print("=" * 60)
print("        SISTEMA DE GESTIÓN BANCARIA")
print("=" * 60)

# ─── Creación de 4 objetos CuentaBancaria ─────────────────
cuenta1 = CuentaBancaria("COL-001-2024", "Ana García",      1_500_000.00, date(2022, 3, 15))
cuenta2 = CuentaBancaria("COL-002-2023", "Luis Martínez",   3_200_000.00, date(2021, 7, 1))
cuenta3 = CuentaBancaria("COL-003-2025", "María Rodríguez",   500_000.00, date(2025, 1, 20))
cuenta4 = CuentaBancaria("COL-004-2020", "Carlos Pérez",    8_750_000.00, date(2020, 11, 5))

# ─── Mostrar información inicial ────
print(" CUENTAS REGISTRADAS:")
print("-" * 60)
for cuenta in [cuenta1, cuenta2, cuenta3, cuenta4]:
    print(cuenta.mostrar_info())
    print("-" * 60)

# ─── Consultar saldo ──────────────────────────────────────
print(" CONSULTA DE SALDOS:")
print(cuenta1.consultar_saldo())
print(cuenta4.consultar_saldo())

# ─── Operaciones de depósito ──────────────────────────────
print(" OPERACIONES DE DEPÓSITO:")
print(cuenta1.depositar(500_000))     # Depósito exitoso
print(cuenta3.depositar(200_000))     # Depósito exitoso
print(cuenta2.depositar(-100_000))    # Monto inválido (negativo)
print(cuenta2.depositar(0))           # Monto inválido (cero)

# ─── Operaciones de retiro ────────────────────────────────
print(" OPERACIONES DE RETIRO:")
print(cuenta1.retirar(300_000))       # Retiro exitoso
print(cuenta4.retirar(9_000_000))     # Saldo insuficiente
print(cuenta3.retirar(0))             # Monto inválido
print(cuenta2.retirar(1_000_000))     # Retiro exitoso

# ─── Uso de setters ───────────────────────────────────────
print(" ACTUALIZACIÓN DE DATOS:")
cuenta3.set_titular("María Rodríguez de López")
print(f"Titular actualizado: {cuenta3.get_titular()}")

# ─── Probar validación del constructor ────────────────────
print(" PRUEBA DE VALIDACIONES:")
try:
    cuenta_invalida = CuentaBancaria("", "Juan", 1000, date.today())
except ValueError as e:
    print(f"Error capturado: {e}")

try:
    cuenta_invalida2 = CuentaBancaria("COL-999", "Pedro", -500, date.today())
except ValueError as e:
    print(f"Error capturado: {e}")

# ─── Estado final de todas las cuentas ───────────────────
print(" ESTADO FINAL DE LAS CUENTAS:")
print("-" * 60)
for cuenta in [cuenta1, cuenta2, cuenta3, cuenta4]:
    print(cuenta.mostrar_info())
    print("-" * 60)
