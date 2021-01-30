import abc
from abc import ABC


class CPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if -100<value<100:
            self.__x = value
        else:
            self.__x = 0

    def __str__(self):
        return f"[{self.x}, {self.y}]"

class CVehicle(metaclass=abc.ABCMeta):
    class Engine():
        def __init__(self, fuel):
            self.fuel = fuel

    def __init__(self, price, speed, year, point):
        self.point = point
        self.year = year
        self.speed = speed
        self.price = price
        self.engine = None

    @abc.abstractmethod
    def set_engine(self): pass
    def get_engine(self):
        return self.engine

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if 1900<value<2022:
            self.__year = value
        else: self.__year = None

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0<value<10000:
            self.__speed = value
        else: self.__speed = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @abc.abstractmethod
    def show(self): pass

    def __str__(self):
        return f"{self.year}, {self.price}, {self.speed},{self.point}"
    def __repr__(self):
        return f"{self.year}, {self.price}, {self.speed}"


class IMoveAble(ABC):
    @abc.abstractmethod
    def move(self): pass


class CCar(CVehicle, IMoveAble):
    def move(self):
        return self.speed

    def __init__(self,price,speed,year):
        CVehicle.__init__(self,price,speed,year, CPoint(100000,1))

    def set_engine(self):
        self.engine = self.Engine("diesel")

    def show(self):
        print("Car", self.__str__())

    def __str__(self):
        return f"{CVehicle.__str__(self)}"


class ISwimAble(ABC):
    @abc.abstractmethod
    def swim(self): pass


class CShip(CVehicle, ISwimAble):


    def swim(self):
        return self.speed

    def __init__(self, price, speed, year, port, passangers):
        CVehicle.__init__(self, price, speed, year, CPoint(1,1))
        self.port = port
        self.passangers = passangers

    def set_engine(self):
        pass

    def show(self):
        print("CShip", self.__str__())

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"


class IFlyAble(ABC):
    @abc.abstractmethod
    def fly(self): pass


class CPlane(CVehicle, IFlyAble):


    def fly(self):
        return self.speed

    def __init__(self, price, speed, year,passangers, height):
        CVehicle.__init__(self, price, speed, year, CPoint(1,1))
        self.height = height
        self.passangers = passangers

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0 < value < 10000:
            self.__height = value
        else:
            self.__height = None
    def set_engine(self):
        pass

    def show(self):
        pass

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"

class Amfibia(CCar, ISwimAble):
    def __init__(self, price, speed, year,passangers, height):
        super().__init__(price, speed, year)
    def swim(self):
        return self.speed / 2

class BatMobile(CCar, ISwimAble, IFlyAble):
    def __init__(self, price, speed, year,passangers, height):
        super().__init__(price, speed, year)
    def swim(self):
        return 100

    def fly(self):
        return self.speed * 2


# 1. вывести на екран механизм с наибольшей ценой
# 2. получить механизм с наименьшей ценой
# 3. получить механизм с ценой меньше 10000
# после 2000 года
# 4. получить масив механизмов год
# выпуска с 2000 по 2010
# 5. получить масив механизмов не
# старше 5 лет с средней ценой(+- 20%)
# и скоростью в диапазоне от 100 до 200

class Vehicles:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def print_maxprice_vehicle(self):
        pass

    def get_minprice_vehicle(self):
        pass

    def get_price_less_after_vehicle(self, less_price=10000, after_year=2000):
        pass

    def get_vehicles_in_range(self, start_year=2000, end_year=2010):
        pass

    def get_vehicles_less_with_aver_price_and_speed_in_range(self,age_year=5,start_speed=100, end_speed=200):
        pass


class Test_Vehicle:
    def test_get_minprice_vehicle(self):
        vehicles = Vehicles(
            [CCar(10000, 150, 2000),
             CShip(500000, 70, 2019, 'Odessa', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             CCar(10000, 150, 2000),
             CShip(500000, 70, 2019, 'Chernomorsk', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             ]
        )
        min_price_exp = 10000
        min_price_act = vehicles.get_minprice_vehicle()
        if min_price_exp == min_price_act:
            print("Correct")
        else:
            print("Error")

if __name__ == '__main__':
    veh = [CCar(10000, 150, 2000),
           CShip(500000, 70, 2019, 'Odessa', 1050),
           CPlane(1000000, 960, 2020, 200, 10000),
           Amfibia(10000, 150, 2000, 200, 10000),
           BatMobile(500000, 70, 2019, 'Chernomorsk', 1050),
           CPlane(1000000, 960, 2020, 200, 10000)
           ]

    swims = []
    for v in veh:
        if isinstance(v,ISwimAble):
            swims.append(v)
    for s in swims:
        print(s.swim())
    #Test_Vehicle().test_get_minprice_vehicle()