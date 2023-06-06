# controlador.py
from model import Producto, Carrito
from view import VistaCarrito


class ControladorCarrito:
    def __init__(self):
        self.carrito = Carrito()
        self.vista = VistaCarrito()

    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.carrito.agregar_producto(producto)
        self.vista.mostrar_producto_agregado(producto)
    
    def eliminar_producto(self, nombre):
        producto = self.carrito.eliminar_producto(nombre)
        if producto:
            self.vista.mostrar_producto_eliminado(producto)
            return True
        else:
            return False

    
    def mostrar_productos(self):
        productos = self.carrito.obtener_productos()
        self.vista.mostrar_productos(productos)
