from mclaurin_rows import *


def test_factorial():
    n = 6
    exp = 720
    res = factorial(n)
    assert res == exp


def test_func_sin():
    x, n = 4, 2
    exp = 1.87
    res = func_sin(x, n)
    assert res == exp


def test_func_cos():
    x, n = 4, 2
    exp = 3.67
    res = func_cos(x, n)
    assert res == exp


def test_func_arcsin():
    x, n = 4, 2
    exp = 91.47
    res = func_arcsin(x, n)
    assert res == exp


def test_func_arccos():
    x, n = 4, 2
    exp = -89.9
    res = func_arccos(x, n)
    assert res == exp
