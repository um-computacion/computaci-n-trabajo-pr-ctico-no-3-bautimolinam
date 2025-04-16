import unittest
from unittest.mock import patch
from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
unittest()