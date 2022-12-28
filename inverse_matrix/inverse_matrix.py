from sle.sle import *

matrix_origin = [
    [1, 2],
    [3, 4]
]


def unit_matrix(n: int) -> list:
    """Создание единичной матрицы"""
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


def connection(matrix: list) -> list:
    """Соединение 2 матриц - A|E"""
    mat = zero_matrix(len(matrix), len(matrix[0] * 2))
    matrix_unit = unit_matrix(len(matrix))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j < len(matrix):
                mat[i][j] = matrix[i][j]
            else:
                mat[i][j] = matrix_unit[i - len(matrix)][j - len(matrix)]
    return mat


def pick_nonzero_row(m, k):
    while k < np.shape(m)[0] and not m[k][k]:
        k += 1
    return k


def forward_stroke(matrix):
    """Прямой ход решения матрицы"""
    m = connection(matrix)
    n = len(m)
    for k in range(n):
        # 1) Swap k-row with one of the underlying if m[k, k] = 0
        swap_row = pick_nonzero_row(m, k)
        if swap_row != k:
            print('111', np.copy(m[k, :]))
            m[k, :], m[swap_row, :] = m[swap_row, :], np.copy(m[k, :])
        # 2) Make diagonal element equals to 1
        if m[k][k] != 1:
            num = m[k][k]
            for i in range(len(m[0])):
                m[k][i] *= 1 / num
        for row in range(k + 1, n):
            num = m[row][k]
            for i in range(len(m[0])):
                m[row][i] -= m[k][i] * num
    return m


def reverse_stroke(m):
    """Обратный ход решения матрицы"""
    n = len(m)
    for k in range(n - 1, 0, -1):
        for row in range(k - 1, -1, -1):
            if m[row][k]:
                num = m[k][k]
                for i in range(len(m[0])):
                    m[row][i] -= m[k][i] * num
    return m


def answer(m):
    row = len(m)
    col = int(len(m[0]) / 2)
    mat = zero_matrix(row, col)
    for i in range(row):
        for j in range(col):
            mat[i][j] = m[i][j - col]
    return mat


def inverse_matrix(matrix):
    m = forward_stroke(matrix)
    m = reverse_stroke(m)
    print(m)
    m = answer(m)
    return m


print(inverse_matrix(matrix_origin))
