class Motor:
    """
    Clase que representa el motor de un automóvil.
    En composición, el Motor NO puede existir sin el Automóvil.
    Por eso esta clase NO se instancia directamente desde el main,
    sino que es creada DENTRO del constructor del Automóvil.
    """

    def __init__(self, cilindrada: float, tipo_combustible: str, potencia: int):
        if cilindrada < 0:
            raise ValueError("La cilindrada no puede ser negativa.")  # 0 es válido para eléctricos
        if tipo_combustible.strip() == "":
            raise ValueError("El tipo de combustible no puede estar vacío.")
        if potencia <= 0:
            raise ValueError("La potencia debe ser mayor a 0.")

        self.__cilindrada       = cilindrada        # En litros, ej: 2.0
        self.__tipo_combustible = tipo_combustible  # Gasolina, Diesel, Eléctrico
        self.__potencia         = potencia          # En caballos de fuerza (HP)
        self.__encendido        = False             # El motor inicia apagado

    # ─────────────── GETTERS ───────────────
    def get_cilindrada(self) -> float:
        return self.__cilindrada

    def get_tipo_combustible(self) -> str:
        return self.__tipo_combustible

    def get_potencia(self) -> int:
        return self.__potencia

    def get_encendido(self) -> bool:
        return self.__encendido

    # ─────────────── SETTERS ───────────────
    def set_cilindrada(self, cilindrada: float):
        if cilindrada <= 0:
            raise ValueError("La cilindrada debe ser mayor a 0.")
        self.__cilindrada = cilindrada

    def set_tipo_combustible(self, tipo: str):
        if tipo.strip() == "":
            raise ValueError("El tipo de combustible no puede estar vacío.")
        self.__tipo_combustible = tipo

    def set_potencia(self, potencia: int):
        if potencia <= 0:
            raise ValueError("La potencia debe ser mayor a 0.")
        self.__potencia = potencia

    # ─────────────── MÉTODOS DE NEGOCIO ───────────────
    def encender(self) -> str:
        if self.__encendido:
            return "  El motor ya está encendido."
        self.__encendido = True
        return "🔑 Motor encendido."

    def apagar(self) -> str:
        if not self.__encendido:
            return "  El motor ya está apagado."
        self.__encendido = False
        return " Motor apagado."

    def mostrar_info(self) -> str:
        estado = "Encendido " if self.__encendido else "Apagado "
        return (
            f"     Motor:\n"
            f"      Cilindrada:        {self.__cilindrada} L\n"
            f"      Tipo combustible:  {self.__tipo_combustible}\n"
            f"      Potencia:          {self.__potencia} HP\n"
            f"      Estado:            {estado}"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
