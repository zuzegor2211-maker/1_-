# Задание №7 - Магазин: доставка товаров и группы товаров

class Product:
    """Класс, описывающий товар"""
    
    def __init__(self, name, price, weight):
        self.name = name      # название товара
        self.price = price    # цена товара
        self.weight = weight  # вес товара
    
    def __str__(self):
        return f"Товар: {self.name}, цена: {self.price}руб., вес: {self.weight} кг"


class ProductGroup:
    """Класс для формирования групп товаров с возможностью вычисления стоимости"""
    
    def __init__(self):
        self.products = []  # список товаров в группе
    
    def add_product(self, product):
        """Добавляет товар в группу"""
        self.products.append(product)
        print(f"Товар '{product.name}' добавлен в группу")

    def remove_product(self, product_name):
        """Удаляет товар из группы по названию"""
        # Проходим по копии списка, чтобы безопасно удалять элементы
        for product in self.products[:]:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Товар '{product_name}' удален из группы")
                return True
        print(f"Товар '{product_name}' не найден в группе")
        return False
    
    def total_price(self):
        """Вычисляет общую стоимость всех товаров в группе"""
        total = 0
        for product in self.products:
            total += product.price
        return total


# Демонстрация работы

# Создаём товары
id01 = Product("Яблоки", 150, 1)   # яблоки: 150 руб, 1 кг
id02 = Product("Молоко", 80, 1)    # молоко: 80 руб, 1 кг
id03 = Product("Хлеб", 45, 0.4)    # хлеб: 45 руб, 0.4 кг

# Создаём группу товаров
group = ProductGroup()

# Добавляем товары в группу
group.add_product(id01)
group.add_product(id02)
group.add_product(id03)

# Удаляем товары из группы
group.remove_product("Молоко")  # удаляем молоко
group.remove_product("Банан")   # попытка удалить несуществующий товар
group.remove_product("Хлеб")    # удаляем хлеб

# Выводим общую стоимость оставшихся товаров (только яблоки)
print(f"Общая стоимость товаров в группе: {group.total_price()} руб.")
