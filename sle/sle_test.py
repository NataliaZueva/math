from sle import *

global myA, myB
myA = [
    [2.0, 4.0, 1.0, 36],
    [5.0, 2.0, 1.0, 47],
    [2.0, 3.0, 4.0, 37]
]

myB = [
    [100, 100, 100],
    [100, 100, 100]
]


def test_leading_element_index():
    m = [1, 0, 9]
    res = leading_element_index(m)
    exp = 2
    assert res == exp


def test_cut_matrix():
    exp = [[2.0, 1.0, 47], [3.0, 4.0, 37]]
    res = cut_matrix(myA, 1, 1)
    assert res == exp


def test_filling_matrix_cut():
    exp = [[2.0, 4.0, 1.0, 36], [5.0, 100, 100, 100], [2.0, 100, 100, 100]]
    res = filling_matrix_cut(myA, myB, 1)
    assert res == exp


def test_moving_rows():
    exp = [[5, 2, 1, 47], [2, 4, 1, 36], [2, 3, 4, 37]]
    res = moving_rows(myA, 0)
    assert res == exp


def test_normalization_levels():
    exp = [1.0, 2.0, 0.5, 18.0]
    res = normalization_levels(myA[0], 1)
    assert res == exp


def test_subtracting_first_line():
    exp = [[2.0, 4.0, 1.0, 36], [5.0, 1.0, 0.5, 23.5], [2.0, 0.0, 0.83, 11.17]]
    res = subtracting_first_line(myA, 1)
    assert res == exp


def test_gauss():
    exp = [[1.0, 0.4, 0.2, 9.4], [0.0, 1.0, 0.19, 5.38], [0.0, 0.0, 1.0, 2.0]]
    res = gauss(myA)
    assert res == exp
