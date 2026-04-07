from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, identificacion, nombre, apellido, correo, carrera):
        super().__init__(identificacion, nombre, apellido, correo)
        self.__carrera = carrera
        self.__limite_libros = 3

    # --- Getters ---
    def get_carrera(self):
        return self.__carrera

    def get_limite_libros(self):
        return self.__limite_libros

    # --- Setters ---
    def set_carrera(self, carrera):
        self.__carrera = carrera

    def set_limite_libros(self, limite):
        self.__limite_libros = limite

    # --- Métodos ---
    def prestar_libro(self, libro):
        if len(self.get_libros_prestados()) < self.__limite_libros:
            self.get_libros_prestados().append(libro)
            return f"{self.get_nombre()} ha prestado el libro: {libro}"
        else:
            return f"{self.get_nombre()} ha alcanzado el límite de libros prestados."

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}\nCarrera: {self.__carrera}\nLímite de libros: {self.__limite_libros}"
