print('Привет! Введите два числа и получите возведение первого числа в степень другого.')


def my_func(x, y):
    return x ** y


try:
    x = int(input('Введите целое положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    if int(x) > 0 and int(y) < 0:
        print(my_func(x, y))
    else:
        print('Не соблюдены условия ввода данных')
except ValueError:
    print('Ввенено не число')
