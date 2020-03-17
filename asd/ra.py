class prev:
    x,y,result =0,0,0

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,x,y):
        self.result = x + y
        return self.result
    def mul(self,x,y):
        self.result = x * y
