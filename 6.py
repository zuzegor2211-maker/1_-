import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.x = center_x
        self.y = center_y
        self.radius = radius

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, factor):
        self.radius *= factor

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(center=({self.x}, {self.y}), radius={self.radius})"


class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, factor):
        self.side *= factor

    def area(self):
        return self.side ** 2

    def __repr__(self):
        return f"Square(corner=({self.x}, {self.y}), side={self.side})"


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, factor):
        self.width *= factor
        self.height *= factor

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle(corner=({self.x}, {self.y}), width={self.width}, height={self.height})"


# Демонстрация
if __name__ == "__main__":
    circle = Circle(0, 0, 5)
    square = Square(10, 10, 4)
    rect = Rectangle(1, 1, 6, 3)

    print("До изменений:")
    print(circle, "Площадь:", circle.area())
    print(square, "Площадь:", square.area())
    print(rect, "Площадь:", rect.area())

    circle.move(2, -1)
    circle.resize(2)
    square.move(-5, 0)
    square.resize(1.5)
    rect.move(3, 3)
    rect.resize(0.5)

    print("\nПосле изменений:")
    print(circle, "Площадь:", circle.area())
    print(square, "Площадь:", square.area())
    print(rect, "Площадь:", rect.area())
