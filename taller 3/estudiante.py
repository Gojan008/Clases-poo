class Estudiante:
    """
    Clase que representa un estudiante universitario.
    Un estudiante puede estar matriculado en varios cursos (asociación muchos a muchos).
    """

    def __init__(self, nombre: str, codigo_estudiantil: str, carrera: str):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if codigo_estudiantil.strip() == "":
            raise ValueError("El código estudiantil no puede estar vacío.")

        self.__nombre              = nombre
        self.__codigo_estudiantil  = codigo_estudiantil
        self.__carrera             = carrera
        self.__cursos              = []   # Lista de objetos Curso (asociación)

    # ─────────────── GETTERS ───────────────
    def get_nombre(self) -> str:
        return self.__nombre

    def get_codigo_estudiantil(self) -> str:
        return self.__codigo_estudiantil

    def get_carrera(self) -> str:
        return self.__carrera

    def get_cursos(self) -> list:
        return list(self.__cursos)   # Retorna copia para proteger la lista interna

    # ─────────────── SETTERS ───────────────
    def set_nombre(self, nombre: str):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def set_carrera(self, carrera: str):
        if carrera.strip() == "":
            raise ValueError("La carrera no puede estar vacía.")
        self.__carrera = carrera

    def set_codigo_estudiantil(self, codigo: str):
        if codigo.strip() == "":
            raise ValueError("El código estudiantil no puede estar vacío.")
        self.__codigo_estudiantil = codigo

    # ─────────────── MÉTODOS DE NEGOCIO ───────────────
    def matricular_curso(self, curso) -> str:
        """
        Matricula al estudiante en un curso si no está ya matriculado.
        Recibe un objeto de tipo Curso.
        """
        # Verificar si ya está matriculado buscando por código
        for c in self.__cursos:
            if c.get_codigo_curso() == curso.get_codigo_curso():
                return (f"⚠️  {self.__nombre} ya está matriculado en "
                        f"'{curso.get_nombre_curso()}'.")
        self.__cursos.append(curso)
        return (f" {self.__nombre} matriculado exitosamente en "
                f"'{curso.get_nombre_curso()}'.")

    def cancelar_curso(self, codigo_curso: str) -> str:
        """Cancela la matrícula del estudiante en un curso por su código."""
        for c in self.__cursos:
            if c.get_codigo_curso() == codigo_curso:
                self.__cursos.remove(c)
                return (f" Matrícula cancelada: {self.__nombre} salió de "
                        f"'{c.get_nombre_curso()}'.")
        return f" El estudiante {self.__nombre} no está matriculado en el curso {codigo_curso}."

    def mostrar_cursos(self) -> str:
        """Muestra todos los cursos en los que está matriculado el estudiante."""
        if not self.__cursos:
            return f" {self.__nombre} no tiene cursos matriculados."
        lineas = [f" Cursos de {self.__nombre} ({self.__codigo_estudiantil}):"]
        for i, curso in enumerate(self.__cursos, 1):
            lineas.append(f"   {i}. {curso.get_nombre_curso()} "
                          f"[{curso.get_codigo_curso()}] - "
                          f"{curso.get_creditos()} créditos")
        return "\n".join(lineas)

    def mostrar_info(self) -> str:
        """Muestra la información básica del estudiante."""
        return (
            f"🎓 Nombre:    {self.__nombre}\n"
            f"   Código:    {self.__codigo_estudiantil}\n"
            f"   Carrera:   {self.__carrera}\n"
            f"   Cursos:    {len(self.__cursos)} matriculado(s)"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
