# Написать контекстный менеджер, который считает и выводит время, проведенной внутри него
import time


class timer:
    def __init__(self):
        self.start_time = time.time()

    def current_time(self):
        return time.time() - self.start_time

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("Elapsed: {}". format(self.current_time()))


with timer() as t:
    time.sleep(1)
    print("Current: {}".format(t.current_time()))
    time.sleep(1)