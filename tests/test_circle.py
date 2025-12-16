import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(1), math.pi, places=10)
        self.assertAlmostEqual(area(5), 25 * math.pi, places=10)

    def test_area_large_radius(self):
        self.assertAlmostEqual(area(1e6), math.pi * 1e12, places=5)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=10)
        self.assertAlmostEqual(perimeter(3), 6 * math.pi, places=10)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(perimeter(1e5), 2 * math.pi * 1e5, places=5)