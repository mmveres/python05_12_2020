class Person:
    def __init__(self, name):
        self.name = name    # устанавливаем имя
        self.age = 1        # устанавливаем возраст

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            self.__age = None

    def display_info(self):
        print("Имя:", self.name, "\tВозраст:", self.age)


if __name__ == '__main__':
    tom = Person("Tom")
    tom.name = "Человек-паук"       # изменяем атрибут name
    tom.age = -129                  # изменяем атрибут age
    tom.display_info()              # Имя: Человек-паук     Возраст: -129