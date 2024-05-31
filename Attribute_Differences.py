# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
# созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


class Buiding:

    total = []

    def __init__(self, count):
        self.count = count
        print(f'Число создаваемых объектов {self.count}:')

    def counter(self):
        for i in range(1, self.count+1):
            Buiding.total.append(i)

        print(Buiding.total)

h1 = Buiding(40)
h1.counter()

