class Curso:
    """
    Clase que representa un curso universitario.
    Un curso puede tener varios estudiantes matriculados (asociación muchos a muchos).
    """

    def __init__(self, nombre_curso: str, codigo_curso: str, creditos: int):
        if nombre_curso.strip() == "":
            raise ValueError("El nombre del curso no puede estar vacío.")
        if codigo_curso.strip() == "":
            raise ValueError("El código del curso no puede estar vacío.")
        if creditos <= 0:
            raise ValueError("Los créditos deben ser mayores a 0.")

        self.__nombre_curso  = nombre_curso
        self.__codigo_curso  = codigo_curso
        self.__creditos      = creditos
        self.__estudiantes   = []   # Lista OBJ studens =(asociación)

    # ─────────────── GETTERS ───────────────
    def get_nombre_curso(self) -> str:
        return self.__nombre_curso

    def get_codigo_curso(self) -> str:
        return self.__codigo_curso

    def get_creditos(self) -> int:
        return self.__creditos

    def get_estudiantes(self) -> list:
        return list(self.__estudiantes)   # Retorna copia para proteger la lista

    # ─────────────── SETTERS ───────────────
    def set_nombre_curso(self, nombre: str):
        if nombre.strip() == "":
            raise ValueError("El nombre del curso no puede estar vacío.")
        self.__nombre_curso = nombre

    def set_codigo_curso(self, codigo: str):
        if codigo.strip() == "":
            raise ValueError("El código del curso no puede estar vacío.")
        self.__codigo_curso = codigo

    def set_creditos(self, creditos: int):
        if creditos <= 0:
            raise ValueError("Los créditos deben ser mayores a 0.")
        self.__creditos = creditos

    # ─────────────── MÉTODOS DE NEGOCIO ───────────────
    def agregar_estudiante(self, estudiante) -> str:
        """
        Agrega un estudiante al curso si no está ya inscrito.
        Recibe un objeto de tipo Estudiante.
        """
        for e in self.__estudiantes:
            if e.get_codigo_estudiantil() == estudiante.get_codigo_estudiantil():
                return (f"⚠️  {estudiante.get_nombre()} ya está inscrito en "
                        f"'{self.__nombre_curso}'.")
        self.__estudiantes.append(estudiante)
        return (f"✅ {estudiante.get_nombre()} agregado al curso "
                f"'{self.__nombre_curso}'.")

    def mostrar_estudiantes(self) -> str:
        """Muestra todos los estudiantes inscritos en el curso."""
        if not self.__estudiantes:
            return f"📭 El curso '{self.__nombre_curso}' no tiene estudiantes inscritos."
        lineas = [f"📋 Estudiantes en '{self.__nombre_curso}' [{self.__codigo_curso}]:"]
        for i, est in enumerate(self.__estudiantes, 1):
            lineas.append(f"   {i}. {est.get_nombre()} "
                          f"- {est.get_carrera()} "
                          f"({est.get_codigo_estudiantil()})")
        return "\n".join(lineas)

    def mostrar_info(self) -> str:
        """Muestra la información básica del curso."""
        return (
            f"📘 Curso:       {self.__nombre_curso}\n"
            f"   Código:      {self.__codigo_curso}\n"
            f"   Créditos:    {self.__creditos}\n"
            f"   Inscritos:   {len(self.__estudiantes)} estudiante(s)"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
