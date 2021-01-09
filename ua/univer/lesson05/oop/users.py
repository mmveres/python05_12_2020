class Person:
    def __init__(self, name = None, age = None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.salary)

    def get_from_file(self, filename):
        with open(filename, "r", encoding="UTF") as myfile:
            user_str = myfile.readline()
        user = tuple(user_str.split(";"))
        self.name = user[0]
        self.age = user[1]
        self.salary = user[2]