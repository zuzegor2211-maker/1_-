
#Задания №2
class quadratic_equations:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

        #Проверка коэффициентов
    def checking_coefficient(self):
        if self.a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен 0 (уравнение не квадратное)")
        
        #Дискременат
    def discriminant(self):
        return self.b**2 - 4*self.a*self.c 

        #Нахождения корней
    def solve(self):
        D = self.discriminant()

        if D > 0:
            x1 = (-self.b + D**0.5) / (2*self.a)
            x2 = (-self.b - D**0.5) / (2*self.a)
            return x1, x2
        elif D == 0:
            x = -self.b / (2*self.a)
            return x
        else:
            return None

Ivan = quadratic_equations(1, -3, 2)  # x² - 3x + 2 = 0
print(f"Дискриминант: {Ivan.discriminant()}")
roots = Ivan.solve()
print(f"Корни уравнения: x1 = {roots[0]}, x2 = {roots[1]}")


