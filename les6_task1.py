from time import sleep


class TrafficLight:
    __color1 = 'red'
    __color2 = 'yellow'
    __color3 = 'green'

    def running(self):
        while True:
            print("\033[31m {}".format(self.__color1))
            sleep(7)
            print("\033[33m {}".format(self.__color2))
            sleep(2)
            print("\033[32m {}".format(self.__color3))
            sleep(7)
            print("\033[33m {}".format(self.__color2))
            sleep(2)
            print("\033[31m {}".format(self.__color1))
            sleep(7)
            el = input("\033[37m {}".format('Хотите продолжить, введите - да, если нет, то нажмите Enter: '))
            if el == '':
                break


a = TrafficLight()
print(a.running())
