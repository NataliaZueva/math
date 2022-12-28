from interpolation import *

global poi
poi = [[1, 2], [3, 4]]


def test_linear_equation():
    exp = 5
    res = linear_equation(1, 2, 3)
    assert res == exp


def test_interpolation_or_extrapolation():
    exp = 2.0
    res = interpolation_or_extrapolation(poi, 1)
    assert res == exp


def test_piecewise_linear_interpolation():
    exp = [[1.0, 1.0]]
    res = piecewise_linear_interpolation(poi)
    assert res == exp


def test_interpolated_elem():
    exp = False
    res = interpolated_elem(poi, 6)
    assert res == exp


def test_basis_polinom():
    exp = 7.0
    res = basis_polinom(poi, 6)
    assert res == exp
