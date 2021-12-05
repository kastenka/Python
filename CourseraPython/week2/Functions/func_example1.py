# Функция - блок кода, который можно переиспользовать несколько раз. Можно вызывать с каким-то аргументами
# и получать(возвращать) значения обратно
from datetime import datetime


def get_seconds():  # название по PEP8
    """Return current seconds"""  # документационная строка - описывает, что происходит в функции
    return datetime.now().ctime()  # возвращаем значение из функции, если не писать return - вернётся None


seconds = get_seconds()  # для вызова функции нужно использовать () и если нужно передать туда параметры
print(get_seconds())

print(get_seconds.__doc__)  # получить документационную строку
print(get_seconds.__name__)  # получить имя функции