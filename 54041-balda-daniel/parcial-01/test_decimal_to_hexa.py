import unittest
from decimal_to_hexadecimal import convert

class TestDecimalToHexadecimal(unittest.TestCase):
    def test_convert_0(self):
        result_convert = convert(0)
        self.assertEqual(result_convert, '0')

    def test_convert_9(self):
        result_convert = convert(9)
        self.assertEqual(result_convert, '9')

    def test_convert_50(self):
        result_convert = convert(50)
        self.assertEqual(result_convert, '32')

    def test_convert_16(self):
        result_convert = convert(16)
        self.assertEqual(result_convert, '10')

    def test_convert_16(self):
        result_convert = convert(10)
        self.assertEqual(result_convert, 'A')

    def test_convert_4095(self):
        result_convert = convert(4095)
        self.assertEqual(result_convert, 'FFF')

    def test_convert_234(self):
        result_convert = convert(234)
        self.assertEqual(result_convert, 'EA')

if __name__ == '__main__':
    unittest.main()