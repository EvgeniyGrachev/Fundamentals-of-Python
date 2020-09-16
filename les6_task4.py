from random import choice
list_choice = ['Север', 'Северо-Запад', 'Северо-Восток', 'Юг', 'Юго-Восток', 'Юго-Запад', 'Восток', 'Запад']


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name}, "{self.color}" поехала со скоростью {self.speed} км/ч!'

    def turn(self):
        return f'Машина {self.name}, "{self.color}" повернула на - {choice(list_choice)}!'

    def show_speed(self, show_speed):
        return f'Текщая скорость {self.name}, "{self.color}" - {show_speed} км/ч!'

    def stop(self):
        return f'Машина {self.name}, "{self.color}" остановилась!'


class TownCar(Car):
    def show_speed(self, show_speed):
        if show_speed <= 60:
            return f'Текщая скорость {self.name}, "{self.color}" - {show_speed} км/ч!'
        else:
            return f'Текщая скорость {self.name}, "{self.color} - {show_speed} км/ч, что превышает допустимую на - \
{show_speed - 60} км/ч!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self, show_speed):
        if show_speed <= 40:
            return f'Текщая скорость {self.name}, "{self.color}" - {show_speed} км/ч!'
        else:
            return f'Текщая скорость {self.name}, "{self.color} - {show_speed} км/ч, что превышает допустимую на - \
{show_speed - 60} км/ч!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


TC = TownCar(10, 'Blue', 'Mazda')
print(TC.go())
print(TC.turn())
print(TC.show_speed(70))
print(TC.stop())
print()
SP = SportCar(20, 'Red', 'GTA')
print(SP.go())
print(SP.turn())
print(SP.show_speed(170))
print(SP.stop())
print()
WC = WorkCar(5, 'Orange', 'Kamaz')
print(WC.go())
print(WC.turn())
print(WC.show_speed(60))
print(WC.stop())
print()
PC = PoliceCar(50, 'Black', 'Lamborghin')
print(PC.go())
print(PC.turn())
print(PC.show_speed(190))
print(PC.stop())
