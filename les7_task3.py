class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f'Сумма ячеек двух клеток равна - {self.num + other.num}'

    def __sub__(self, other):
        if self.num - other.num > 0:
            return f'Вычитание ячеек двух клеток равно - {self.num - other.num}'
        else:
            return 'Вычитание не возможно, в первой клетке меньше ячеек, чем во второй'

    def __mul__(self, other):
        return f'Умножение ячеек двух клеток равно - {self.num * other.num}'

    def __floordiv__(self, other):
        if self.num // other.num > 0:
            return f'Деление ячеек двух клеток равно - {self.num  // other.num}'
        else:
            return 'Деление не возможно, в первой клетке меньше ячеек, чем во второй'

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.num // row)]) + '\n' + '*' * (self.num % row)


cell_a = Cell(25)
cell_b = Cell(15)
print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a * cell_b)
print(cell_a // cell_b)
print(cell_a.make_order(6))
print(cell_b.make_order(4))
