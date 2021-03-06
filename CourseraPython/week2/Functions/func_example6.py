# Аргументы по умолчанию
# Существует возможность использовать аргументы по умолчанию в функции - можно не передавать какие-то аргументы

def greeting(name="It\'s me..."):
    print("Hello, {}".format(name))

# вывод дефолтной фразы, тк не передан аргумент
greeting()  # Hello, It's me...


"""Нужно быть внимательными с аргументами по умолчанию, если мы используем в качестве аргументов по умолчанию
изменяемые значения - тк при определении функции интерпретатор Python бежит по файлу с кодом, определяется
связь между именем функции и дефолтными значениями - у каждой функции появляется словарь с дефолтными значениями, и 
именно в эти переменные каждый раз происходит запись.
Если дефолтные значения являются изменяемыми, то в них можно записывать - это обычные переменные.
Поэтому лучше дефолтные значения определять как None"""


def append_one(iterable=[]):
    iterable.append(1)
    return iterable


# если не передан параметр, то создаем список на лету, чтобы не было ошибки
def function(iterable=None):
    if iterable is None:
        iterable = []
    # или iterable = iterable or []


print(append_one([1]))  # [1, 1]


# если вызываем 2 раза
print(append_one())  # [1]
print(append_one())  # [1, 1]
print(append_one.__defaults__)







