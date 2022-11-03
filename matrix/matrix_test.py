from matrix import *


def test_add():
    a = [[2, 3, 0], [1, 5, 6]]
    b = [[0, 1, 4], [2, 5, 1]]
    exp = [[2, 4, 4], [3, 10, 7]]
    res = add(a, b)
    assert res == exp


def test_sub():
    a = [[2, 3, 0], [1, 5, 6]]
    b = [[0, 1, 4], [2, 5, 1]]
    exp = [[2, 2, -4], [-1, 0, 5]]
    res = sub(a, b)
    assert res == exp


def test_transposition():
    a = [[2, 3, 5], [5, 7, 6]]
    exp = [[2, 5], [3, 7], [5, 6]]
    res = transposition(a)
    assert res == exp


def test_multiplication_scalar():
    a = [[1, 2], [3, 4]]
    scal = 2
    exp = [[2, 4], [6, 8]]
    res = multiplication_scalar(a, scal)
    assert res == exp


def test_multiplication():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    exp = [[19, 22], [43, 50]]
    res = multiplication(a, b)
    assert res == exp


def test_matrix_index_row():
    a = [[1, 3], [2, 3], [3, 5]]
    index = 1
    exp = [2, 3]
    res = matrix_index_row(a, index)
    assert res == exp


def test_matrix_index_col():
    a = [[1, 3], [2, 3], [3, 5]]
    index = 1
    exp = [3, 3, 5]
    res = matrix_index_col(a, index)
    assert res == exp


def test_permutation():
    a = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
    k, n = 1, 2
    exp = [[1, 1, 1], [3, 3, 3], [2, 2, 2], [4, 4, 4]]
    res = permutation(a, k, n)
    assert res == exp


def test_multiplication_index_scalar():
    a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    index, scal = 1, 2
    exp = [[1, 1, 1], [4, 4, 4], [3, 3, 3]]
    res = multiplication_index_scalar(a, index, scal)
    assert res == exp


def test_add_or_sub_strings_number():
    a = [[1, 2], [3, 4]]
    arithmetic, i, i2, k = '-', 1, 0, 2
    exp = [[1, 2], [1, 0]]
    res = add_or_sub_strings_number(a, arithmetic, i, i2, k)
    assert res == exp
