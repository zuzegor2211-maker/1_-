#Задания №7
class product:

    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def __str__(self):
        return f"Товар: {self.name}, цена: {self.price}руб., вес: {self.weight} кг"
    
class product_group:
    
    def __init__(self):
        self.products = []
    
    def add_product(self,product): #Добавляет товар в группу
        self.products.append(product)
        print(f"Товар '{product.name}' добавлен в группу")

    def finish_product(self, product_name): #Удаляем товар по названию
        for product in self.products[:]:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Товар '{product_name}' удален из группы")
                return True
        print(f"Товар '{product_name}' не найден в группе")
        return False
    
    def amount(self):
        sumt = 0
        for product in self.products:
            sumt += product.price
        return sumt
    
#Создаем товары 
id01 = product("Яблока", 150, 1)
id02 = product("Молоко", 80, 1)
id03 = product("Хлеб", 45, 0.4)

group = product_group()
group.add_product(id01)
group.add_product(id02)
group.add_product(id03)
group.finish_product("Молоко")
group.finish_product("Банан")
group.finish_product("Хлеб")
print(group.amount())