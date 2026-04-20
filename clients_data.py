# clients_data.py - файл с данными клиентов

from datetime import datetime

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

# Функция для создания списка клиентов
def get_clients_list():
    """Возвращает список клиентов агробанка"""
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
        ),
        # Добавим еще одного клиента для демонстрации
        Client_Agricultural_Bank(
            client_id="005",
            client_type="фермер физлицо",
            name="Петров Петр Петрович",
            region="Воронежская область",
            activity="животноводство"
        )
    ]
    return clients

def show_all_clients(clients):
    """Показать всех клиентов банка"""
    print("\n=== СПИСОК КЛИЕНТОВ АГРОБАНКА ===")
    for i, client in enumerate(clients, 1):
        print(f"{i}. {client.info()}")


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