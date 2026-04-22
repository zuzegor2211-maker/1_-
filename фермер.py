import random

# ================= БАЗОВЫЙ КЛАСС ЖИВОТНОГО =================
class Animal:
    def __init__(self, name, price, food_cost, growth_time, product, product_price, meat_price):
        self.name = name
        self.price = price              # Цена покупки
        self.food_cost = food_cost      # Стоимость кормления
        self.growth_time = growth_time  # Дней до взросления
        self.product = product          # Какой продукт даёт
        self.product_price = product_price  # Цена продукта
        self.meat_price = meat_price    # Цена мяса
        self.age = 0                    # Текущий возраст
        self.is_adult = False           # Взрослое?
        self.fed_today = False          # Кормили сегодня?

    def feed(self, farmer):
        """Кормление: списывает деньги, увеличивает возраст"""
        if farmer.money >= self.food_cost:
            farmer.money -= self.food_cost
            self.age += 1
            self.fed_today = True
            if self.age >= self.growth_time:
                self.is_adult = True
            return True
        return False

    def get_product(self):
        """Сбор продукта (только если взрослое и сытое)"""
        if self.is_adult and self.fed_today:
            self.fed_today = False  # После сбора становится голодным
            return self.product, self.product_price
        return None, 0


# ================= БАЗОВЫЙ КЛАСС РАСТЕНИЯ =================
class Plant:
    def __init__(self, name, price, growth_time, product, sell_price):
        self.name = name
        self.price = price              # Цена посадки
        self.growth_time = growth_time  # Дней до созревания
        self.product = product          # Что даёт
        self.sell_price = sell_price    # Цена продажи
        self.age = 0
        self.is_ready = False
        self.watered_today = False

    def water(self):
        self.watered_today = True

    def grow(self):
        """Рост только если полито"""
        if self.watered_today:
            self.age += 1
            if self.age >= self.growth_time:
                self.is_ready = True
            self.watered_today = False

    def harvest(self):
        """Сбор урожая"""
        if self.is_ready:
            self.is_ready = False
            self.age = 0
            return self.sell_price
        return 0

