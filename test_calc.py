import unittest
import calculator

class TestStringMethods(unittest.TestCase):

    def test_basic_add(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("1+1"), 2)
    def test_basic_subtract(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("10-1"), 9)
    def test_basic_divide(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("4/2"), 2)
    def test_basic_multiply(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("4*2"), 8)
    def test_complex(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("1+4-25+60/25*2"), -15.2)
    def test_complex_not_equal(self):
        Calc = calculator.Calculator()
        self.assertNotEqual(Calc.Evaluate("1+4-25+60/25*2"), -15)
    def test_divide_zero(self):
        Calc = calculator.Calculator()
        self.assertEqual(Calc.Evaluate("100/0"), "Error")

if __name__ == '__main__':
    unittest.main()