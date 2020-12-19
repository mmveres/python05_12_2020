from ua.univer.lesson03.exception.data_verify import input_int_value
from ua.univer.lesson03.matrix_tasks.matrix_helper import get_matrix_from_console, print_v1
from ua.univer.lesson03.matrix_tasks.matrix_tasks import print_positive_elem
from ua.univer.lesson03.matrix_tasks.matrix_test_data import get_matrix_2x3


if __name__ == '__main__':
    matrix = None
    while True:
        print("0. Вывести данные с консоли")
        print("1. Вывести все положительные елементы")
        answer = int(input("Enter answer"))
        if answer == 0 :
            matrix = get_matrix_from_console()
        elif answer == 1:
            if matrix != None:
                print_positive_elem(matrix)





