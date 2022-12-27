def zero_matrix(row, col):
    return [[0.0 for i in range(col)] for j in range(row)]


def copy2d(a, do_copy=True):
    if do_copy:
        return [b[:] for b in a]
    return a


def swap_rows(a, i, i2, do_copy=True):
    a = copy2d(a, do_copy)
    a[i], a[i2] = a[i2], a[i]
    return a


def add(a, b):
    """Сложение"""
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        mat_0 = zero_matrix(len(a), len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[0])):
                mat_0[i][j] = a[i][j] + b[i][j]
        return mat_0
    else:
        return "Матрицы разных размеров"


def sub(a, b):
    """Вычитание"""
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        mat_0 = zero_matrix(len(a), len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[0])):
                mat_0[i][j] = a[i][j] - b[i][j]
        return mat_0
    else:
        return None


def transposition(a):
    """Транспонирование"""
    mat_0 = zero_matrix(len(a[0]), len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            mat_0[j][i] = a[i][j]
    return mat_0


def multiplication_scalar(a, scal):
    """Умножение на скаляр"""
    mat_0 = zero_matrix(len(a[0]), len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            mat_0[i][j] = a[i][j] * scal
    return mat_0


def multiplication(a, b):
    """Умножение"""
    mat_0 = zero_matrix(len(b[0]), len(a))
    if len(a[0]) <= len(b[0]):
        for i in range(len(a)):
            for j in range(len(b[0])):
                mat_0[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
        return mat_0
    else:
        raise ValueError


def matrix_index_row(a, index):
    """Получение строки по индексу"""
    mat_0 = None
    try:
        mat_0 = a[index]
    except IndexError:
        raise
    finally:
        return mat_0


def matrix_index_col(a, index):
    """Получение столбца по индексу"""
    mat_0 = zero_matrix(len(a[0]), len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            mat_0[j][i] = a[i][j]
    mat_00 = None
    try:
        mat_00 = mat_0[index]
    except IndexError:
        raise
    finally:
        return mat_00


def permutation(a, i, i2):
    """Перестановка строк матрицы местами"""
    do_copy = zero_matrix(len(a), len(a[0]))
    return swap_rows(a, i, i2, do_copy)


def multiplication_index_scalar(a, index, scal):
    """Умножение одной строки матрицы по заданному индексу на скаляр"""
    do_copy = zero_matrix(len(a), len(a[0]))
    mat_0 = copy2d(a, do_copy)
    for j in range(len(a[0])):
        mat_0[index][j] = mat_0[index][j] * scal
    return mat_0


def division_index_scalar(a, index, scal):
    """Деление одной строки матрицы на число (по заданному индексу)"""
    do_copy = zero_matrix(len(a), len(a[0]))
    mat_0 = copy2d(a, do_copy)
    for j in range(len(a[0])):
        mat_0[index][j] = mat_0[index][j] / scal
    return mat_0


def add_or_sub_strings_number(a, arithmetic, i, i2, k):
    """Сложение/вычитание строк, умноженных на число"""
    do_copy = zero_matrix(len(a), len(a[0]))
    mat_0 = copy2d(a, do_copy)
    if arithmetic == '+':
        for j in range(len(mat_0[0])):
            mat_0[i][j] = mat_0[i][j] + mat_0[i2][j] * k
    elif arithmetic == '-':
        for j in range(len(mat_0[0])):
            mat_0[i][j] = mat_0[i][j] - mat_0[i2][j] * k
    return mat_0
