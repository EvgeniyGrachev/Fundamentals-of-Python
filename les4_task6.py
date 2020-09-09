from itertools import count, cycle

for el in count(10):
    if el > 20:
        break
    else:
        print(el)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0
for el in cycle(list1):
    if n > 10:
        break
    print(el)
    n += 1
