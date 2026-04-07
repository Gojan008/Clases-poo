from producto import Producto
from item_pedido import ItemPedido
from cliente import Cliente
from pedido import Pedido

# Paso 1: crear productos
prod1 = Producto("Camiseta", "CAM-001")
prod2 = Producto("Pantalon", "PAN-002")
prod3 = Producto("Zapatos",  "ZAP-003")
prod4 = Producto("Gorra",    "GOR-004")

# Paso 2: crear clientes
cli1 = Cliente("Ana Garcia",    "ana@email.com",   "3001234567")
cli2 = Cliente("Luis Martinez", "luis@email.com",  "3109876543")
cli3 = Cliente("Maria Perez",   "maria@email.com", "3205551234")
cli4 = Cliente("Carlos Lopez",  "carlo@email.com", "3154449988")

# Paso 3: crear pedidos y agregar items (composicion: los items viven dentro del pedido)
print("---------- Pedido 1 ----------")
pedido1 = Pedido(cli1, "2024-03-01")
pedido1.agregar_item(ItemPedido(prod1, 2, 50000))
pedido1.agregar_item(ItemPedido(prod2, 1, 120000))
pedido1.mostrar_info()

print()
print("---------- Pedido 2 ----------")
pedido2 = Pedido(cli2, "2024-03-02")
pedido2.agregar_item(ItemPedido(prod3, 1, 200000))
pedido2.mostrar_info()

print()
print("---------- Pedido 3 ----------")
pedido3 = Pedido(cli3, "2024-03-03")
pedido3.agregar_item(ItemPedido(prod1, 3, 50000))
pedido3.agregar_item(ItemPedido(prod4, 2, 30000))
pedido3.mostrar_info()

print()
print("---------- Pedido 4 ----------")
pedido4 = Pedido(cli4, "2024-03-04")
pedido4.agregar_item(ItemPedido(prod2, 2, 120000))
pedido4.agregar_item(ItemPedido(prod3, 1, 200000))
pedido4.agregar_item(ItemPedido(prod4, 1, 30000))
pedido4.mostrar_info()

# Setters
print()
print("Actualizando datos:")
cli1.set_telefono("3009998877")
print("Nuevo telefono de Ana:", cli1.get_telefono())
