from datetime import date


class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def number_int(cls, data):
        try:
            cls.data = data
            numbers = list(map(int, data.split("-")))
            return numbers[0], numbers[1], numbers[2]
        except IndexError:
            return "The date is not correct! Enter as in the example: (23-12-2007)"

    @staticmethod
    def valid_digit(data):
        try:
            numbers = list(map(int, data.split("-")))
            return date(numbers[-1], numbers[-2], numbers[-3])
        except ValueError:
            return "The date is not correct! Enter as in the example: (23-12-2007)"


print(Date.number_int("12-2025"))
print(Date.number_int("09-05-2022"))
print(Date.valid_digit("09--2022"))
print(Date.valid_digit("09-05-2022"))
print(Date("09-05-2022"))
