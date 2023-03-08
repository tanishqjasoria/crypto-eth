field_modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583
# See, it's prime!
assert pow(2, field_modulus, field_modulus) == 2

def FQ(prime):
    class FQ:
        p = prime
        def __init__(self, n):
            try:
                self.n = n % FQ.p
            except:
                TypeError("Can't cast type %s to %s in __init__" % (type(n).__name__, type(self).__name__))

        def __add__(self, other):
            if
    return FQ


def IntegersModP(p):
    class IntegerModP(FieldElement):
        def __init__(self, n):
            self.n = n % p
            self.field = IntegerModP

        def __add__(self, other): return IntegerModP(self.n + other.n)
        def __sub__(self, other): return IntegerModP(self.n - other.n)
        def __mul__(self, other): return IntegerModP(self.n * other.n)
        def __truediv__(self, other): return self * other.inverse()
        def __div__(self, other): return self * other.inverse()
        def __neg__(self): return IntegerModP(-self.n)
        def __eq__(self, other): return isinstance(other, IntegerModP) and self.n == other.n
        def __abs__(self): return abs(self.n)
        def __str__(self): return str(self.n)
        def __repr__(self): return '%d (mod %d)' % (self.n, self.p)

        def __divmod__(self, divisor):
            q,r = divmod(self.n, divisor.n)
            return (IntegerModP(q), IntegerModP(r))

        def inverse(self):
            ...?

        IntegerModP.p = p
        IntegerModP.__name__ = 'Z/%d' % (p)
        return IntegerModP