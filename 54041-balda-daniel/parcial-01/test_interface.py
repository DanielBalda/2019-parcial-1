import unittest
from interface import esnumero

class TestInterface(unittest.TestCase):
    def test_interface_string(self):
        result_esnumero = esnumero('hola')
        self.assertEqual(result_esnumero, 'Debe ingresar un numero entero')

    def test_interface_float(self):
        result_esnumero = esnumero(12.52)
        self.assertEqual(result_esnumero, 'C')

if __name__ == '__main__':
    unittest.main()