import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_side(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10.5), 110.25)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(7), 28)
        self.assertEqual(perimeter(3.25), 13.0)