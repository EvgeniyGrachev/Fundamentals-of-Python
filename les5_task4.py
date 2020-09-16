rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_444.txt', 'a', encoding='utf-8') as text_444:
    with open('text_4.txt', 'r', encoding='utf-8') as text_4:
        for i in text_4.read().split('\n'):
            i = i.split(' - ')
            text_444.writelines(rus[i[0]] + ' - ' + i[1] + '\n')
