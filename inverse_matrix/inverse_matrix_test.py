from inverse_matrix import *


def test_unit_matrix():
    n = 3
    exp = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    res = unit_matrix(n)
    assert res == exp


def test_connection():
    matrix = [[1, 2], [3, 4]]
    exp = [[1, 2, 1, 0], [3, 4, 0, 1]]
    res = connection(matrix)
    assert res == exp


def test_pick_nonzero_row():
    m, k = [[1, 2], [3, 4]], 2
    exp = 2
    res = pick_nonzero_row(m, k)
    assert res == exp


def test_forward_stroke():
    matrix = [[1, 2], [3, 4]]
    exp = [[1, 2, 1, 0], [-0.0, 1.0, 1.5, -0.5]]
    res = forward_stroke(matrix)
    assert res == exp


def test_reverse_stroke():
    matrix = [[1, 2, 1, 0], [-0.0, 1.0, 1.5, -0.5]]
    exp = [[1.0, 1.0, -0.5, 0.5], [-0.0, 1.0, 1.5, -0.5]]
    res = reverse_stroke(matrix)
    assert res == exp


def test_answer():
    matrix = [[1.0, 1.0, -0.5, 0.5], [-0.0, 1.0, 1.5, -0.5]]
    exp = [[-0.5, 0.5], [1.5, -0.5]]
    res = answer(matrix)
    assert res == exp


def test_inverse_matrix():
    matrix = [[1, 2], [3, 4]]
    exp = [[-0.5, 0.5], [1.5, -0.5]]
    res = inverse_matrix(matrix)
    assert res == exp
