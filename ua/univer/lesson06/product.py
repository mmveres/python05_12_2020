import json, logging
from datetime import datetime

from ua.univer.lesson06.currency import Currency

logging.basicConfig(filename='product.log', level=logging.ERROR, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class ProductException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)

class Product:
    def __init__(self, name = None, price = 1, weight = 1):
        self.__name = name
        self.set_price(price)
        self.set_weight(weight)

    def get_name(self):
        return self.__name

    def set_price(self, value):
        if value > 0:
            self.__price = value/Currency.usd
            logging.info("set price" + str(value))
        else:
            self.__price = None
            str_err = "Error price, value < 0"
            print(str_err)
            raise ProductException(str_err)
          #  if self.__price !=None:
          #      print("Error price")
          #  else:
          #      self.__price = None
    def get_discount_price(self):
        if self.get_name() == "Tom":
            return self.get_price()*0.9

    def get_price(self):
        return self.__price*Currency.usd*(1.20+0.10+0.15)

    def set_weight(self, value):
        if 0<value<100:
            self.__weight = value
        else:
            self.__weight = None
            print("Error weight")

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.get_name()}, {self.get_price()}, {self.get_weight()}"

    def __repr__(self):
        return f"Product {self.__name}, {self.__price}, {self.__weight}"
