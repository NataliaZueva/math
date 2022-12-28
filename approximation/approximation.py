from sle.sle import *


def second_power_polunom(a, b, c, x):
    """Аппроксимация полиномом второй степени"""
    return a * x ** 2 + b * x + c


def third_power_polunom(a, b, c, d, x):
    """Аппроксимация полиномом третьей степени"""
    return a * x ** 3 + b * x ** 2 + c * x + d


a = [
    [1, 1],
    [3, 1],
    [5, 1]
]
x = [
    [0.99],
    [0.67]
]

b = [
    [1, 2],
    [3, 4],
    [3.5, 3],
    [6, 7]
]


def unification(a, b):
    '''Соединение двух матриц А + Х'''
    c = zero_matrix(len(a), len(a) + 1)
    for i in range(len(c)):
        for j in range(len(c[0])):
            if j < len(a[0]):
                c[i][j] = a[i][j]
            else:
                c[i][j] = b[i - len(a)][j - len(a)]
    return c


def finding_function_values(a, x):
    '''Линейная аппроксимация: поиск значений функции'''
    if len(x[0]) != 1:
        b = zero_matrix(len(a), int(len(x) / 2))
    else:
        b = zero_matrix(len(a), 1)
    for i in range(len(a)):
        for j in range(len(x)):
            if len(x[0]) != 1:
                b[i][i] += round(a[i][j] * x[j][i], 1)
                b[i][i - 1] += round((a[0][j] * x[j][0]) / 4, 1)
            else:
                b[i][0] += round(a[i][j] * x[j][0], 1)
    return b


def least_squares(matrix: list):
    """МНК"""
    matrix = copy2d(matrix)
    matrix_tr = transposition(matrix)
    b_part = transposition(matrix_tr[-1:])
    A_part = transposition(matrix_tr[:-1])
    matrix_tr = matrix_tr[:-1]
    A_tilda = finding_function_values(matrix_tr, A_part)
    b_tilda = finding_function_values(matrix_tr, b_part)
    return answer(unification(A_tilda, b_tilda))


def linear_aproximation(xy_data: list):
    """Линейная аппроксимация: поиск коэффициентов функции"""
    matrix = [[x, 1, y] for x, y in xy_data]
    return least_squares(matrix)


print(linear_aproximation(b))
