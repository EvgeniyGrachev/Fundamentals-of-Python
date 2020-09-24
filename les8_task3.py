class MyError(Exception):
    list_1 = []

    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def check(value):
        try:
            value = float(value)
            MyError.list_1.append(value)
        except ValueError:
            raise MyError(f'Введено не число')

    @staticmethod
    def ml():
        print('Введите число, для выхода введите "#"')
        while True:
            try:
                temp = input('Следующее число: ')
                if not temp.lower() == '#':
                    MyError.check(temp)
                else:
                    break
            except MyError as e:
                print(e.txt)

    @classmethod
    def get_list(cls):
        return cls.list_1


MyError.ml()
print(MyError.get_list())
