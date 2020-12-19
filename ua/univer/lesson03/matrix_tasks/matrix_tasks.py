# Дана целочисленная прямоугольная матрица.
# 1. Вывести все положительные елементы;
# 2. Вывести количество строк, не содержащих ни одного нулевого элемента;
# 3. Вывести номера столбцов, содержащих хотя бы
#    один нулевой элемент;
# 4. Вывести количество строк и номера строк в
# которых есть отрицательные елементы.
# 5. Вывести максимальное из чисел,
# встречающихся в заданной матрице более одного раза.
# 6. Вывести номер строки, в которой находится
# самая длинная серия одинаковых элементов.
# 7. Характеристикой строки целочисленной матрицы
# назовем сумму ее положительных четных элементов.
#    Переставляя строки заданной матрицы,
# расположить их в соответствии с ростом характеристик.
from ua.univer.lesson03.matrix_tasks.matrix_test_data import *

def print_positive_elem(matrix):
    print("--------------------------")
    for row in matrix:
        for cell in row:
            if cell >= 0:
                print(cell, end="\t")
            else:
                print("-", end="\t")
        print()

def get_count_row_without_zero(matrix):
    count_row_without_zero = 0
    for row in matrix:
        is_zero = False
        for cell in row:
            if cell == 0:
                is_zero = True
                break
        if is_zero == False and len(row)>0:
            count_row_without_zero+=1
    return count_row_without_zero

def get_count_collumn_with_zero():
    # TODO реализовать функцию
    pass

if __name__ == '__main__':
    m =[
        [],
        []
    ]
    print(get_count_row_without_zero(m))
    print(get_count_row_without_zero(get_matrix_2x3()))
    print(get_count_row_without_zero(get_matrix_with_0_3x3()))
    print(get_count_row_without_zero(get_matrix_with_negative_3x3()))