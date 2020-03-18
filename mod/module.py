class mode:
    modeS, modeA, modeM, modeMul = 0, 0, 0, 0

    def sum(self, a, b):
        self.modeS += 1
        if type(a) != type(b):
            return print("타입이 맞지 않습니다.")
        else:
            return a + b

    def agv(self, a, b):
        self.modeA += 1
        if type(a) != type(b):
            return print("타입이 맞지 않습니다.")
        else:
            return a / b

    def subtract(self, a, b):
        self.modeM += 1
        if type(a) != type(b):
            return print("타입이 맞지 않습니다.")
        else:
            return a - b

    def mul(self, a, b):
        self.modeMul += 1
        if type(a) != type(b):
            return print("타입이 맞지 않습니다.")
        else:
            return a * b

    def showCount(self):
        s = print("덧셈 : %s \n" % self.modeS +
              "뺄셈 : %s \n" % self.modeM +
              "곱셈 : % s \n" % self.modeMul +
              "나눗셈 : % s \n" % self.modeA)
        return s
