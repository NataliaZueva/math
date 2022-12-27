from vector import *


def test_add():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [5, 10, 6]
    res = add(a, b)
    assert res == exp


def test_sub():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [-3, -6, 4]
    res = sub(a, b)
    assert res == exp


def test_sub_abs():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [-3, -6, 4]
    res = sub(a, b)
    assert res == exp


def test_scalar_product():
    a = [3, 4]
    b = [4, 3]
    exp = 24
    res = scalar_product(a, b)
    assert res == exp


def test_multiplication_by_scalar():
    a = [1, 2, 3]
    scal = 3
    exp = [3, 6, 9]
    res = multiplication_by_scalar(a, scal)
    assert res == exp


def test_colinearity():
    a = [3, -2, 1]
    b = [6, -4, 2]
    exp = True
    res = colinearity(a, b)
    assert res == exp


def test_vector_lenght():
    a = [4, 3]
    exp = 5
    res = vector_lenght(a)
    assert res == exp


def test_equal():
    a = [3, 4]
    b = [4, 3]
    exp = False
    res = equal(a, b)
    assert res == exp


def test_orthogonality():
    a = [1, 2]
    b = [2, -1]
    exp = True
    res = orthogonality(a, b)
    assert res == exp


def test_codirectional():
    a = [4, 0]
    b = [8, 0]
    exp = True
    res = codirectional(a, b)
    assert res == exp


def test_opposite():
    a = [4, 0]
    b = [8, 0]
    exp = False
    res = opposite(a, b)
    assert res == exp


def test_cos_of_vectors():
    a = [3, 4]
    b = [4, 3]
    exp = 0.96
    res = cos_of_vectors(a, b)
    assert res == exp


def test_equal_eps():
    a = [3, 4]
    b = [4, 3]
    eps = 2
    exp = True
    res = equal_eps(a, b, eps)
    assert res == exp


def test_angle_of_vectors():
    a = [3, 4]
    b = [4, 3]
    exp = 16.26
    res = angle_of_vectors(a, b)
    assert res == exp


def test_vector_normalize():
    a = [0, 1, 0]
    exp = 1.0
    res = vector_normalize(a)
    assert res == exp


def test_vector_projection():
    a = [1, 2]
    b = [3, 4]
    exp = 2.2
    res = vector_projection(a, b)
    assert res == exp