class Farmer:
    def __init__(self):
        self.money = 100                # Стартовый капитал
        self.animals = []               # Список животных
        self.plants = []                # Список растений
        self.products = {}              # Склад: {название: количество}
        self.max_animals = 3            # Лимит животных
        self.max_crops = 5              # Лимит растений
        self.actions_today = 0          # Сделано действий сегодня
        self.max_actions = 5            # Максимум действий в день
        self.day = 1                    # Текущий день

        # Шаблоны животных (имя, цена, корм, рост, продукт, цена_продукта, цена_мяса)
        self.animal_templates = {
            'Курица': ('Курица', 10, 9, 4, 'яйцо', 5, 14),
            'Корова': ('Корова', 30, 9, 6, 'молоко', 8, 114),
            'Овца': ('Овца', 20, 9, 5, 'шерсть', 75, 80)
        }

        # Шаблоны растений (имя, цена, рост, продукт, цена_продажи)
        self.plant_templates = {
            'Пшеница': ('Пшеница', 5, 3, 'зерно', 20),
            'Кукуруза': ('Кукуруза', 4, 4, 'початок', 25),
            'Картошка': ('Картошка', 3, 5, 'картофель', 30)
        }

        # Цены на продукты (для продажи)
        self.prices = {'яйцо': 5, 'молоко': 8, 'шерсть': 75, 'зерно': 20, 'початок': 25, 'картофель': 30}

    def _use_action(self):
        """Проверка лимита действий"""
        if self.actions_today >= self.max_actions:
            print("Действий на сегодня не осталось! Закончите день.")
            return False
        return True

    def buy_animal(self, animal_type):
        if not self._use_action() or len(self.animals) >= self.max_animals:
            print(f"Нет места! Максимум {self.max_animals} животных.")
            return False
        name, price, food, growth, prod, prod_price, meat = self.animal_templates[animal_type]
        if self.money >= price:
            self.animals.append(Animal(name, price, food, growth, prod, prod_price, meat))
            self.money -= price
            self.actions_today += 1
            print(f"{animal_type} куплена!")
            return True
        print(f"Не хватает {price - self.money} монет!")
        return False

    def plant_crop(self, crop_type):
        if not self._use_action() or len(self.plants) >= self.max_crops:
            print(f"Нет полей! Максимум {self.max_crops}.")
            return False
        name, price, growth, prod, sell = self.plant_templates[crop_type]
        if self.money >= price:
            self.plants.append(Plant(name, price, growth, prod, sell))
            self.money -= price
            self.actions_today += 1
            print(f"{crop_type} посажена!")
            return True
        print(f"Не хватает {price - self.money} монет!")
        return False

    def feed_animals(self):
        if not self._use_action():
            return
        fed = sum(1 for a in self.animals if a.feed(self))
        if fed:
            self.actions_today += 1
            print(f"Покормлено {fed} животных, потрачено {fed * 9} монет")
        else:
            print("Нет денег или все сыты!")

    def water_crops(self):
        if not self._use_action() or not self.plants:
            print("Нет растений для полива!")
            return
        cost = len(self.plants) * 2
        if self.money >= cost:
            self.money -= cost
            for p in self.plants:
                p.water()
            self.actions_today += 1
            print(f"Полито {len(self.plants)} растений, потрачено {cost} монет")
        else:
            print(f"Не хватает {cost - self.money} монет на полив!")

    def collect_products(self):
        if not self._use_action():
            return
        collected = 0
        for a in self.animals:
            prod, price = a.get_product()
            if prod:
                self.products[prod] = self.products.get(prod, 0) + 1
                collected += 1
        if collected:
            self.actions_today += 1
            print(f"Собрано {collected} продуктов!")
        else:
            print("Нет продуктов! Животные должны быть взрослыми и сытыми.")

    def harvest_crops(self):
        if not self._use_action():
            return
        total = 0
        harvested = []
        for i, p in enumerate(self.plants):
            val = p.harvest()
            if val:
                total += val
                harvested.append(i)
        if harvested:
            for i in reversed(harvested):
                del self.plants[i]
            self.money += total
            self.actions_today += 1
            print(f"Собрано {len(harvested)} урожаев на {total} монет!")
        else:
            print("Нет созревших растений!")

    def sell_products(self):
        if not self._use_action() or not self.products:
            print("Нет продуктов для продажи!")
            return
        total = sum(count * self.prices[prod] for prod, count in self.products.items())
        self.money += total
        self.products.clear()
        self.actions_today += 1
        print(f"Продано на {total} монет! Теперь у вас {self.money} монет")

    def sell_animal_for_meat(self):
        if not self._use_action() or not self.animals:
            print("Нет животных для продажи!")
            return
        for i, a in enumerate(self.animals):
            status = "взрослое" if a.is_adult else f"молодое ({a.age}/{a.growth_time})"
            print(f"{i+1}. {a.name} - {status}, мясо: {a.get_meat_price()} монет")
        try:
            choice = int(input("Выбор: ")) - 1
            if 0 <= choice < len(self.animals):
                a = self.animals[choice]
                price = a.get_meat_price()
                self.money += price
                del self.animals[choice]
                self.actions_today += 1
                print(f"Продано за {price} монет!")
        except ValueError:
            print("Ошибка ввода!")

    def upgrade_farm(self):
        if not self._use_action():
            return
        print("1. Расширить загон (+2 места) - 200 монет")
        print("2. Вспахать поля (+3 поля) - 150 монет")
        choice = input("Выбор: ")
        if choice == "1" and self.money >= 200:
            self.money -= 200
            self.max_animals += 2
            self.actions_today += 1
            print(f"Загон расширен! Теперь {self.max_animals} животных")
        elif choice == "2" and self.money >= 150:
            self.money -= 150
            self.max_crops += 3
            self.actions_today += 1
            print(f"Поля расширены! Теперь {self.max_crops} культур")
        else:
            print("Не хватает денег или неверный выбор!")

    def random_event(self):
        """Случайное событие в конце дня (40% шанс)"""
        if random.random() > 0.4:
            return
        events = [
            ("Дождь!", lambda: [p.water() for p in self.plants], "Растения политы бесплатно!"),
            ("Ярмарка!", lambda: [setattr(self.prices, k, int(v*1.5)) for k,v in self.prices.items()], "Цены +50%!"),
            ("Находка!", lambda: setattr(self, 'money', self.money + random.randint(10, 50)), "Нашли монеты!"),
            ("Сосед помог!", lambda: [setattr(a, 'fed_today', True) or setattr(a, 'age', a.age+1) or setattr(a, 'is_adult', a.age>=a.growth_time) for a in self.animals], "Бесплатный корм!"),
        ]
        name, effect, desc = random.choice(events)
        print(f"СОБЫТИЕ: {name} - {desc}")
        effect()

    def next_day(self):
        """Переход к следующему дню"""
        print(f"\n=== День {self.day} завершён ===")
        self.random_event()
        for p in self.plants:
            p.grow()
        for a in self.animals:
            a.fed_today = False
        self.day += 1
        self.actions_today = 0
        print(f"=== ДЕНЬ {self.day} НАЧАЛСЯ! Денег: {self.money} ===")

    def show_status(self):
        """Отображение статуса фермы"""
        print(f"\nДень {self.day} | Действий: {self.actions_today}/{self.max_actions} | Денег: {self.money}")
        print(f"Животные: {len(self.animals)}/{self.max_animals}")
        for a in self.animals:
            print(f"  {a.name}: {'взрослое' if a.is_adult else f'{a.age}/{a.growth_time}'}, {'сытое' if a.fed_today else 'голодное'}")
        print(f"Растения: {len(self.plants)}/{self.max_crops}")
        for p in self.plants:
            print(f"  {p.name}: {'созрело' if p.is_ready else f'{p.age}/{p.growth_time}'}, {'полито' if p.watered_today else 'не полито'}")
        if self.products:
            print(f"Склад: {self.products}")

