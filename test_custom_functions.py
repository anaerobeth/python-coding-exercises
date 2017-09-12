import unittest
from functions import custom_functions as cf

class TestCustomFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(cf.average([20, 30, 70]), 40.0)
        with self.assertRaises(ZeroDivisionError):
            cf.average([])
        with self.assertRaises(TypeError):
            cf.average(20, 30, 70)

    def test_mode(self):
        self.assertEqual(cf.mode([20, 30, 70, 20]), 20)
        with self.assertRaises(TypeError):
            cf.mode(20, 30, 70, 20)

    def test_gcd(self):
        self.assertEqual(cf.gcd(12, 16), 4)
        with self.assertRaises(TypeError):
            cf.gcd(12)

unittest.main()
