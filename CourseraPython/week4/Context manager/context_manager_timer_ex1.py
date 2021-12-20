# Написать контекстный менеджер, который считает и выводит время, проведенной внутри него
import time


class timer:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return

    def __exit__(self, *args):
        exit_time = time.time()
        print("Elapsed: {}". format(exit_time - self.start_time))


with timer():
    time.sleep(1)