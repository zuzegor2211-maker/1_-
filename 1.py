#Задания №1
class Account:
    def __init__(self, last_name, account_number, interest, open_date, balance):
        self.last_name = last_name
        self.account_number = account_number
        self.interest = interest
        self.open_date = open_date
        self.balance = balance

        #Замена владельца счета
    def account_holder_change(self, new_owner):
        self.last_name = new_owner

        #Снятие денег со счета
    def withdrawing_money(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f"Снято: {withdrawal_amount}. Остаток: {self.balance}")
        else:
            print(f"Недостаточно средств. Доступно: {self.balance}")

        #Пополнение счета
    def deposit_money(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Пополнено: {deposit_amount}. Баланс: {self.balance}")

# Создание объекта
Ivan = Account('Sokolov', 77755522, 5, '12.12.2025', 5000)

# Вывод информации
print(f'{Ivan.last_name}, {Ivan.account_number}, {Ivan.open_date}, {Ivan.balance}')

# Тестирование методов
print
Ivan.withdrawing_money(1000)  # Снятие
Ivan.deposit_money(2000)      # Пополнение
Ivan.account_holder_change('Petrov')  # Смена владельца
print(f'Новый владелец: {Ivan.last_name}')
