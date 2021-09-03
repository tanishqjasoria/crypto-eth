import mod


class EllipticCurve:

    def __init__(self, name, p, a, b):
        assert (4 * a ** 3 + 27 * b ** 2) % p != 0
        self.name = name
        self.p = p
        self.a = a
        self.b = b

    def __eq__(self, other):
        return (self.a, self.b, self.p) == (other.a, other.b, other.p)

    def y2(self, x):
        return (x ** 3 + self.a * x + self.b) % self.p

    def points(self):
        points = []
        for i in range(self.p):
            points.append((i, self.y2(i)))
        return points

    def is_belongs(self, point):
        if point is None:
            return True

        x, y = point
        return ((y * y) % self.p) == self.y2(x)

    def negPoint(self, point):

        assert self.is_belongs(point)

        if point is None:
            return None

        x, y = point

        res = (x, -y % self.p)

        assert self.is_belongs(res)

        return res

    def sum(self, point1, point2):

        assert self.is_belongs(point1)
        assert self.is_belongs(point2)

        if point1 is None:
            return point2

        if point2 is None:
            return point1

        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2 and y1 != y2:
            return None

        if x1 == x2:
            # This is the case point1 == point2.
            m = (3 * x1 * x1 + self.a) * mod.inverse_extended_euclidean(2 * y1, self.p)
        else:
            # This is the case point1 != point2.
            m = (y1 - y2) * mod.inverse_extended_euclidean(x1 - x2, self.p)

        x3 = m * m - x1 - x2
        y3 = y1 + m * (x3 - x1)
        res = (x3 % self.p,
               -y3 % self.p)

        assert self.is_belongs(res)

        return res

    def scalarMul(self, k, point):

        assert self.is_belongs(point)

        if point is None:
            return None

        if k < 0:
            return self.scalarMul(-k, self.negPoint(point))

        res = None
        num = point

        while k:
            if k & 1:
                res = self.sum(res, num)

            num = self.sum(num, num)

            k >>= 1

        assert self.is_belongs(res)

        return res

    def subGroup(self, g, n, h):

        return EllipticCurveSubGroup(
            self.name,
            self.p,
            self.a,
            self.b,
            g,
            n,
            h
        )


class EllipticCurveSubGroup(EllipticCurve):

    def __init__(self, name, p, a, b, g, n, h):
        assert (4 * a ** 3 + 27 * b ** 2) % p != 0
        super(EllipticCurveSubGroup, self).__init__(name, p, a, b)

        self.g = g
        self.n = n
        self.h = h

    def __eq__(self, other):
        return (self.a, self.b, self.p, self.g, self.n, self.h) == (
            other.a, other.b, other.p, other.g, other.n, other.h)

    # def is_belongs(self, point):
    #     belongs_to_curve = super(EllipticCurveSubGroup, self).is_belongs(point)
    #     if belongs_to_curve:
    #         belongs_to_subgroup = self.scalarMul(self.n, point) == point
    #
    #     return belongs_to_curve and belongs_to_subgroup


class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y
        self.point = (x, y)
        if x is None or y is None:
            self.point = None
        assert curve.is_belongs(self.point)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        x, y = self.curve.sum(self.point, other.point)

        return Point(self.curve, x, y)

    def __mul__(self, other):
        if isinstance(other, Point):
            raise Exception('Cannot multiply two Points')

        x, y = self.curve.scalarMul(other, self.point)

        return Point(self.curve, x, y)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return self.point.__str__()

    def __iter__(self):
        return self.point.__iter__()

    def __eq__(self, other):
        return self.point == other.point


class Ideal(Point):
    def __init__(self, curve):
        super().__init__(curve, None, None)

    def __neg__(self):
        return self

    def __add__(self, other):
        return other

    def __mul__(self, other):
        if isinstance(other, Point):
            raise Exception('Cannot multiply two Points')
        return self

    def __str__(self):
        return "Ideal"

    def __iter__(self):
        return ().__iter__()

    def __eq__(self, other):
        if other.point is None:
            return True
        return False


def bits(n):
    while n:
        yield n & 1
        n >>= 1


def double_and_add(n, x):
    res = 0
    num = x

    for bit in bits(n):
        if bit == 1:
            res += num
        num += num
    return res
