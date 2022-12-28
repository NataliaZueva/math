import numpy as np

from matrix.matrix import *
from vector.vector import *


def leading_element_index(matrix: list) -> int:
    """Нахождение индекса максимального элемента"""
    i = 0
    index = max(matrix)
    while matrix[i] != index:
        i += 1
    return i


def cut_matrix(matrix: list, stripe: int, parameter: int) -> list:
    """Обрезка матрицы"""
    a = np.shape(matrix)
    matrix_result = matrix
    if len(a) > 1:
        if stripe != 0:
            length = len(matrix) - stripe
            matrix_result = zero_matrix(length, length + parameter)
            for i in range(len(matrix_result)):
                for j in range(len(matrix_result[0])):
                    matrix_result[i][j] = matrix[i + stripe][j + stripe]
    return matrix_result


def filling_matrix_cut(matrix: list, matrix_cut: list, parameter: int) -> list:
    n1 = len(matrix) - 1
    if len(matrix_cut) == 1 and parameter == 1:
        matrix[n1][n1] = round(matrix_cut[0][0], 2)
        matrix[n1][n1 + 1] = round(matrix_cut[0][1], 2)
    else:
        if len(matrix) != len(matrix_cut):
            no = len(matrix) - len(matrix_cut)
            for i in range(len(matrix) - len(matrix_cut) - 1, len(matrix_cut)):
                for j in range(len(matrix[0]) - len(matrix_cut[0]) - 1, len(matrix_cut[0])):
                    matrix[i + no][j + no] = round(matrix_cut[i][j], 2)
    return matrix


def moving_rows(matrix: list, stripe: int) -> list:
    """Поиск максимального элемента"""
    # res_mat = cut_matrix(matrix, stripe, 1)
    res_mat = matrix
    m_col = matrix_index_col(res_mat, 0)
    index = leading_element_index(m_col)
    res_mat = permutation(res_mat, 0, index)
    # matrix = filling_matrix_cut(matrix, res_mat, 1)
    return res_mat


def normalization_levels(matrix: list, stripe: int) -> list:
    """нормализация уровней'"""
    if stripe != 0:
        res_mat = cut_matrix(matrix, stripe, 1)
    else:
        res_mat = matrix
    n = len(res_mat)
    index = res_mat[0]
    if index != 0:
        for i in range(n):
            res_mat[i] = round((res_mat[i] / index), 4)
    matrix = filling_matrix_cut(matrix, res_mat, 1)
    return matrix


def subtracting_first_line(matrix: list, stripe: int) -> list:
    """вычитание первой строки"""
    res_mat = cut_matrix(matrix, stripe, 1)
    if res_mat[0][0] != 1:
        n = len(res_mat)
        for i in range(n):
            res_mat[i] = normalization_levels(res_mat[i], 0)
    n = len(res_mat)
    for i in range(1, n):
        res_mat[i] = sub(res_mat[0], res_mat[i])
    matrix = filling_matrix_cut(matrix, res_mat, 1)
    return matrix


def gauss(matrix: list) -> list:
    """Прямая последовательность"""
    result_matrix = copy2d(matrix)
    k = len(result_matrix)
    for j in range(k):
        result_matrix = moving_rows(result_matrix, j)
        n = len(result_matrix)
        for i in range(n):
            result_matrix[i] = normalization_levels(result_matrix[i], j)
        result_matrix = subtracting_first_line(result_matrix, j)
    return result_matrix


def answer(matrix):
    res_mat = gauss(matrix)
    ans = []
    ans1 = zero_matrix(len(matrix), len(matrix))
    k = 0
    for i in reversed(res_mat):
        k += 1
        for j in range(len(res_mat[0])):
            if i[j] == 1:
                if not ans:
                    ans.append(i[j + k])
                else:
                    if j + k <= len(matrix):
                        num = i[j + k]
                        ans.append(num)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            ans1[i][j] = res_mat[i][j]
    ans = ans[::-1]
    ans = np.linalg.solve(ans1, ans)
    for j in range(len(ans)):
        ans[j] = round(ans[j], 1)
    return ans
