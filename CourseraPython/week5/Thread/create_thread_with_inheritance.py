"""Потоки. Поток напоминает процесс. У потока своя последовательность инструкций для исполнения. Каждый поток имеет
собственный стек. Все потоки выполняются в рамках процесса(этим они и отличаются, если мы говорили о процессах и у
каждого процесса были свои ресурсы и память, то все созданные потоки разделяют память и ресурсы процесса). Управелнем
выполнением потоков занимается ОС. Потоки в Python имеют свои ограничения для потоков.
"""

# Создание потока на Python. Существует альтернативный способ создания потока при помощи наследования
from threading import Thread


# объявляем свой класс
class PrintThread(Thread):  # наследуемся от класса Thread

    # передаем в конструктор нужные аргументы, для того чтобы выполнить функцию в отдельном потоке
    def __init__(self, name):
        super().__init__()
        self.name = name  # запоминаем аргументы в self

    # переопределяем метод run, который будет выполнен уже в отдельном потоке управления
    def run(self):
        # можем использовать переданные аргументы конструктору, которые запомнили в self
        print("Hello", self.name)


# создаем объект класса PrintThread, передаем туда нужные аргументы
th = PrintThread("Mike")

# метод start создаст поток
th.start()

# при помощи join будет ждать, пока этот поток завершится в основном потоке
th.join()
