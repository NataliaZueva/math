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
    if len(matrix_cut) == 1 and parameter == 1:
        matrix[2][2] = matrix_cut[0][0]
        matrix[2][3] = matrix_cut[0][1]
    else:
        if len(matrix) != len(matrix_cut):
            no = len(matrix) - len(matrix_cut)
            for i in range(len(matrix) - len(matrix_cut) - 1, len(matrix_cut)):
                for j in range(len(matrix[0]) - len(matrix_cut[0]) - 1, len(matrix_cut[0])):
                    matrix[i + no][j + no] = round(matrix_cut[i][j], 2)
    return matrix


def moving_rows(matrix: list, stripe: int) -> list:
    """Поиск максимального элемента"""
    res_mat = cut_matrix(matrix, stripe, 1)
    m_col = matrix_index_col(res_mat, 0)
    index = leading_element_index(m_col)
    res_mat = permutation(res_mat, 0, index)
    matrix = filling_matrix_cut(matrix, res_mat, 1)
    return matrix


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
