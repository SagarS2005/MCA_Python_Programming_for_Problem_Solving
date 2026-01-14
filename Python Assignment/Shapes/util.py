from .circle import Circle
from .rectangle import Rectangle

def demo():
    c = Circle(3)
    r = Rectangle(2, 5)

    print("Circle area:", c.area())
    print("Rectangle area:", r.area())
