class MyError (Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input('Введите любое число: ')
num_2 = input('Введите число, отличное от нуля: ')

try:
    num_1, num_2 = float(num_1), float(num_2)
    if num_2 == 0:
        raise MyError('Второе введённое число равно нулю. На ноль дельть нельзя!!!')
except ValueError:
    print('Введено не число')
except (ZeroDivisionError, MyError) as err:
    print(err)
else:
    print(f'Введены верные числа, результат деления - {num_1 / num_2: .2f}')
