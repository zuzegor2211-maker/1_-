# Задание №3 - Комплексные числа

class Complex:
    # Конструктор: действительная и мнимая часть
    def __init__(self, real, imag):
        self.real = real  # действительная часть
        self.imag = imag  # мнимая часть
    
    # Перегрузка оператора сложения (+)
    def __add__(self, other):
        # (a + bi) + (c + di) = (a+c) + (b+d)i
        return Complex(self.real + other.real, self.imag + other.imag)
    
    # Перегрузка оператора вычитания (-)
    def __sub__(self, other):
        # (a + bi) - (c + di) = (a-c) + (b-d)i
        return Complex(self.real - other.real, self.imag - other.imag)
    
    # Перегрузка оператора умножения (*)
    def __mul__(self, other):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    
    # Вывод комплексного числа в красивом виде
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Демонстрация работы
a = Complex(3, 2)  # 3 + 2i
b = Complex(1, 4)  # 1 + 4i

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")  # (3+2i) + (1+4i) = 4 + 6i
print(f"a - b = {a - b}")  # (3+2i) - (1+4i) = 2 - 2i
print(f"a * b = {a * b}")  # (3+2i)(1+4i) = (3-8) + (12+2)i = -5 + 14i
