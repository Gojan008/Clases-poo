from producto import Producto

class ItemPedido:
    def __init__(self, producto, cantidad, precio_unitario):
        self.__producto = producto
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_precio_unitario(self):
        return self.__precio_unitario

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio_unitario(self, precio):
        self.__precio_unitario = precio

    def calcular_subtotal(self):
        return self.__cantidad * self.__precio_unitario

    def mostrar_info(self):
        print("  Producto:", self.__producto.get_nombre())
        print("  Cantidad:", self.__cantidad)
        print("  Precio unitario:", self.__precio_unitario)
        print("  Subtotal:", self.calcular_subtotal())
