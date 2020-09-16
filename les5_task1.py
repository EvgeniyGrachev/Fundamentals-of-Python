with open("my_text_1.txt", "w", encoding="utf-8") as my_text_1:
    while True:
        el = input('Введите значение: ')
        print(f'{el}', file=my_text_1)
        if el == '':
            break
