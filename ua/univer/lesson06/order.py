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
    def find_max_weight_product(self, products):
        max_weight_product = products[0]
        for product in products:
            if max_weight_product.get_weight()< product.get_weight():
                max_weight_product = product
        print(max_weight_product)