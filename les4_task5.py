from functools import reduce

list1 = [el for el in range(100, 1001) if el % 2 == 0]
print(list1)


def func1(el1, el2):
    return el1 * el2


print(f'Произведение всех чётных чисел (очень страшное число) - {reduce(func1, list1)}')
