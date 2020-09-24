class Data:
    def __init__(self, string_date: str):
        self.raw = string_date
        self.date = self.extract(self.raw)

    @classmethod
    def extract(cls, raw_str):
        if cls.validation(raw_str)[0]:
            return list(map(int, raw_str.split('-')))
        else:
            return cls.extract('01-01-0001')

    @staticmethod
    def validation(str_date: str):
        temp = str_date.split('-')
        try:
            day = int(temp[0])
            month = int(temp[1])
            year = int(temp[2])
        except (ValueError, IndexError):
            return f'Неверный формат ввода "dd-mm-yyyy" для "{str_date}"'
        else:
            if not 1 <= day <= 31:
                return f'Неверно введена дата: {day}, для {str_date}'
            if not 1 <= month <= 12:
                return f'Неверно введен месяц: {month}, для {str_date}'
            if not 1900 <= year <= 2020:
                return f'Неверно введен год {year}, для {str_date}'
        return str_date

    def __str__(self):
        return f'{self.date[0]:0=2}-{self.date[1]:0=2}-{self.date[2]:0=4}'


data_1 = Data('22-09-2020')
print(data_1)

print(Data.extract('22-09-2020'))
print(Data.validation('22-09-2020'))
print(Data.validation('22-16-2020'))
