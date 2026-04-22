from clients_data import Client_Agricultural_Bank, get_clients_list
class Client:
    def __init__(self, account_number, owner, current_balance, currency):
        self.account_number = account_number  # номер счёта
        self.owner = owner  # владелец
        self.current_balance = current_balance  # текущий баланс
        self.currency = currency  # валюта
    
    # метод пополнения баланса
    def deposits(self, amount): 
        if amount > 0:
            self.current_balance += amount
            print(f"Пополнение на {amount} {self.currency}. Новый баланс: {self.current_balance} {self.currency}")
        else:
            print("Сумма пополнения должна быть положительной")
    
    # метод списания баланса
    def withdraw(self, amount): 
        if amount <= 0:
            print("Сумма списания должна быть положительная")
        elif amount > self.current_balance:
            print(f"Недостаточно средств! Доступно: {self.current_balance} {self.currency}")
        else:
            self.current_balance -= amount
            print(f"Списание {amount} {self.currency}. Остаток: {self.current_balance} {self.currency}")
    
    def get_balance(self):
        return f"Баланс счёта {self.account_number}: {self.current_balance} {self.currency}"
    
    def __str__(self):
        return f"Счёт №{self.account_number}, Владелец: {self.owner.name}, Баланс: {self.current_balance} {self.currency}"

clients = get_clients_list()

def show_all_clients(clients):
    """Показать всех клиентов банка"""
    for client in range(clients):
        return client.info()

def find_client_by_id(clients, client_id):
    """Найти клиента по ID"""
    for client in clients:
        if client.client_id == client_id:
            return client
    return None

def find_client_by_name(clients, name):
    """Найти клиента по имени"""
    for client in clients:
        if client.name.lower() == name.lower():
            return client
    return None

# Получаем список клиентов из внешнего файла

print(show_all_clients(clients)) #список клиентов
print(find_client_by_id(clients, "001")) #поиск клиента по id
print(find_client_by_name(clients,"Иванов Иван Иванович")) #поиск клиента по имени

