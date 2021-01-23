class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0<value<100:
            self.__age = value
        else:
            self.__age = None

    def __str__(self):
        return f"{self.name}, {self.age}"

class Student(Human):
    def __init__(self, name, age, id_group):
        super().__init__(name, age)
        self.id_group = id_group

    @property
    def id_group(self):
        return self.__id_group

    @id_group.setter
    def id_group(self, value):
        if value in range(1,10):
            self.__id_group=value
        else:
            self.__id_group =None


    def study(self):
        print("studing")

    def __str__(self):
        return f"{super().__str__()}, {self.id_group}"

class Doctor(Human):
    def __init__(self, name, age, id_licence):
        Human.__init__(self,name, age)
        self.id_licence = id_licence


    @property
    def id_licence(self):
        return self.__id_licence

    @id_licence.setter
    def id_licence(self, value):
        if value in range(10000000,100000000):
            self.__id_licence =value
        else:
            self.__id_licence =None

    def cure(self):
        print("curing")

    def __str__(self):
        return f"{self.name}, {self.age}, {self.id_licence}"

class Vetirinar(Doctor):
    def __init__(self,name, age, id_licence):
        Doctor.__init__(self, name, age, id_licence)

class Pediatr(Doctor):
    pass

class Fighter(Human):
    def __init__(self, name, age, power, defence):
        Human.__init__(self, name, age)
        self.power = power
        self.defence = defence

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if 0<value<1000:
            self.__power = value
        else:
            self.__power = 0

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        if value in range(0,1000):
            self.__defence = value
        else:
            self.__defence = 0

    def fight(self, other_figher):
        if self.defence - other_figher.power>0 and self.power - other_figher.defence>0:
            print("We are winner")
        else:
            print("We are loser")

    def __str__(self):
        return f"{Human.__str__(self)}, {self.power}, {self.defence}"

    def __repr__(self):
        return f"{Human.__str__(self)}, {self.power}, {self.defence}"

class FighterDoc(Doctor, Fighter):
    def __init__(self,name, age, id_licence, power, defence):
        Doctor.__init__(self, name, age, id_licence)
        Fighter.__init__(self, name, age, power, defence)
    

    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.id_licence}, {self.power}, {self.defence}"