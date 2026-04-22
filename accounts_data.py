# accounts_data.py - файл с данными о счетах клиентов

from keus_1 import Client
from clients_data import get_clients_list, find_client_by_id

# Получаем список клиентов
clients_list = get_clients_list()

def get_accounts_list():
    """Возвращает список счетов клиентов"""
    
    # Находим клиентов по ID для привязки счетов
    client_001 = find_client_by_id(clients_list, "001")  # Иванов Иван Иванович
    client_002 = find_client_by_id(clients_list, "002")  # КФХ 'Золотой колос'
    client_003 = find_client_by_id(clients_list, "003")  # Агрофирма 'Юг-Агро'
    client_004 = find_client_by_id(clients_list, "004")  # КФХ 'Урожайное'
    client_005 = find_client_by_id(clients_list, "005")  # Петров Петр Петрович
    
    accounts = [
        Client(
            account_number="00001",
            owner=client_001,
            current_balance=150000.50,
            currency="RUB"
        ),
        Client(
            account_number="00002",
            owner=client_001,
            current_balance=5000.75,
            currency="USD"
        ),
        Client(
            account_number="00003",
            owner=client_002,
            current_balance=2500000.00,
            currency="RUB"
        ),
        Client(
            account_number="00004",
            owner=client_002,
            current_balance=15000.00,
            currency="EUR"
        ),
        Client(
            account_number="00005",  # ИСПРАВЛЕНО: было 000005
            owner=client_003,
            current_balance=8750000.50,
            currency="RUB"
        ),
        Client(
            account_number="00006",  # ИСПРАВЛЕНО: было 000006
            owner=client_004,
            current_balance=1200000.00,
            currency="RUB"
        ),
        Client(
            account_number="00007",  # ИСПРАВЛЕНО: было 000007
            owner=client_004,
            current_balance=25000.00,
            currency="USD"
        ),
        Client(
            account_number="00008",  # ИСПРАВЛЕНО: было 000008
            owner=client_005,
            current_balance=350000.75,
            currency="RUB"
        ),
    ]
    return accounts

# показать все счета клиентов
def show_all_accounts(accounts):
    print("\n=== СПИСОК ВСЕХ СЧЕТОВ КЛИЕНТОВ ===")
    for i, account in enumerate(accounts, 1):
        print(f"{i}. {account}")
    print("="*50)

# найти все счета владельца по имени
def find_accounts_by_owner(accounts, owner_name):
    found_accounts = []
    for account in accounts:
        if account.owner.name.lower() == owner_name.lower():
            found_accounts.append(account)
    return found_accounts

# найти счёт по номеру
def find_account_by_number(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

# получить суммарный баланс клиента по всем счетам
def get_total_balance_by_client(accounts, owner_name):
    total = 0
    currencies = {}
    
    for account in accounts:
        if account.owner.name.lower() == owner_name.lower():
            total += account.current_balance
            if account.currency in currencies:
                currencies[account.currency] += account.current_balance
            else:
                currencies[account.currency] = account.current_balance
    
    return total, currencies

# ИСПРАВЛЕНИЕ ЗДЕСЬ: добавляем проверку на прямой запуск
accounts = get_accounts_list()
show_all_accounts(accounts)