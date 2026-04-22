# Задание №6 - Геометрические фигуры: круг, квадрат, прямоугольник

import math

# Класс Круг
class Circle:
    def __init__(self, center_x, center_y, radius):
        self.x = center_x      # координата X центра
        self.y = center_y      # координата Y центра
        self.radius = radius   # радиус круга

    def move(self, dx, dy):
        """Перемещение фигуры на dx, dy"""
        self.x += dx
        self.y += dy

    def resize(self, factor):
        """Изменение размера (умножение радиуса на factor)"""
        self.radius *= factor

    def area(self):
        """Вычисление площади круга: π * R²"""
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(center=({self.x}, {self.y}), radius={self.radius})"


# Класс Квадрат
class Square:
    def __init__(self, x, y, side):
        self.x = x        # координата X угла
        self.y = y        # координата Y угла
        self.side = side  # длина стороны

    def move(self, dx, dy):
        """Перемещение фигуры на dx, dy"""
        self.x += dx
        self.y += dy

    def resize(self, factor):
        """Изменение размера (умножение стороны на factor)"""
        self.side *= factor

    def area(self):
        """Вычисление площади квадрата: сторона²"""
        return self.side ** 2

    def __repr__(self):
        return f"Square(corner=({self.x}, {self.y}), side={self.side})"


# Класс Прямоугольник
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x          # координата X угла
        self.y = y          # координата Y угла
        self.width = width  # ширина
        self.height = height # высота

    def move(self, dx, dy):
        """Перемещение фигуры на dx, dy"""
        self.x += dx
        self.y += dy

    def resize(self, factor):
        """Изменение размера (умножение ширины и высоты на factor)"""
        self.width *= factor
        self.height *= factor

    def area(self):
        """Вычисление площади прямоугольника: ширина * высота"""
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle(corner=({self.x}, {self.y}), width={self.width}, height={self.height})"


# Демонстрация работы
if __name__ == "__main__":
    # Создаём объекты фигур
    circle = Circle(0, 0, 5)      # круг в центре (0,0) радиус 5
    square = Square(10, 10, 4)    # квадрат в (10,10) со стороной 4
    rect = Rectangle(1, 1, 6, 3)  # прямоугольник 6x3 в (1,1)

    # Выводим начальное состояние
    print("До изменений:")
    print(circle, "Площадь:", circle.area())
    print(square, "Площадь:", square.area())
    print(rect, "Площадь:", rect.area())

    # Применяем перемещения и изменения размеров
    circle.move(2, -1)   # сдвиг круга на (2, -1)
    circle.resize(2)     # увеличение радиуса в 2 раза
    square.move(-5, 0)   # сдвиг квадрата на (-5, 0)
    square.resize(1.5)   # увеличение стороны в 1.5 раза
    rect.move(3, 3)      # сдвиг прямоугольника на (3, 3)
    rect.resize(0.5)     # уменьшение размеров в 2 раза

    # Выводим конечное состояние
    print("\nПосле изменений:")
    print(circle, "Площадь:", circle.area())
    print(square, "Площадь:", square.area())
    print(rect, "Площадь:", rect.area())
