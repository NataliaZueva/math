import math


def add(a, b):
    '''Сложение векторов'''
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    '''Вычитание векторов'''
    return [x - y for x, y in zip(a, b)]


def scalar_product(a, b):
    """Скалярное произведение"""
    return sum([x * y for x, y in zip(a, b)])


def multiplication_by_scalar(a, scal):
    """Умножение вектора на скаляр"""
    return [x * scal for x in a]


def colinearity(a, b):
    """Проверка на колинеарность"""
    c = scalar_product(a, b) / (abs(vector_lenght(a)) * abs(vector_lenght(b)))
    return abs(c) == 1


def vector_lenght(a):
    """Вычисление длинны вектора"""
    return (sum([i ** 2 for i in a])) ** 0.5


def equal(a, b):
    """Равны ли вектора"""
    l = len(a)
    for i in range(l):
        if a[i] != b[i]:
            return False
    return True


def orthogonality(a, b):
    """Ортогональность векторов"""
    if colinearity(a, b) == 0:
        return True
    else:
        return False


def codirectional(a, b):
    """Сонаправленость векторов"""
    c = cos_of_vectors(a, b)
    if c == 1:
        return True
    else:
        return False


def opposite(a, b):
    """Противоположнонаправленные векторa"""
    c = cos_of_vectors(a, b)
    if c == -1:
        return True
    else:
        return False


def cos_of_vectors(a, b):
    """Вычесление коссинуса угла между двумя векторами"""
    return scalar_product(a, b) / (vector_lenght(a) * vector_lenght(b))


def equal_eps(a, b, eps):
    """Равенсто векторов с точностью eps"""
    z = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if abs(a[i] - b[i]) < eps:
                z += 1
    if z == len(a):
        return True
    else:
        return False


def angle_of_vectors(a, b):
    """Угол между векторами в градусах"""
    radian = 57.2958
    return round(math.acos(cos_of_vectors(a, b)) * radian, 2)


def vector_normalize(a):
    """Нормализация вектора"""
    num = 0
    for i in range(len(a)):
        num += a[i] ** 2
    d = 1 / num
    return d


def vector_projection(a, b):
    """Проекция вектора а на b"""
    return scalar_product(a, b) / vector_lenght(b)
