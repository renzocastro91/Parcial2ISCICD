import unittest
from unittest.mock import patch
from io import StringIO

import os
import sys

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta al PYTHONPATH
sys.path.append(current_dir)

from controller import ControladorCarrito


class TestControladorCarrito(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorCarrito()

    def test_agregar_producto(self):
        nombre = "Producto 1"
        precio = 10.0
        expected_output = "Producto agregado: Producto 1 - $10.0\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.controlador.agregar_producto(nombre, precio)
            actual_output = fake_stdout.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_eliminar_producto(self):
        nombre = "Producto 1"
        self.controlador.carrito.agregar_producto(self.controlador.carrito)
        expected_output = "Producto eliminado: Producto 1\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.controlador.eliminar_producto(nombre)
            actual_output = fake_stdout.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_mostrar_productos(self):
        expected_output = "Productos en el carrito:\n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.controlador.mostrar_productos()
            actual_output = fake_stdout.getvalue()

        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
