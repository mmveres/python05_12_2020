# 4. Даны имена 2х человек (тип string). Если имена равны,
# то вывести сообщение о том, что люди являются тезками.

def namesake(name1= "anonim", name2="anonim"):
    if name1 == name2:
        print('The names are the same')
    else:
        print('Names are different')


def task04_tezki():
    n1 = (input('Enter first name: '))
    n2 = (input('Enter second name: '))
    namesake(name1= n1,name2= n2)


