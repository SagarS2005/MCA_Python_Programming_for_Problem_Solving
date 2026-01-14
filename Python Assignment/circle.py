from point import Point
import math

class Circle:
    def __init__(self, center, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")

        if not isinstance(center, Point):
            raise TypeError("Center must be a Point object")

        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"
