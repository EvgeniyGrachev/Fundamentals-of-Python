from sys import argv

name_file, hours_worked, rate_per_hour, bonus = argv

print('Количество отработанных часов: ', hours_worked)
print('Ставка за 1 час: ', rate_per_hour)
print('Премия: ', bonus)

try:
    hours_worked = float(hours_worked)
    rate_per_hour = float(rate_per_hour)
    bonus = float(bonus)
    print(f'ЗП ставила - {(hours_worked * rate_per_hour) + bonus:.2f} руб.')
except TypeError:
    print('Введено не число')
except ValueError:
    print('Введено не верное количество значений')
