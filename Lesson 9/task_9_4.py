class Car:

    def __init__(self, name, color, speed, is_police=bool):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.police = is_police

    def go(self):
        return f'Машина {self.name} цвета {self.color} начала движение'

    def stop(self):
        return f'Машина {self.name} цвета {self.color} закончила движение'

    def turn(self, direction):
        return f'Машина {self.name} цвета {self.color} повернула на {direction}'

    def show_speed(self):
        return f'Машина {self.name} цвета {self.color} движется со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.police and self.speed > 60.0:
            return f'скорость городского транспорта превышена {self.speed}'
        else:
            return f'ДАВИ НА ГАЗ!'


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.police and self.speed > 40.0:
            return f'скорость рабочего транспорта превышена {self.speed}'
        else:
            return f'ДАВИ НА ГАЗ!'


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


town_car = TownCar("Трактор", "Зеленый", 61.5)
sport_car = SportCar("Трактор", "Красный", 80.0)
work_car = WorkCar("Трактор", "Желтый", 44, True)
police_car = PoliceCar("Трактор", "Синий", 999.99)
work_car_1 = WorkCar("Трактор", "Грязный", 44, False)

print(town_car.go())
print(town_car.turn("на лево"))
print(sport_car.turn("на право"))
print(work_car.show_speed())
print(town_car.show_speed())
print(work_car_1.show_speed())
print(town_car.show_speed())
