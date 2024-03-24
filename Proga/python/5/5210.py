class Fraction:
    def _lazy_gcd(self):
        a = abs(self.num)
        b = abs(self.den)
        while b:
            a, b = b, a % b
        self.num //= a
        self.den //= a

    @staticmethod
    def __very_lazy_sub_gcd(num, den):
        fst = abs(num)
        scnd = abs(den)
        while scnd:
            fst, scnd = scnd, fst % scnd
        return num // fst, den // fst

    def __init__(self, *args):
        if len(args) > 1:
            self.num = args[0]
            self.den = args[1]
        elif '/' not in str(args[0]):
            self.num = int(args[0])
            self.den = 1
        else:
            self.num = int(args[0].split('/')[0])
            self.den = int(args[0].split('/')[1])
        self._lazy_gcd()

    def numerator(self, new_numerator=0):
        if not new_numerator:
            return abs(self.num)
        else:
            self.num = new_numerator
            self._lazy_gcd()

    def denominator(self, new_denominator=0):
        if not new_denominator:
            return abs(self.den)
        else:
            self.den = new_denominator
            self._lazy_gcd()

    def __str__(self):
        if self.num > 0 and self.den > 0:
            return f'{self.num}/{self.den}'
        elif self.num > 0 and self.den < 0 or self.num < 0 and self.den > 0:
            return f'{-abs(self.num)}/{abs(self.den)}'
        else:
            return f'{abs(self.num)}/{abs(self.den)}'

    def __repr__(self):
        if self.num > 0 and self.den > 0:
            f"Fraction('{self.num}/{self.den}')"
        elif self.num > 0 and self.den < 0 or self.num < 0 and self.den > 0:
            return f"Fraction('{-abs(self.num)}/{abs(self.den)}')"
        else:
            return f"Fraction('{abs(self.num)}/{abs(self.den)}')"

    @staticmethod
    def __check(value):
        if isinstance(value, Fraction):
            return value
        else:
            return Fraction(value, 1)

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        other = self.__check(other)
        return Fraction(self.num * other.den + other.num * self.den,
                        other.den * self.den)

    def __sub__(self, other):
        other = self.__check(other)
        return Fraction(self.num * other.den - other.num * self.den,
                        other.den * self.den)

    def __iadd__(self, other):
        other = self.__check(other)
        self.num, self.den = self.__very_lazy_sub_gcd(self.num * other.den
                                                      + self.den * other.num, self.den * other.den)
        return self

    def __isub__(self, other):
        other = self.__check(other)
        self.num, self.den = self.__very_lazy_sub_gcd(self.num * other.den
                                                      - self.den * other.num, self.den * other.den)
        return self

    def __mul__(self, other):
        other = self.__check(other)
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        other = self.__check(other)
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __itruediv__(self, other):
        other = self.__check(other)
        self.num = self.num * other.den
        self.den = self.den * other.num
        self._lazy_gcd()
        return self

    def __imul__(self, other):
        other = self.__check(other)
        self.num = self.num * other.num
        self.den = self.den * other.den
        self._lazy_gcd()
        return self

    def reverse(self):
        return Fraction(self.den, self.num)

    def __lt__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den < other.num / other.den)

    def __le__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den <= other.num / other.den)

    def __eq__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den == other.num / other.den)

    def __ne__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den != other.num / other.den)

    def __gt__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den > other.num / other.den)

    def __ge__(self, other):
        other = self.__check(other)
        return bool(self.num / self.den >= other.num / other.den)

    def __radd__(self, other):
        return self.__check(other) + self

    def __rsub__(self, other):
        return self.__check(other) - self

    def __rmul__(self, other):
        return self.__check(other) * self

    def __rtruediv__(self, other):
        return self.__check(other) / self