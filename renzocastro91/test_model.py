# test_modelo.py

from renzocastro91.model import Carrito, Producto

def test_agregar_producto():
    carrito = Carrito()
    producto = Producto("Producto 1", 10)
    carrito.agregar_producto(producto)
    assert len(carrito.obtener_productos()) == 1

def test_eliminar_producto():
    carrito = Carrito()
    producto = Producto("Producto 1", 10)
    carrito.agregar_producto(producto)
    carrito.eliminar_producto("Producto 1")
    assert len(carrito.obtener_productos()) == 0
    assert carrito.eliminar_producto("Producto 1") is None

def test_obtener_total():
    carrito = Carrito()
    producto1 = Producto("Producto 1", 10)
    producto2 = Producto("Producto 2", 20)
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    assert carrito.obtener_total() == 30
