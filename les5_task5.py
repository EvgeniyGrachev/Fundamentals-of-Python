from random import randint

with open('my_text_5.txt', 'w+', encoding='utf-8') as my_text_5:
    my_text_5.write(' '.join([str(randint(1, 100)) for _ in range(1000)]))
    my_text_5.seek(0)
    print(sum(map(int, my_text_5.readline().split())))
