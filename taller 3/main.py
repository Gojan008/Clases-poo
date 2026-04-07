from estudiante import Estudiante
from curso import Curso

#   EJERCICIO 3 - SISTEMA DE ESTUDIANTES Y CURSOS

print("=" * 60)
print("       SISTEMA UNIVERSITARIO - MATRÍCULAS")
print("=" * 60)

# ─── Paso 1: Crear los cursos primero ─────────────────────
# (Lógica de negocio: los cursos deben existir antes de matricular)
print(" CURSOS DISPONIBLES:")
print("-" * 60)

curso1 = Curso("Programación Orientada a Objetos", "POO-101", 3)
curso2 = Curso("Cálculo Diferencial",              "MAT-201", 4)
curso3 = Curso("Base de Datos I",                  "BDD-301", 3)
curso4 = Curso("Inglés Técnico",                   "ING-101", 2)

for curso in [curso1, curso2, curso3, curso4]:
    print(curso.mostrar_info())
    print("-" * 60)

# ─── Paso 2: Crear los estudiantes ────────────────────────
print(" ESTUDIANTES REGISTRADOS:")
print("-" * 60)

est1 = Estudiante("Ana García",      "EST-2024-001", "Ingeniería de Sistemas")
est2 = Estudiante("Luis Martínez",   "EST-2024-002", "Ingeniería de Sistemas")
est3 = Estudiante("María Rodríguez", "EST-2024-003", "Matemáticas")
est4 = Estudiante("Carlos Pérez",    "EST-2024-004", "Administración")

for est in [est1, est2, est3, est4]:
    print(est.mostrar_info())
    print("-" * 60)


print("\n🔗 PROCESO DE MATRÍCULA:")

# Ana se matricula 3 cursos
print(est1.matricular_curso(curso1))
print(curso1.agregar_estudiante(est1))
print(est1.matricular_curso(curso2))
print(curso2.agregar_estudiante(est1))
print(est1.matricular_curso(curso4))
print(curso4.agregar_estudiante(est1))

print()

# Luis se matricula 2 cursos
print(est2.matricular_curso(curso1))
print(curso1.agregar_estudiante(est2))
print(est2.matricular_curso(curso3))
print(curso3.agregar_estudiante(est2))

print()

# María se matricula en 2 cursos
print(est3.matricular_curso(curso2))
print(curso2.agregar_estudiante(est3))
print(est3.matricular_curso(curso3))
print(curso3.agregar_estudiante(est3))

print()

# Carlos se matricula 1 curso
print(est4.matricular_curso(curso4))
print(curso4.agregar_estudiante(est4))

# ─── Probar duplicado ───────────────
print(" INTENTO DE MATRÍCULA DUPLICADA:")
print(est1.matricular_curso(curso1))   # Ana ya está en POO-101

# ─── Ver cursos por estudiante ──────
print(" CURSOS POR ESTUDIANTE:")
print("-" * 60)
for est in [est1, est2, est3, est4]:
    print(est.mostrar_cursos())
    print("-" * 60)

# ─── Ver estudiantes por curso ──────
print(" ESTUDIANTES POR CURSO:")
print("-" * 60)
for curso in [curso1, curso2, curso3, curso4]:
    print(curso.mostrar_estudiantes())
    print("-" * 60)

# ─── Cancelar una matrícula ───────────────────────────────
print(" CANCELACIÓN DE MATRÍCULA:")
print(est2.cancelar_curso("POO-101"))
print(est3.cancelar_curso("MAT-999"))  # Curso que no existe para este estudiante

print(" Cursos de Luis después de cancelar:")
print(est2.mostrar_cursos())
