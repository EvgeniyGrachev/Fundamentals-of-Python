counter = 0
with open('my_text_2.txt', 'r', encoding='utf-8') as my_text_2:
    for line in my_text_2:
        counter += 1
        print(line, 'слов в строке: ', len(line.split()))
    print('Всего строк:', counter)
