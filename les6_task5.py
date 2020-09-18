class Stationery:
    def __init__(self, title):
        self.title = title  # указать как будет рисовать предмет

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Ручка начинает рисовать {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Карандаш начинает рисовать {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Маркер начинает рисовать {self.title}'


pen_1 = Pen('тонко')
print(pen_1.draw())

print()
pencil_1 = Pencil('бледно')
print(pencil_1.draw())

print()
handle_1 = Handle('жирно')
print(handle_1.draw())
