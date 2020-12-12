#Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
#Вывести на консоль количество максимальных чисел среди этих четырех.

def find_min(x, y):
    localmin = x
    if x>y:
        localmin = y
    return localmin

def find_max(x, y):
    localmax = x
    if x<y:
        localmax = y
    return localmax


def task01_print_min_value():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = int(input("Enter c"))
    d = int(input("Enter d"))
    mymin = find_min(find_min(a, b), find_min(c, d))
    print("min =", mymin)

def task02_print_max_count():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = int(input("Enter c"))
    d = int(input("Enter d"))
    mymax = find_max(find_max(find_max(a, b), c), d)
    count_max = 0
    if mymax == a:
        count_max += 1
    if mymax == b:
        count_max += 1
    if mymax == c:
        count_max += 1
    if mymax == d:
        count_max += 1
    print("max =", mymax)
    print("count max =", count_max)
