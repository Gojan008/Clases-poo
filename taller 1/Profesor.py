from Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, identificacion, nombre, apellido, correo, departamento):
        super().__init__(identificacion, nombre, apellido, correo)
        self.__departamento = departamento
        self.__limite_libros = 5

    # --- Getters ---
    def get_departamento(self):
        return self.__departamento

    def get_limite_libros(self):
        return self.__limite_libros

    # --- Setters ---
    def set_departamento(self, departamento):
        self.__departamento = departamento

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
        return f"{info_base}\nDepartamento: {self.__departamento}\nLímite de libros: {self.__limite_libros}"
