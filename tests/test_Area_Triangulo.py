import unittest
from src.Area_Triangulo import AreaTriangulo

class TestAreaTriangulo(unittest.TestCase):
    def test_area1(self):
        triangle = AreaTriangulo()
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6)
        self.assertAlmostEqual(triangle.area(6, 8, 10), 24)
        self.assertAlmostEqual(triangle.area(7, 24, 25), 84)
    def test_area_enumerado(self):
        triangle = AreaTriangulo()
        cases = [
            (3, 4, 5, 6),
            (6, 8, 10, 24),
            (7, 24, 25, 84),
            (13, 14, 15, 84),
            (5, 12, 13, 30),
        ]

        for i, (a, b, c, expected) in enumerate(cases, 1):
            with self.subTest(case=i):
                result = triangle.area(a, b, c)
                self.assertAlmostEqual(result, expected, places=7, msg=f"Failed en el caso {i}: area({a}, {b}, {c}) = {result}, expected {expected}")

if __name__ == '__main__':
    unittest.main()
