list1 = [9, 7, 7, 5, 5, 5, 3, 1]
print(list1)
new_num = int(input('Привет! Введите новый элемент, в виде натурального числа: '))
i = 0
for n in list1:
    if new_num <= n:
        i += 1
list1.insert(i, new_num)
print(list1)
