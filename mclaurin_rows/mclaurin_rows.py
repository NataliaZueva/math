def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def func_sin(x, n):
    value = 0
    for i in range(n + 1):
        value += ((-1) ** i * x ** (2 * i + 1)) / factorial(2 * i + 1)
    return round(value, 2)


def func_cos(x, n):
    value = 0
    for i in range(n + 1):
        value += ((-1) ** i * x ** (2 * i)) / factorial(2 * i)
    return round(value, 2)


def func_ar_(x, n):
    value = 0
    for i in range(n + 1):
        value += factorial(2 * i) * x ** (2 * i + 1) / \
                 (4 ** i * (factorial(i) ** 2) * (2 * i + 1))
    return value


def func_arcsin(x, n):
    return round(func_ar_(x, n), 2)


def func_arccos(x, n):
    pi = 3.1415
    return round(pi / 2 - func_ar_(x, n), 2)
