from ua.univer.lesson03.exception.data_verify import input_int_value


def print_v1(matrix):
    for irow in matrix:
        for ijcol in irow:
            print(ijcol, end="\t")
        print()

def print_v2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def get_matrix_from_console():
    matrix = []
    print("Enter number row")
    mrow = input_int_value()
    print("Enter number collumn")
    ncol = input_int_value()
    for i in range(mrow):
        matrix.append([])
        for j in range(ncol):
            print("Enter matrix[", i,"][",j,"]=")
            matrix[i].append(input_int_value())
    return matrix