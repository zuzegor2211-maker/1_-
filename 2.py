# Задание №2 - Квадратное уравнение

class quadratic_equations:
    # Конструктор класса, принимает коэффициенты a, b, c
    def __init__(self, a, b, c):
        self.a = a  # коэффициент при x²
        self.b = b  # коэффициент при x
        self.c = c  # свободный член

    # Проверка коэффициентов (убеждаемся, что уравнение квадратное)
    def checking_coefficient(self):
        if self.a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен 0 (уравнение не квадратное)")
        
    # Вычисление дискриминанта
    def discriminant(self):
        return self.b**2 - 4*self.a*self.c 

    # Нахождение корней уравнения
    def solve(self):
        D = self.discriminant()  # получаем дискриминант

        if D > 0:  # два корня
            x1 = (-self.b + D**0.5) / (2*self.a)
            x2 = (-self.b - D**0.5) / (2*self.a)
            return x1, x2
        elif D == 0:  # один корень
            x = -self.b / (2*self.a)
            return x
        else:  # корней нет
            return None

# Создаём объект: уравнение x² - 3x + 2 = 0
Ivan = quadratic_equations(1, -3, 2)

# Выводим дискриминант
print(f"Дискриминант: {Ivan.discriminant()}")

# Находим и выводим корни
roots = Ivan.solve()
print(f"Корни уравнения: x1 = {roots[0]}, x2 = {roots[1]}")
