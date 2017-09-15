import unittest
from average import average
from mode import mode
from gcd import gcd

class TestCustomFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

    def test_mode(self):
        self.assertEqual(mode([20, 30, 70, 20]), 20)
        with self.assertRaises(TypeError):
            average(20, 30, 70, 20)

    def test_gcd(self):
        self.assertEqual(gcd(12, 16), 4)
        with self.assertRaises(TypeError):
            gcd(12)

unittest.main()
