from datetime import date

class Account:
    def __init__(self, owner_family, account_number, interest_rate, opening_date, amount):
        self.owner_family = owner_family
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.opening_date = opening_date
        self.amount = amount

    def change_owner(self, new_family):
        self.owner_family = new_family

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def calculate_interest(self):
        self.amount += self.amount * (self.interest_rate / 100)

    def convert_to_dollars(self, rate=90):
        return self.amount / rate


# Демо
acc = Account("Иванов", "12345", 5.5, date(2020, 1, 1), 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.calculate_interest()
print(f"Баланс: {acc.amount:.2f} руб.")
print(f"В долларах: {acc.convert_to_dollars():.2f} USD")
acc.change_owner("Петров")
print(f"Новый владелец: {acc.owner_family}")
