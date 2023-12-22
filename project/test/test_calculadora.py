import unittest

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(self.calc.resta(5, 2), 3)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(3, 4), 12)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(8, 4), 2)
        

if __name__ == '__main__':
    unittest.main()
