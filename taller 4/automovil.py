from motor import Motor

class Automovil:
    """
    Clase que representa un automóvil.
    COMPOSICIÓN: El Automóvil CREA su propio Motor en el constructor.
    Si el Automóvil deja de existir, el Motor también desaparece.
    El Motor no puede existir de forma independiente fuera del Automóvil.
    """

    def __init__(self, marca: str, modelo: str, anio: int, color: str,
                 cilindrada: float, tipo_combustible: str, potencia: int):
        # Validaciones del automóvil
        if marca.strip() == "":
            raise ValueError("La marca no puede estar vacía.")
        if modelo.strip() == "":
            raise ValueError("El modelo no puede estar vacío.")
        if anio < 1886:
            raise ValueError("El año no puede ser anterior a 1886 (primer auto de la historia).")

        # Atributos propios del automóvil
        self.__marca    = marca
        self.__modelo   = modelo
        self.__anio     = anio
        self.__color    = color
        self.__velocidad_actual = 0  # km/h, inicia en 0

        # COMPOSICIÓN: El Motor se crea AQUÍ DENTRO, no se recibe como objeto
        # El Automóvil es dueño total del Motor
        self.__motor = Motor(cilindrada, tipo_combustible, potencia)

    # ─────────────── GETTERS ───────────────
    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> str:
        return self.__modelo

    def get_anio(self) -> int:
        return self.__anio

    def get_color(self) -> str:
        return self.__color

    def get_velocidad_actual(self) -> int:
        return self.__velocidad_actual

    def get_motor(self) -> Motor:
        return self.__motor

    # ─────────────── SETTERS ───────────────
    def set_marca(self, marca: str):
        if marca.strip() == "":
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = marca

    def set_modelo(self, modelo: str):
        if modelo.strip() == "":
            raise ValueError("El modelo no puede estar vacío.")
        self.__modelo = modelo

    def set_color(self, color: str):
        self.__color = color

    def set_anio(self, anio: int):
        if anio < 1886:
            raise ValueError("El año no puede ser anterior a 1886.")
        self.__anio = anio

    # ─────────────── MÉTODOS DE NEGOCIO ───────────────
    def encender(self) -> str:
        """Enciende el automóvil (lo que activa el motor internamente)."""
        resultado = self.__motor.encender()
        if self.__motor.get_encendido():
            return f"🚗 {self.__marca} {self.__modelo} encendido. {resultado}"
        return resultado

    def apagar(self) -> str:
        """Apaga el automóvil. Solo si está detenido."""
        if self.__velocidad_actual > 0:
            return (f" No puedes apagar el auto en movimiento. "
                    f"Velocidad actual: {self.__velocidad_actual} km/h")
        resultado = self.__motor.apagar()
        if not self.__motor.get_encendido():
            return f"🚗 {self.__marca} {self.__modelo} apagado. {resultado}"
        return resultado

    def acelerar(self, incremento: int) -> str:
        """Aumenta la velocidad si el motor está encendido."""
        if not self.__motor.get_encendido():
            return " No puedes acelerar. El auto está apagado."
        if incremento <= 0:
            return " El incremento de velocidad debe ser mayor a 0."
        self.__velocidad_actual += incremento
        return (f" Acelerando... Velocidad actual: "
                f"{self.__velocidad_actual} km/h")

    def frenar(self, decremento: int) -> str:
        """Reduce la velocidad del automóvil."""
        if self.__velocidad_actual == 0:
            return "  El auto ya está detenido."
        if decremento <= 0:
            return " El decremento debe ser mayor a 0."
        self.__velocidad_actual = max(0, self.__velocidad_actual - decremento)
        return (f" Frenando... Velocidad actual: "
                f"{self.__velocidad_actual} km/h")

    def mostrar_info(self) -> str:
        """Muestra toda la información del automóvil y su motor."""
        return (
            f" Automóvil:\n"
            f"   Marca:     {self.__marca}\n"
            f"   Modelo:    {self.__modelo}\n"
            f"   Año:       {self.__anio}\n"
            f"   Color:     {self.__color}\n"
            f"   Velocidad: {self.__velocidad_actual} km/h\n"
            f"{self.__motor.mostrar_info()}"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
