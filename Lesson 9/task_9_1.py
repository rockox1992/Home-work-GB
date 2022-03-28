import time


class TrafficLight:
    __colors = ["Red", "Yellow", "Green"]

    def __init__(self, colors):
        self.color = colors.capitalize()

    def running(self, green_time=1):
        while True:
            if self.color == self.__colors[0]:
                print(self.color)
                time.sleep(7)
                self.color = self.__colors[1]
            elif self.color == self.__colors[1]:
                print(self.color)
                time.sleep(2)
                self.color = self.__colors[2]
            elif self.color == self.__colors[2]:
                print(self.color)
                time.sleep(green_time)
                self.color = self.__colors[0]


traffic_light = TrafficLight("YelloW")  # c какого цвета стартует светофор
traffic_light.running(3)  # Время работы Green
