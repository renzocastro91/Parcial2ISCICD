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

    def test_mostrar_productos(self):
        expected_output = "Lista de productos:/n"

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.controlador.mostrar_productos()
            actual_output = fake_stdout.getvalue()

        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
