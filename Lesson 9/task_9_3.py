class Worker:
    _income = {"wage": "на хлебушек", "bonus": "с маслом"}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'Сотрудник: {self.surname} {self.name},'

    def get_total_income(self):
        return f'на должности: {self.position}, получает {self._income["wage"]} {self._income["bonus"]}'


cry = Position("Иван", "Удальцов", "игрец на дуде")
print(cry.get_full_name(), cry.get_total_income())

