# 7. Характеристикой строки целочисленной матрицы
# назовем сумму ее положительных элементов.
# Переставляя строки заданной матрицы,
# расположить их в соответствии с ростом характеристик

def sort_matrix(matrix):
    sum_row_list = []
    for row in matrix:
        sum = 0
        for cell in row:
            sum+=cell
        sum_row_list.append(sum)
    print(sum_row_list)

    for j in range(len(sum_row_list)-1):
        for i in range(len(sum_row_list)-1-j):
            if sum_row_list[i]>sum_row_list[i+1]:
                temp = sum_row_list[i]
                temp_row = matrix[i]

                sum_row_list[i] = sum_row_list[i+1]
                matrix[i] = matrix[i+1]

                sum_row_list[i+1] =temp
                matrix[i+1] = temp_row

    print(sum_row_list)

if __name__ == '__main__':
    matrix=[[1,2,3,4],
            [2,2,7,7],
            [1,1,1,1]
    ]
    matrix[1]
    sort_matrix(matrix)
    print(matrix)