print('Привет! Введите ваши данные: ')


def my_data(**kwargs):
    return kwargs


print(my_data(Имя=input('Имя: '), Фамилия=input('Фамилия: '), Год_рождения=input('Год рождения: '),
              Город_проживания=input('Город проживания: '), Email=input('Email: '), Телефон=input('Телефон: ')))
