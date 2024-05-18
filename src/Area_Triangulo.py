import math

class AreaTriangulo:
    def area(self, a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))