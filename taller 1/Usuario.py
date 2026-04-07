class Usuario:
    def __init__(self, identificacion, nombre, apellido, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__libros_prestados = []

    # --- Getters ---
    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_correo(self):
        return self.__correo

    def get_libros_prestados(self):
        return self.__libros_prestados

    # --- Setters ---
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_correo(self, correo):
        self.__correo = correo

    # --- Métodos ---
    def __str__(self):
        return (f"{self.__nombre} {self.__apellido}\n"
                f"ID: {self.__identificacion}\n"
                f"Correo: {self.__correo}\n"
                f"Libros prestados: {len(self.__libros_prestados)}")

    def mostrar_informacion(self):
        return str(self)

    def anexar_libro(self, libro):
        self.__libros_prestados.append(libro)
        return f"Libro '{libro}' agregado a los libros prestados de {self.__nombre}"

    def quitar_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)
            return f"Libro '{libro}' removido de los libros prestados de {self.__nombre}"
        else:
            return f"El libro '{libro}' no se encuentra en los libros prestados de {self.__nombre}"

    def quitar_todos_libros(self):
        self.__libros_prestados.clear()
        return f"Todos los libros prestados de {self.__nombre} han sido removidos"
