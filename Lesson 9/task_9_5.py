class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Канц. товары")


class Pen(Stationery):
    def draw(self):
        print(f"Ручка шариковая {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш НН {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Маркер для CD {self.title}")


stationery = Stationery("")
pen = Pen("Синяя")
pencil = Pencil("Механический")
handle = Handle("Красный")
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
