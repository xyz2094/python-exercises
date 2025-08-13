class Shape:
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        return f"\nArea of Circle with radius {self.radius}: {area}\n"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        area = self.side * self.side
        return f"\nArea of Square with side {self.side}: {area}\n"
    
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print("-" * 20)
    print(shape.calculate_area())

print("-" * 20)