class Game:
    def __init__(self):
        self.farmer = Farmer()
        self.win_condition = 100000

    def run(self):
        print("ДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР ФЕРМЕРА!")
        print(f"Цель: заработать {self.win_condition} монет")
        name = input("Имя фермера: ")
        print(f"Удачи, {name}!\n")

        while True:
            print("\n1-Купить животное 2-Посадить 3-Кормить 4-Полить 5-Собрать продукты")
            print("6-Собрать урожай 7-Продать склад 8-Продать на мясо 9-Улучшить 10-Статус 11-Спать 0-Выход")
            choice = input("Выбор: ")

            if choice == "1":
                for i, name in enumerate(self.farmer.animal_templates, 1):
                    print(f"{i}. {name} - {self.farmer.animal_templates[name][1]} монет")
                idx = input("Номер: ")
                if idx.isdigit() and 1 <= int(idx) <= 3:
                    self.farmer.buy_animal(list(self.farmer.animal_templates.keys())[int(idx)-1])
            elif choice == "2":
                for i, name in enumerate(self.farmer.plant_templates, 1):
                    print(f"{i}. {name} - {self.farmer.plant_templates[name][1]} монет")
                idx = input("Номер: ")
                if idx.isdigit() and 1 <= int(idx) <= 3:
                    self.farmer.plant_crop(list(self.farmer.plant_templates.keys())[int(idx)-1])
            elif choice == "3":
                self.farmer.feed_animals()
            elif choice == "4":
                self.farmer.water_crops()
            elif choice == "5":
                self.farmer.collect_products()
            elif choice == "6":
                self.farmer.harvest_crops()
            elif choice == "7":
                self.farmer.sell_products()
            elif choice == "8":
                self.farmer.sell_animal_for_meat()
            elif choice == "9":
                self.farmer.upgrade_farm()
            elif choice == "10":
                self.farmer.show_status()
            elif choice == "11":
                if self.farmer.actions_today > 0:
                    self.farmer.next_day()
                else:
                    print("Сделайте хоть что-нибудь перед сном!")
            elif choice == "0":
                print("До встречи!")
                break

            if self.farmer.money >= self.win_condition:
                print(f"ПОБЕДА! {name} заработал {self.farmer.money} монет за {self.farmer.day} дней!")
                break

if __name__ == "__main__":
    Game().run()