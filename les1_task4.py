print('Привет!')

num = int(input('Введите целое положительное число и узнаете наибольшую цифру в этом цисле:'))
num_max = num % 10
num_p = num

while num_p > 0:
    num_tek = num_p % 10
    if num_tek > num_max:
        num_max = num_tek
        if num_max == 9:
            break
    num_p = num_p // 10

print(f'Наибольшая цифра в числе {num} - {num_max}')
