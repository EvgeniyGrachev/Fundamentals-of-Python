from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print(f'{size} - не верное заначение, минимальное заначение - 40')
            self.__size = 40
        elif size > 58:
            print(f'{size} - не верное заначение, максимальное заначение - 58')
            self.__size = 58
        else:
            self.__size = size

    @property
    def calculation(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            print(f'{height} - не верное заначение, минимальное заначение - 150 см')
            self.__height = 150
        elif height > 220:
            print(f'{height} - не верное заначение, максимальное заначение - 220 см')
            self.__height = 220
        else:
            self.__height = height

    @property
    def calculation(self):
        return 2 * self.__height / 100 + 0.3


coat1 = Coat(int(input('Введите размер пальто от 40 до 58: ')))
print(f'Для пальто {coat1.size} размера потребуется{coat1.calculation: .2f} метров ткани')
costume1 = Costume(int(input('Введите рост для костюма от 150 см до 220 см: ')))
print(f'Для костюма ростом {costume1.height} см потребуется{costume1.calculation: .2f} метров ткани')
print(f'Всего на пальто и костюм потребуется {coat1 + costume1: .2f} метров ткани')
