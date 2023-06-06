from .view import VistaCarrito
from .model import Producto

def test_mostrar_producto_agregado(capsys):
    vista = VistaCarrito()
    producto = Producto("Producto 1", 10)
    vista.mostrar_producto_agregado(producto)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Producto agregado: Producto 1 ($10)"



def test_mostrar_producto_eliminado(capsys):
    vista = VistaCarrito()
    producto = Producto("Producto 1", 10)
    vista.mostrar_producto_eliminado(producto)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Producto eliminado: Producto 1 ($10)"



def test_mostrar_productos(capsys):
    vista = VistaCarrito()
    productos = [
        Producto("Producto 1", 10),
        Producto("Producto 2", 20)
    ]
    vista.mostrar_productos(productos)
    captured = capsys.readouterr()
    expected_output = "Lista de productos:\n"
    expected_output += "- Producto 1 ($10)\n"
    expected_output += "- Producto 2 ($20)\n"
    assert captured.out == expected_output
