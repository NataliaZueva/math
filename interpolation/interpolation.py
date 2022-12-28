from sle.sle import *


def calc_linear_function(points: list) -> list:
    """Возвращает a b коэффиценты из СЛАУ"""
    initial_equation = [[x, 1, y] for x, y in points]
    output_ab = answer(initial_equation)
    return output_ab


def linear_equation(a: float, b: float, x: float) -> float:
    """Возвращает y линейной функции"""
    return a * x + b


def interpolation_or_extrapolation(points: list, x: float) -> float:
    """Возвращает интерпалированное или экстраполированное значение"""
    return_value = calc_linear_function(points)
    return linear_equation(*return_value, x)


def piecewise_linear_interpolation(matrix: list) -> list:
    """Вывод ответов на Кусочно-линейную интерполяцию"""
    res_mat = []
    for i in range(len(matrix) - 1):
        prob_mat = [matrix[i], matrix[i + 1]]
        mat = calc_linear_function(prob_mat)
        for j in range(len(mat)):
            mat[j] = round(mat[j], 1)
        res_mat.append([*mat])
    return res_mat


def interpolated_elem(points: list, x: float) -> bool:
    """Интерпалированное значение или нет"""
    return points[0][0] <= x <= points[-1][0]


def basis_polinom(data_xy: list, x: float) -> float:
    """Возвращает l(y), базисный полином Лангранжа"""
    data_x, data_y = matrix_index_col(data_xy, 0), matrix_index_col(data_xy, 1)
    polynomial = 0
    for i in range(len(data_x)):
        basis_polynomial = 1
        for j in range(len(data_x)):
            if i == j:
                continue
            basis_polynomial *= (x - data_x[j]) / (data_x[i] - data_x[j])
        polynomial += data_y[i] * basis_polynomial
    return polynomial
