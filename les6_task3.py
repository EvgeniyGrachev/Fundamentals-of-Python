class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


income = {'wage': float(input('Введите оклад: ')), 'bonus': float(input('Введите премию: '))}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return income.get('wage') + income.get('bonus')


a = Position('Ivan', 'Ivanov', 'Engineer', income)
print(f'ФИО - {a.get_full_name()}')
print(f'ЗП - {a.get_total_income()}')
