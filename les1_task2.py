print('Привет!')

num = int(input('Введите количество секунд и узнаете, сколько это будет в часах и мутутах:'))

print(f'{num // 3600:02}:{(num % 3600) // 60:02}:{(num % 3600) % 60:02}')
