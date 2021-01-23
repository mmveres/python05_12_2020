from ua.univer.lesson07.inheritance.people import *

if __name__ == '__main__':
    st1 = Student("Tom", 20, 1)
    doc1 = Doctor("Haus", 50, 66666666)
    fight1 = Fighter("BrusLi",30,99,50)
    fight2 = Fighter("Conan",30,50,40)
    vet1 = Vetirinar("AyBolit", 70, 77777777)
    ped1 = Pediatr("P",30,88888888)
    fd = FighterDoc("F1",1,22222222,3,4)

    humans = [st1,doc1,fight1,fight2,vet1,ped1,fd]
    old_human = humans[0]
    for human in humans:
        if human.age> old_human.age:
            old_human = human
    print(old_human)

    fighters = []
    for human in humans:
        if isinstance(human,Fighter):
            fighters.append(human)

    print(fighters)

    for fight in fighters:
        print(fight)