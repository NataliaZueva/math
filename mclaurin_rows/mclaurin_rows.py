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


print(cos_f(5, 3))
