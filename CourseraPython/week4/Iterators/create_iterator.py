# Итератор - какой-то объект, по которому вы можете бежать, те итерироваться
# Можно реализовать свой собственный итератор, написав класс с соответствующими магическими методами __iter__, __next__


class SquareIterator:
    """Аналог функции range, только возвращает квадраты чисел"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # метод __iter__ должен возвращать итератор в себя
    def __iter__(self):
        return self

    # метод __next__ определяет, какие элементы возвращаются из итератора при итерации
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # исключение, которое говорит протоколу итерации, что итерация должна закончиться

        # возводим число в квадрат и инкрементируем счетчик
        result = self.current ** 2
        self.current += 1
        return result


for num in SquareIterator(1, 4):
    print(num)

