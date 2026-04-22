from datetime import date

class Account:
    # Конструктор класса
    def __init__(self, owner_family, account_number, interest_rate, opening_date, amount):
        self.owner_family = owner_family      # фамилия владельца
        self.account_number = account_number  # номер счёта
        self.interest_rate = interest_rate    # процент начисления
        self.opening_date = opening_date      # дата открытия
        self.amount = amount                  # сумма в рублях

    # Смена владельца
    def change_owner(self, new_family):
        self.owner_family = new_family

    # Снятие денег
    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount

    # Пополнение счёта
    def deposit(self, amount):
        self.amount += amount

    # Начисление процентов
    def calculate_interest(self):
        self.amount += self.amount * (self.interest_rate / 100)

    # Конвертация в доллары
    def convert_to_dollars(self, rate=90):
        return self.amount / rate


# Демонстрация работы
acc = Account("Иванов", "12345", 5.5, date(2020, 1, 1), 10000)  # создаём счёт
acc.deposit(5000)           # пополняем на 5000
acc.withdraw(3000)          # снимаем 3000
acc.calculate_interest()    # начисляем проценты
print(f"Баланс: {acc.amount:.2f} руб.")                     # выводим баланс
print(f"В долларах: {acc.convert_to_dollars():.2f} USD")    # конвертируем в доллары
acc.change_owner("Петров")  # меняем владельца
print(f"Новый владелец: {acc.owner_family}")                # выводим нового владельца
