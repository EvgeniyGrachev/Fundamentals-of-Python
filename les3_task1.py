print('Привет!')


def my_division(num_1, num_2):
    return num_1 / num_2


try:
    num_1 = input('Для выполнения деления, введите любое первое число: ')
    num_2 = input('Введите второе число, отличное от 0: ')
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(f'Результат деления - {my_division(num_1, num_2)}')
except ZeroDivisionError:
    print('Второе число равно 0')
except (NameError, ValueError):
    print('Ввенено не число')
