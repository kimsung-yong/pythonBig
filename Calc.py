import asdf.Calc2


class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.calc2 = asdf.Calc2.Calc2(x, y)

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.calc2.mul()


ca = Calc(3, 2)
print(ca.mul())
