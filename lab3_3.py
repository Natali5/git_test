import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Perimetr(self):
        return self.a + self.b + self.c

    def Square(self):
        return (self.a * self.b) / 2

    def Information(self):
        return "Perimetr: {}; Square: {}; a: {}; b: {}; c: {};".format(self.Perimetr(), self.Square(), self.a, self.b, self.c)


class Quadrangle(Triangle):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def Square(self):
        up = 4 * self.e ** 2 * self.f ** 2 - (self.b ** 2 + self.d ** 2 - self.a ** 2 - self.c ** 2)
        bottom = 16
        return math.sqrt(up ** 2 / bottom)

    def Perimetr(self):
        return self.a + self.b + self.c + self.d

    def Information(self):
        return "Perimetr: {}; Square: {}; a: {}; b: {}; c: {}; d: {}; e: {}; f: {};".\
            format(self.Perimetr(), self.Square(), self.a, self.b, self.c, self.d, self.e, self.f)


triangle = Triangle(4, 5, 12)
print triangle.Information()

quadrangle = Quadrangle(4, 5, 3, 6, 3, 4)
print quadrangle.Information()
