# Importamos las clases desde sus archivos para poder usarlas aqui
from Libro import Libro
from Estudiante import Estudiante
from Profesor import Profesor


# Creamos 5 objetos Libro y los guardamos en una lista
libro1 = Libro("Cien anos de soledad",      "Gabriel Garcia Marquez",   1967, "ISBN-001", True)
libro2 = Libro("El Principito",             "Antoine de Saint-Exupery", 1943, "ISBN-002", True)
libro3 = Libro("Como entender a una mujer", "Pedro Picapiedras",        1599, "ISBN-003", True)
libro4 = Libro("Don Quijote de la Mancha",  "Miguel de Cervantes",      1605, "ISBN-004", True)
libro5 = Libro("Harry Potter",              "J.K. Rowling",             1997, "ISBN-005", True)

# Lista con todos los libros instanciados
libros = [libro1, libro2, libro3, libro4, libro5]

print("=" * 60)
print("CATALOGO DE LIBROS")
print("=" * 60)
# print(libro) llama al metodo __str__ de la clase Libro
for libro in libros:
    print(libro)


# Prestamos el libro 6 veces para que es_popular() retorne True
print("\n" + "=" * 60)
print(f"HACIENDO POPULAR: {libro1.get_titulo()}")
print("=" * 60)
for _ in range(6):
    libro1.cambiar_disponibilidad()  # prestamo
    libro1.cambiar_disponibilidad()  # devolucion

print(f"Veces prestado: {libro1.get_veces_prestado()}")
print(f"Es popular: {libro1.es_popular()}")


# Creamos 6 objetos Estudiante
# El constructor llama a super().__init__ para heredar los atributos de Usuario
est1 = Estudiante(1001, "Ana",       "Garcia",    "ana@mail.com",    "Ingenieria")
est2 = Estudiante(1002, "Luis",      "Martinez",  "luis@mail.com",   "Medicina")
est3 = Estudiante(1003, "Sofia",     "Rodriguez", "sofia@mail.com",  "Derecho")
est4 = Estudiante(1004, "Carlos",    "Lopez",     "carlos@mail.com", "Arquitectura")
est5 = Estudiante(1005, "Valentina", "Perez",     "vale@mail.com",   "Psicologia")
est6 = Estudiante(1006, "Andres",    "Torres",    "andres@mail.com", "Economia")

estudiantes = [est1, est2, est3, est4, est5, est6]


# Creamos 6 objetos Profesor
# Igual que Estudiante pero con departamento y limite de 5 libros
prof1 = Profesor(2001, "Marta",    "Sanchez",  "marta@uni.com",    "Ciencias")
prof2 = Profesor(2002, "Jorge",    "Ramirez",  "jorge@uni.com",    "Humanidades")
prof3 = Profesor(2003, "Elena",    "Castro",   "elena@uni.com",    "Ingenieria")
prof4 = Profesor(2004, "Ricardo",  "Morales",  "ricardo@uni.com",  "Medicina")
prof5 = Profesor(2005, "Patricia", "Vargas",   "patricia@uni.com", "Derecho")
prof6 = Profesor(2006, "Hernan",   "Diaz",     "hernan@uni.com",   "Matematicas")

profesores = [prof1, prof2, prof3, prof4, prof5, prof6]


# Asignamos 3 libros a cada estudiante usando prestar_libro()
# que verifica el limite antes de agregar el libro a la lista
asignaciones_estudiantes = [
    (est1, [libro1, libro2, libro3]),
    (est2, [libro2, libro3, libro4]),
    (est3, [libro1, libro3, libro5]),
    (est4, [libro2, libro4, libro5]),
    (est5, [libro1, libro2, libro5]),
    (est6, [libro3, libro4, libro5]),
]

for est, libros_asignados in asignaciones_estudiantes:
    for libro in libros_asignados:
        est.prestar_libro(libro)
        # Registramos el prestamo en el diccionario del libro {usuario: titulo}
        libro.get_libros_prestados()[est.get_nombre()] = libro.get_titulo()


# Asignamos 3 libros a cada profesor con la misma logica
asignaciones_profesores = [
    (prof1, [libro1, libro2, libro3]),
    (prof2, [libro2, libro3, libro4]),
    (prof3, [libro1, libro4, libro5]),
    (prof4, [libro2, libro3, libro5]),
    (prof5, [libro1, libro3, libro4]),
    (prof6, [libro2, libro4, libro5]),
]

for prof, libros_asignados in asignaciones_profesores:
    for libro in libros_asignados:
        prof.prestar_libro(libro)
        libro.get_libros_prestados()[prof.get_nombre()] = libro.get_titulo()


# Mostramos cada estudiante con sus libros
# mostrar_informacion() esta sobreescrito en Estudiante (polimorfismo)
print("\n" + "=" * 60)
print(f"TOTAL DE ESTUDIANTES: {len(estudiantes)}")
print("=" * 60)
for est in estudiantes:
    print(f"\n{est.mostrar_informacion()}")
    print("  Libros asignados:")
    for libro in est.get_libros_prestados():
        print(f"    - {libro.get_titulo()}")


# Mostramos cada profesor con sus libros
print("\n" + "=" * 60)
print(f"TOTAL DE PROFESORES: {len(profesores)}")
print("=" * 60)
for prof in profesores:
    print(f"\n{prof.mostrar_informacion()}")
    print("  Libros asignados:")
    for libro in prof.get_libros_prestados():
        print(f"    - {libro.get_titulo()}")


# Resumen final con el total de libros prestados
print("\n" + "=" * 60)
print("RESUMEN FINAL DE LIBROS PRESTADOS")
print("=" * 60)

total_libros_estudiantes = sum(len(est.get_libros_prestados()) for est in estudiantes)
total_libros_profesores  = sum(len(prof.get_libros_prestados()) for prof in profesores)
total_general            = total_libros_estudiantes + total_libros_profesores

print("\nLIBROS POR ESTUDIANTE")
for est in estudiantes:
    cantidad = len(est.get_libros_prestados())
    print(f"  {est.get_nombre()} {est.get_apellido():<12} -> {cantidad} libro(s)")

print(f"\n  Total libros prestados a estudiantes: {total_libros_estudiantes}")

print("\nLIBROS POR PROFESOR")
for prof in profesores:
    cantidad = len(prof.get_libros_prestados())
    print(f"  {prof.get_nombre()} {prof.get_apellido():<12} -> {cantidad} libro(s)")

print(f"\n  Total libros prestados a profesores: {total_libros_profesores}")

print("\n" + "=" * 60)
print(f"  Total general de libros prestados: {total_general}")
print(f"  Total de usuarios: {len(estudiantes) + len(profesores)}")
print(f"  Estudiantes: {len(estudiantes)}  |  Profesores: {len(profesores)}")
print("=" * 60)
