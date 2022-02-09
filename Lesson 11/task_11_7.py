class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b < 0:
            return f'Сумма равна: {self.a + other.a} - {abs(self.b + other.b)}i'
        else:
            return f'Сумма равна: {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        if self.b * other.a < 0:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)} - {abs(self.b * other.a)}i'
        else:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'


c_1 = ComplexNumber(4, 8)
c_2 = ComplexNumber(6, 11)
c_3 = ComplexNumber(-6, 11)
c_4 = ComplexNumber(-5, 13)
print(c_1 + c_2)
print(c_1 * c_2)
print(c_3 + c_4)
print(c_3 * c_4)
