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
    )
]

def show_all_clients(clients):
        for client in clients:
            print(f"{client.info()}")

# Вызов класс-метода
print(show_all_clients(clients))

