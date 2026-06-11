class Ali127:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def determinant_2x2(self):
        result = (self.a * self.d) - (self.b * self.c)
        return result 
