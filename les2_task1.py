list1 = [58, 21.5, "str", (1 + 6j), (1, 5, 6), [8, 9, 7], {15, 57, 18}, False, None]

for el, it in enumerate(list1, 1):
    print(f'{el} {it} - {type(it)}')
