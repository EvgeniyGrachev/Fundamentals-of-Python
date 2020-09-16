with open('text_6.txt', 'r', encoding='utf-8') as text_6:
    for el in text_6.readlines():
        res1 = ''.join((i if i in '0123456789' else ' ') for i in el)
        res2 = [int(1) for i in res1.split()]
        print(f'{el.split()[0]} {sum(res2)}')
