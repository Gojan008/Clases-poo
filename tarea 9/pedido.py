from item_pedido import ItemPedido

class Pedido:
    def __init__(self, cliente, fecha):
        self._cliente = cliente
        self._fecha = fecha
        self._items = []

    def get_cliente(self):
        return self._cliente

    def get_fecha(self):
        return self._fecha

    def get_items(self):
        return self._items

    def set_fecha(self, fecha):
        self._fecha = fecha

    def agregar_item(self, item):
        self._items.append(item)
        print("Item agregado:", item.get_producto().get_nombre())

    def calcular_total(self):
        total = 0
        for item in self._items:
            total += item.calcular_subtotal()
        return total

    def mostrar_info(self):
        print("Pedido de:", self._cliente.get_nombre())
        print("Fecha:", self._fecha)
        print("Items:")
        for item in self._items:
            item.mostrar_info()
            print("  ---")
        print("Total:", self.calcular_total())
