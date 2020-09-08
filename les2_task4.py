st = input('Привет! Введите строку из нескольких слов, разделённых пробелами: ').split()

for i, w in enumerate(st, 1):
    print(f'{i} - {w[:10]}')
