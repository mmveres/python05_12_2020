from ua.univer.lesson02.task_if.task04 import task04_tezki
from ua.univer.lesson02.task_if.task_if_lib import task01_print_min_value, task02_print_max_count

print("1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.")
print("2. Вывести на консоль количество максимальных чисел среди этих четырех.")
print("4. Даны имена 2х человек (тип string). Если имена равны, то вывести сообщение о том, что люди являются тезками.")

print("press any int value for exit")
answer = input()
if answer == "1":
    task01_print_min_value()
elif answer == "2":
    task02_print_max_count()
elif answer == "4":
    task04_tezki()
else:
    print("No task no problem. Good bye...")