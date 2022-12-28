from sle.sle import *

points = [[2, 5], [6, 9]]


def calc_linear_function(points: list) -> list:
    """Возвращает a b коэффиценты из слау"""
    initial_equation = [[x, 1, y] for x, y in points]
    output_ab = answer(initial_equation)
    return output_ab


print('fdsef', calc_linear_function(points))
