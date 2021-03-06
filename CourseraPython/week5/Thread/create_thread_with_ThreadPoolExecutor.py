"""Потоки. Поток напоминает процесс. У потока своя последовательность инструкций для исполнения. Каждый поток имеет
собственный стек. Все потоки выполняются в рамках процесса(этим они и отличаются, если мы говорили о процессах и у
каждого процесса были свои ресурсы и память, то все созданные потоки разделяют память и ресурсы процесса). Управелнем
выполнением потоков занимается ОС. Потоки в Python имеют свои ограничения для потоков.
"""

# Создание потока на Python.
# В Python3 появился удобный класс ThreadPoolExecutor для создания пула потоков модуля concurrent.futures.Future
from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


"""Предположим:Есть массив чисел и нам нужно ограничить количество потоков и рассчитать квадраты чисел для этого массива
Используем контекстный менеджер, указываем в нем вызов ThredPoolExecutor c параметром max_workers, который отвечает
за максимальное количество потоков, которые будут созданы в этом блоке with
Не нужно заботиться о завершении потоков, нужное количество потоков будет создано автоматически и при завершении
контекстного менеджера будет вызвана функция shutdown(), которая дождется завершения всех созданных потоков"""

with ThreadPoolExecutor(max_workers=3) as pool:

    # метод submit создает объект класса concurrent.futures.Future - это такой объект, который еще не завершился, но
    # выполняется и будет завершен в будущем
    results = [pool.submit(f, i) for i in range(10)]

    # при помощи метода as_completed() можем дождаться завершения всех наших объектов и получить результат по мере
    # завершения всех этих потоков, созданных Executor
    for future in as_completed(results):
        print(future.result())