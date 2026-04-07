from datetime import date

class CuentaBancaria:
    """
    Clase que representa una cuenta de ahorro bancaria.
    Aplica encapsulación fuerte: todos los atributos son privados.
    Las operaciones incluyen validaciones para proteger la integridad del saldo.
    """

    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float, fecha_apertura: date):
        # Validaciones en el constructor
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        if numero_cuenta.strip() == "":
            raise ValueError("El número de cuenta no puede estar vacío.")
        if titular.strip() == "":
            raise ValueError("El nombre del titular no puede estar vacío.")

        # Atributos privados
        self.__numero_cuenta  = numero_cuenta
        self.__titular        = titular
        self.__saldo          = saldo_inicial
        self.__fecha_apertura = fecha_apertura

    # ─────────────── GETTERS ───────────────
    def get_numero_cuenta(self) -> str:
        return self.__numero_cuenta

    def get_titular(self) -> str:
        return self.__titular

    def get_saldo(self) -> float:
        return self.__saldo

    def get_fecha_apertura(self) -> date:
        return self.__fecha_apertura

    # ─────────────── SETTERS ───────────────
    def set_titular(self, titular: str):
        if titular.strip() == "":
            raise ValueError("El nombre del titular no puede estar vacío.")
        self.__titular = titular

    def set_numero_cuenta(self, numero_cuenta: str):
        if numero_cuenta.strip() == "":
            raise ValueError("El número de cuenta no puede estar vacío.")
        self.__numero_cuenta = numero_cuenta

    def set_fecha_apertura(self, fecha: date):
        if not isinstance(fecha, date):
            raise TypeError("La fecha debe ser un objeto de tipo date.")
        self.__fecha_apertura = fecha

    # Nota: el saldo NO tiene setter público — solo se modifica con la plata

    # ─────────────── MÉTODOS DE NEGOCIO ───────────────
    def depositar(self, monto: float) -> str:
        """
        Deposita un monto positivo en la cuenta.
        Valida que el monto sea mayor a cero.
        """
        if monto <= 0:
            return f"❌ El monto a depositar debe ser mayor a $0. Monto ingresado: ${monto:,.2f}"
        self.__saldo += monto
        return (f" Depósito exitoso de ${monto:,.2f}. "
                f"Nuevo saldo: ${self.__saldo:,.2f}")

    def retirar(self, monto: float) -> str:
        """
        Retira un monto de la cuenta si hay saldo suficiente.
        Valida que el monto sea positivo y que haya saldo disponible.
        """
        if monto <= 0:
            return f" El monto a retirar debe ser mayor a $0. Monto ingresado: ${monto:,.2f}"
        if monto > self.__saldo:
            return (f" Saldo insuficiente. Saldo disponible: ${self.__saldo:,.2f} | "
                    f"Monto solicitado: ${monto:,.2f}")
        self.__saldo -= monto
        return (f" Retiro exitoso de ${monto:,.2f}. "
                f"Nuevo saldo: ${self.__saldo:,.2f}")

    def consultar_saldo(self) -> str:
        """Muestra el saldo actual de la cuenta."""
        return f" Saldo actual de la cuenta {self.__numero_cuenta}: ${self.__saldo:,.2f}"

    def mostrar_info(self) -> str:
        """Muestra toda la información de la cuenta."""
        return (
            f" Número de cuenta: {self.__numero_cuenta}\n"
            f"   Titular:         {self.__titular}\n"
            f"   Saldo:           ${self.__saldo:,.2f}\n"
            f"   Fecha apertura:  {self.__fecha_apertura.strftime('%d/%m/%Y')}"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
