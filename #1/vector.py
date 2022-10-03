class Vector:
    """Класс, выполняющий различные функции с векторами"""

    def __init__(self, m=0, a=0, b=0, k=0):
        self.m = m
        self.a = a
        self.b = b
        self.k = k

    def angle(self):
        aa = Vector.length(self, self.a)
        bb = Vector.length(self, self.b)
        сс = Vector.scalar_product(self)
        c = (сс) / (abs(aa) * abs(bb))
        return c

    def func_general(self):
        if len(self.a) > len(self.b):
            for i in range(len(self.a) - len(self.b)):
                self.b.append(0)
        elif len(self.a) < len(self.b):
            for i in range(len(self.b) - len(self.a)):
                self.a.append(0)
        if len(self.a) == len(self.b):
            return self.a, self.b
        else:
            func_general()

    def scalar_product(self):
        Vector.func_general(self)
        c = 0
        for i in range(len(self.a)):
            c += self.a[i] * self.b[i]
            # print(c)
        return c

    def length(self, d):
        num = 0
        for i in range(len(d)):
            num += d[i] ** 2
        return (num) ** (0.5)

    def helps(self):
        eps = int(input("С какой точностью вы хотите узнать равенство векторов? "))
        return eps

    def func1(self):
        Vector.func_general(self)
        c = []
        for i in range(len(self.a)):
            c.append(self.a[i] + self.b[i])
        print("Сложение векторов: ", c)
        # print(f"c = ({self.a[0] + self.b[0]}, {self.a[1] + self.b[1]})")

    def func2(self):
        Vector.func_general(self)
        c = []
        for i in range(len(self.a)):
            c.append(self.a[i] - self.b[i])
        print("Вычитание векторов: ", c)

    def func3(self):
        c = Vector.scalar_product(self)
        print('Скалярное произведение векторов равно: ', c)

    def func4(self):
        Vector.func_general(self)
        z = 0
        x = 0
        if len(self.a) == len(self.b):
            for i in range(len(self.a)):
                if self.a[i] == self.b[i]:
                    z += 1
                elif self.a[i] - self.b[i] == 0:
                    x += 1
        if z == len(self.a) or x == len(self.a):
            print("Векторы равны")
        else:
            print("Векторы не равны")

    def func5(self):
        c = Vector.angle(self)
        print("Угол между векторами = ", c)
        if c == 0:
            print("Этот угол прямой")
        elif c > 0:
            print("Этот угол острый")
        elif c < 0:
            print("Этот угол тegjq")

    def func6(self):
        c = Vector.angle(self)
        if abs(c) == 1:
            print("Векторы коллинеарны")
        else:
            print("Векторы не коллинеарны")

    def func7(self):
        c = Vector.angle(self)
        if c == 1:
            print("Векторы сонаправлены")
        elif c == -1:
            print("Векторы противоположно направлены")
        else:
            print("Векторы разноправленны")

    def func8(self):
        Vector.func_general(self)
        eps = Vector.helps(self)
        z = 0
        if len(self.a) == len(self.b):
            for i in range(len(self.a)):
                if abs(self.a[i] - self.b[i]) < eps:
                    z += 1
        if z == len(self.a):
            print(f"Векторы равны c точностью {eps}")
        else:
            print("Векторы не равны c данной точностью {eps}")

    def func9(self):
        с = Vector.angle(self)
        if c == 0:
            print("Да, векторы ортогональны")
        elif c != 0:
            print("Нет, векторы не ортогональны")

    def func10(self):
        c = Vector.length(self, self.a)
        print("Длина вектора равна: ", c)

    def func11(self):
        num = 0
        for i in range(len(self.a)):
            num += self.a[i] ** 2
        d = 1 / num
        print("Hормировка вектора: ", d)

    def func12(self):
        c = self.a
        for i in range(len(c)):
            c[i] = c[i] * self.k
        print(f"Умножение на скаляр ({self.k}): ", c)

    def func13(self):
        c = self.a
        for i in range(len(c)):
            c[i] = c[i] / self.k
        print(f"Деление на скаляр (self.{k}): ", c)