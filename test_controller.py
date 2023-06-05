# test_controlador.py

from controller import ControladorCarrito
from model import Producto

def test_agregar_producto(capsys):
    controlador = ControladorCarrito()
    controlador.agregar_producto("Producto 1", 10)
    captured = capsys.readouterr()
    assert captured.out == "Producto agregado: Producto 1 ($10)\n\n"


def test_eliminar_producto(capsys):
    controlador = ControladorCarrito()
    controlador.agregar_producto("Producto 1", 10)
    controlador.eliminar_producto("Producto 1")
    captured = capsys.readouterr()
    assert captured.out == "Producto eliminado: Producto 1 ($10)\n"

def test_mostrar_productos(capsys):
    controlador = ControladorCarrito()
    controlador.agregar_producto("Producto 1", 10)
    controlador.agregar_producto("Producto 2", 20)
    controlador.mostrar_productos()
    captured = capsys.readouterr()
    expected_output = "Lista de productos:\n"
    expected_output += "- Producto 1 ($10)\n"
    expected_output += "- Producto 2 ($20)\n"
    assert captured.out == expected_output
