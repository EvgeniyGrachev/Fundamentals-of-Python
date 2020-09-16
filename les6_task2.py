class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Длинна дороги - {length} м, ширина дороги - {width} м')

    def res(self):
        return f'Масса требуемого асфальта - {self._length * self._width * 25 * 5 / 1000} т'


a = Road(2000, 10)
print(a.res())
