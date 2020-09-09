list1 = [5, 6, 6, 12, 25, 6, 6, 5, 66, 88, 2, 12, 5, 16]
list2 = [el for el in list1 if list1.count(el) == 1]

print(list1)
print(list2)
