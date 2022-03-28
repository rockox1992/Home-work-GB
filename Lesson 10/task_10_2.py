from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param, cost):
        self.param = param
        self.cost = cost

    def __add__(self, other):
        return f'Сумма:{round((self.cost * (self.param / 6.5 + 0.5)) + (other.cost * (2 * other.param + 0.3)), 4)}'

    @abstractmethod
    def abstract(self):
        return 'abstract'


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {round((self.param / 6.5 + 0.5), 4)} ткани'

    def abstract(self):
        return 'abstract coat'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {round((2 * self.param + 0.3), 4)} ткани'

    def abstract(self):
        return 'abstract costume'


coat = Coat(777, 3)
costume = Costume(555, 2)
print(coat.abstract())
print(coat.consumption)
print(costume.consumption)
print(coat + costume)
