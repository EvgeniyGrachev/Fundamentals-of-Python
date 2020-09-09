list1 = [2, 25, 89, 5, 78, 5, 6, 4, 88, 2, 8, 4, 56]

list2 = [el for el in list1[1:] if el > list1[list1.index(el) - 1]]

print(list1)
print(list2)
