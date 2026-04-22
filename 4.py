import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # Сложение
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Вычитание
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    # Скалярное произведение
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Длина вектора
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Угол между векторами (в радианах)
    def angle(self, other):
        len_prod = self.length() * other.length()
        if len_prod == 0:
            return 0
        return math.acos(self.dot(other) / len_prod)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


# Демонстрация
if __name__ == "__main__":
    v1 = Vector3D(1, 0, 0)
    v2 = Vector3D(0, 1, 0)

    print("Сумма:", v1 + v2)
    print("Разность:", v1 - v2)
    print("Скалярное произведение:", v1.dot(v2))
    print("Длина v1:", v1.length())
    print("Угол между v1 и v2 (рад):", v1.angle(v2))
