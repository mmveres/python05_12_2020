class CCar:
    pass


class CShip:
    pass


class CPlane:
    pass

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
    Test_Vehicle().test_get_minprice_vehicle()