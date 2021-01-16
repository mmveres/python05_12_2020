# Класс Product содержит поля
# -наименование(яблоки, бананы, компьютер, телефон)
# -вес
# -цена
# написать методами класса
# Создать массив из 10 продуктов.
# 1) Найти с максимальным весом с ценой менее 10 грн
# 2) Найти с максимальной ценой весом 3 кг
# 3) Найти с общий вес всех продуктов
# 4) Найти с общую стоимость всех продуктов
# 5) Найти все яблоки
# 6) Найти яблоки с максимальной ценой
# 7) Найти среднюю стоимость овощей

class Order:
    def __init__(self, products=[]):
        self.__products = products

    def add(self, product):
        self.__products.append(product)

    def find_max_weight_product(self):
        max_weight_product = self.__products[0]
        for product in self.__products:
            if max_weight_product.get_weight() < product.get_weight():
                max_weight_product = product
        print(max_weight_product)

    def find_max_price(self):
        max_price = self.__products[0]
        for prod in self.__products:
            if max_price.get_price() < prod.get_price():
                max_price = prod
        return max_price


    def total_weight(self):
        total = 0
        for prod in self.__products:
            total += prod.get_weight

        print(repr(total))


    def total_price(self):
        total = 0
        for prod in self.__products:
            total += prod.get_price()
        return (repr(total))


    def average_price(self):
        total = 0
        count = 0
        for prod in self.__products:
            total += prod.get_price
        count += 1
        average = total / count
        print(repr(average))

    def get_total_check(self):
        str_order = "Our order :"
        for product in self.__products:
            str_order+="\n" + product.__str__()
        str_order+="\ntotal price :"
        str_order+= self.total_price()
        return str_order

    def save_total_check(self):
        with open("check.txt", "w") as file_write:
            file_write.write(self.get_total_check())