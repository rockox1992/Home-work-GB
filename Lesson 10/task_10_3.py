class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return f'{self.number + other.number} ячеек в новой клетке'

    def __sub__(self, other):
        if self.number < other.number:
            return f'1 клетка меньше 2 клетки'
        else:
            return f'{self.number - other.number} ячеек в новой клетке'

    def __mul__(self, other):
        return f'{self.number * other.number} ячеек в новой клетке'

    def __floordiv__(self, other):
        return f'{self.number // other.number} ячеек в новой клетке'

    def __truediv__(self, other):
        return f'{self.number / other.number} ячеек в новой клетке'

    def make_order(self, num_row):
        n_1 = self.number // int(num_row)
        n_2 = self.number % int(num_row)
        if n_2 == 0:
            return ''.join({((num_row * "*") + "/n") * (n_1 - 1)}) + ''.join({(num_row * "*")})
        else:
            return ''.join({((num_row * "*") + "/n") * n_1}) + ''.join({(n_2 * "*")})


a = Cell(13)
b = Cell(9)
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a // b)
print(a / b)
print(a.make_order(10))
print()
print(b.make_order(3))

