class Client_Agricultural_Bank:

    def __init__(self, client_id, client_type, name, region, activity):
        self.client_id = client_id  # уникальный идентификатор клиента
        self.client_type = client_type  # тип клиента (фермер физлицо, КФХ, агрофирма)
        self.name = name  # наименование (ФИО или название хозяйства)
        self.region = region  # регион
        self.activity = activity  # основной вид деятельности

    def info(self):
        return (f"Тип: {self.client_type}, "
                f"Название: {self.name}, "
                f"Регион: {self.region}, "
                f"Деятельность: {self.activity}")
    
    def __str__(self):
        return self.info()
    
class Client:
    def __init__(self,account_number,owner,current_balance,currency):
        self.account_number = account_number # номер счёта
        self.owner = owner # владелец
        self.current_balance = current_balance # текущий баланс
        self.currency = currency # валюта
    
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
    
# Создание списка клиентов
clients = [
    Client_Agricultural_Bank(
        client_id="001",
        client_type="фермер физлицо",
        name="Иванов Иван Иванович",
        region="Краснодарский край",
        activity="растениеводство"
    ),
    Client_Agricultural_Bank(
        client_id="002",
        client_type="КФХ",
        name="КФХ 'Золотой колос'",
        region="Ростовская область",
        activity="смешанное"
    ),
    Client_Agricultural_Bank(
        client_id="003",
        client_type="агрофирма",
        name="Агрофирма 'Юг-Агро'",
        region="Ставропольский край",
        activity="животноводство"
    ),
    Client_Agricultural_Bank(
        client_id="004",
        client_type="КФХ",
        name="КФХ 'Урожайное'",
        region="Волгоградская область",
        activity="растениеводство"
    )
]

def show_all_clients(clients):
        for client in clients:
            print(f"{client.info()}")


account1 = Client("000001", clients[0], 50000, "RUB")
account1.withdraw(1000)
account1.get_balance()
account1.deposits(10000)
account1.get_balance()
print(account1)
