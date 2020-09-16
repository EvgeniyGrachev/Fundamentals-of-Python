with open('text_3.txt', 'r', encoding='utf-8') as text_3:
    sum1 = []
    less = []
    line = text_3.read().split('\n')
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        sum1.append(i[1])

print(f'ЗП меньше 20 000 руб. у: {less}. Средняя ЗП - {sum(map(float, sum1)) / len(sum1)} руб.')
