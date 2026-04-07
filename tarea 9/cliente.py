class Cliente:
    def __init__(self, nombre, email, telefono):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def mostrar_info(self):
        print("Cliente:", self.__nombre)
        print("Email:", self.__email)
        print("Telefono:", self.__telefono)
