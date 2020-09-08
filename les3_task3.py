print('Привет! Введите 3 целых числа и получите сумму двух наибольших чисел: ')


def my_func(a_1, a_2, a_3):
    return sum((a_1, a_2, a_3)) - min(a_1, a_2, a_3)


a_1 = input('Введите первое число: ')
a_2 = input('Введите второе число: ')
a_3 = input('Введите третье число: ')

try:
    a_1 = int(a_1) or float(a_1)
    a_2 = int(a_2) or float(a_2)
    a_3 = int(a_3) or float(a_2)
    print(f'Cумма двух наибольших чисел - {my_func(a_1, a_2, a_3)}')
except (NameError, ValueError):
    print('Ввенено целое не число')
