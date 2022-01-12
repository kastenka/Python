# Синхронизация потоков, условные переменные
import threading


class Queue(object):
    """Класс очередь, с которым нужно работать в большом количестве потоков"""
    def __init__(self, size=5):
        self._size = size  # размер очереди
        self._queue = []
        self._mutex = threading.RLock()

        # условные переменные в конструктор получает объект блокировки, если переменные взаимозависимые - нужно
        # использовать обшую блокировку
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    # При помощи условных перменных удобно ожидать событий при помощи wait() и оповещать все потоки, которые сейчас
    # ждут наступления этого события
    def put(self, val):
        with self._full:
            # Очередь не должна расти больше заданного размера
            while len(self._queue) > self._size:
                self._full.wait()  # ждать, пока количество элементов в очереди не уменьшится (неизвестно сколько)

            self._queue.append(val)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            ret = self._queue.pop(0)


