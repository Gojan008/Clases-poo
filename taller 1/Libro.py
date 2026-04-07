class Libro:
    def __init__(self, titulo, autor, anio_publicacion, isbn, disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__isbn = isbn
        self.__disponible = disponible
        self.__veces_prestado = 0
        self.__libros_prestados = {}  

    # --- Getters ---
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio_publicacion(self):
        return self.__anio_publicacion

    def get_isbn(self):
        return self.__isbn

    def get_disponible(self):
        return self.__disponible

    def get_veces_prestado(self):
        return self.__veces_prestado

    def get_libros_prestados(self):
        return self.__libros_prestados

    # --- Setters ---
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_disponible(self, disponible):
        self.__disponible = disponible

    # --- Métodos ---
    def registrar_prestamo(self, nombre_usuario):
        """Registra el préstamo del libro a un usuario en el diccionario."""
        if self.__disponible:
            self.__libros_prestados[nombre_usuario] = self.__titulo
            self.__disponible = False
            self.__veces_prestado += 1
            return f"Libro '{self.__titulo}' prestado a {nombre_usuario}."
        else:
            return f"El libro '{self.__titulo}' no está disponible."

    def devolver_prestamo(self, nombre_usuario):
        """Elimina el registro del préstamo cuando el usuario devuelve el libro."""
        if nombre_usuario in self.__libros_prestados:
            del self.__libros_prestados[nombre_usuario]
            self.__disponible = True
            return f"Libro '{self.__titulo}' devuelto por {nombre_usuario}."
        else:
            return f"{nombre_usuario} no tiene prestado el libro '{self.__titulo}'."

    def mostrar_prestamos(self):
        """Muestra el diccionario de préstamos activos."""
        if self.__libros_prestados:
            print(f"  Préstamos activos de '{self.__titulo}':")
            for usuario, libro in self.__libros_prestados.items():
                print(f"    {usuario} → {libro}")
        else:
            print(f"  '{self.__titulo}' no tiene préstamos activos.")

    def cambiar_disponibilidad(self):
        if self.__disponible:
            self.__disponible = False
            self.__veces_prestado += 1
            return f"El libro '{self.__titulo}' ahora está prestado."
        else:
            self.__disponible = True
            return f"El libro '{self.__titulo}' ahora está disponible."

    def es_popular(self):
        return self.__veces_prestado > 5

    def __str__(self):
        return (f"{self.__titulo} por {self.__autor} ({self.__anio_publicacion}) "
                f"- ISBN: {self.__isbn} - "
                f"{'Disponible' if self.__disponible else 'No Disponible'}")
