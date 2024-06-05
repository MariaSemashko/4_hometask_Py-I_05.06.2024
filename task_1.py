'''Напишите функцию для транспонирования матрицы'''


def transpose_matrix(matrix):
    if not matrix:
         return []
    transposed = [list(row) for row in zip(*matrix)]

    return transposed

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(transpose_matrix(matrix))