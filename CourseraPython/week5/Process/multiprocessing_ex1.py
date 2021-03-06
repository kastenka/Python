# Процессы. Обычно используют модуль multiprocessing для создания процессов
"""Не во всех системах есть системный вызов fork, поэтому нужно использовать multiprocessing для создания собственных
дочерних объектов - Не в каждой системе есть системный вызов fork, поэтому в multiprocessing все сделано за нас"""

from multiprocessing import Process  # чтобы запустить процесс на Python нужно импортировать Process из multiprocessing


def f(name):
    print("Hello", name)


if __name__ == '__main__':
    # передаем в конструктор функцию, которую хотим исполнить в отдельном дочернем процессе и аргументы этой функции
    p = Process(target=f, args=("Bob",))  # после того, как создали объект, никакого процесса создано не будет

    # будет вызван(создан) процесс после вызова метода start() нашего объекта, внутри start будет вызван системный
    # вызов fork и исполнена функция f в отдельном процессе
    p.start()

    # Важно ожидать завершения всех созданных дочерних процессов, можно использовать для этого join
    # Метод join блокирует выполнение главного процесса пока не завершится дочерний процесс. без метода join главный
    # процесс не будет ждать завершения дочернего процесса
    p.join()  # вызывается метод wait
