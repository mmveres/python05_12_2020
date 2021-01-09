from ua.univer.lesson05.oop.users import Person

if __name__ == '__main__':
    user1 = Person()
    user1.get_from_file("userTom.csv")
    user1.show()

    user2 = Person("Bob",30, 2000)
    user2.show()
