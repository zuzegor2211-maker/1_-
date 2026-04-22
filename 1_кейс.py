from clients_data import get_clients_list, show_all_clients, find_client_by_id, find_client_by_name
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

#Класс банковский счёт клиента
#Баланса и базовые операции со счётом
class Account:
    def __init__(self, account_number, owner, current_balance, currency="RUB"):
        self.account_number = account_number # номер счёта
        self.owner = owner # владелец счёта
        self.current_balance = current_balance # текущий баланс
        self.currency = currency # валюта счёта

    # Метод для получения текущего баланса
    def current_balance(self):
        return self.current_balance
    
    #Пополнения
    def deposit(self, amount):
        if amount > 0:
            self._current_balance += amount
            return True
        return False
    
    #Списание
    def withdraw(self, amount):
        if 0 < amount <= self._current_balance:
            self._current_balance -= amount
            return True
        return False
    
    #формируем инфо о балансе счёта
    def get_balance_info(self):
        return f"Баланс счёта {self.account_number}: {self._current_balance:.2f} {self.currency}"
    
    #строковое представления счёта
    def __str__(self):
        return (f"Счёт №{self.account_number}, Владелец: {self.owner.name}, "
                f"Баланс: {self._current_balance:.2f} {self.currency}")

class InvestmentAgroCreditAccount(Account):
    def __init__(self, account_number, owner, credit_purpose, interest_rate,
                 loan_term_months, initial_balance=0.0, currency="RUB"):
        super().__init__(account_number, owner, initial_balance, currency)
        self.credit_purpose = credit_purpose # цель кредита
        self.interest_rate = interest_rate  # годовая процентная ставка
        self.loan_term_months = loan_term_months # срок кредита в месяцах 
    
    #Рассчитывает начисленые проценты за указанный период
    def calculate_interest(self, months=1):
        monthly_rate = self.interest_rate / 12 / 100
        interest = self._current_balance * monthly_rate * months
        return interest
    
    def __str__(self):
        base_info = super().__str__()
        return (f"{base_info}, Цель кредита: {self.credit_purpose}, "
                f"Ставка: {self.interest_rate}%, Срок: {self.loan_term_months} мес.")

class SeasonalOperatingAccount(Account):
    def __init__(self, account_number, owner, season, credit_purpose,
                 interest_rate, initial_balance=0.0, currency="RUB"):
        super().__init__(account_number, owner, initial_balance, currency)
        self.season = season  # сезон
        self.credit_purpose = credit_purpose # цель кредита
        self.interest_rate = interest_rate # процента ставка

    # Рассчитывает проценты с учётом сезонной корректировки ставки
    def calculate_interest(self, months=1):
        # Сезонная ставка может меняться в зависимости от сезона
        effective_rate = self.interest_rate * 1.2 if self.season == "весна" else self.interest_rate
        monthly_rate = effective_rate / 12 / 100
        interest = self._current_balance * monthly_rate * months
        return interest

    def __str__(self):
        base_info = super().__str__()
        return (f"{base_info}, Сезон: {self.season}, Цель: {self.credit_purpose}, "
                f"Ставка: {self.interest_rate}%")

class Transaction:
    def __init__(self, transaction_type, amount, source_account=None, destination_account=None, description=""):
        self.timestamp = datetime.now() # дата и время создания транзакции 
        self.transaction_type = transaction_type  # пополнение, списание, перевод, начисление процентов
        self.amount = amount # сумма операции
        self.source_account = source_account # счёт, с которого списываются средства
        self.destination_account = destination_account # счёт, на который зачисляются средства
        self.description = description #комментария платежа

    #делаем вид информации о транзакции
    def get_transaction_info(self):
        info = (f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"Тип: {self.transaction_type} | Сумма: {self.amount:.2f}")
        if self.source_account:
            info += f" | Источник: {self.source_account.account_number}"
        if self.destination_account:
            info += f" | Получатель: {self.destination_account.account_number}"
        if self.description:
            info += f" | Назначение: {self.description}"
        return info

    def __str__(self):
        return self.get_transaction_info()
    
    #Проверяет валидность транзакции перед выполнением.
    #Выполняет базовую проверку корректности данных
    def is_valid(self):
        if self.amount <= 0:
            return False
        if self.transaction_type == 'перевод':
            return self.source_account is not None and self.destination_account is not None
        elif self.transaction_type == 'списание':
            return self.source_account is not None
        elif self.transaction_type == 'пополнение':
            return self.destination_account is not None
        # Для других типов (например, 'начисление процентов') считаем валидной, если сумма > 0
        return True
    #Выполняем транзакцию,если все хорошо
    def execute(self):
        if not self.is_valid():
            return False
        try:
            if self.transaction_type == "списание":
                return self.source_account.withdram(self.amount)
            elif self.transaction_type == 'пополнение':
                return self.destination_account.deposit(self.amount)
            elif self.transaction_type == 'перевод':
                # Для перевода сначала списываем со источника, затем пополняем получателя
                if self.source_account.withdraw(self.amount):
                    self.destination_account.deposit(self.amount)
                    return True
                return False
            elif self.transaction_type == 'начисление процентов':
                # Начисление процентов — это пополнение счёта
                return self.destination_account.deposit(self.amount)
            else:
                # Неизвестный тип транзакции
                return False
        except Exception as e:
            print(f"Ошибка при выполнении транзакции: {e}")
            return False
        
# Получаем список клиентов из внешнего файла
clients = get_clients_list()

print(show_all_clients(clients)) #список клиентов
print(find_client_by_id(clients, "001")) #поиск клиента по id
print(find_client_by_name(clients,"Иванов Иван Иванович")) #поиск клиента по имени

