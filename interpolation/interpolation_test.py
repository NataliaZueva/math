def test_add():
    a = [[2, 3, 0], [1, 5, 6]]
    b = [[0, 1, 4], [2, 5, 1]]
    exp = [[2, 4, 4], [3, 10, 7]]
    res = add(a, b)
    assert res == exp
