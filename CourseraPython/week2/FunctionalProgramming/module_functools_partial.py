# Модуль functools позволяет использовать функциональные особенности Python
from functools import partial


def greeter(person, greeting):
    return "{}, {}!".format(greeting, person)


# partial позволяет модифицировать поведение функций - принимает функцию и какой-то параметр, который нужно подменить
# можем определить новый набор функций, подменив по умолчанию определенные параметры

# создаем функцию hier, которая всегда будет приветствовать с Hi
hier = partial(greeter, greeting="Hi")  # стала функция, которая принимает только person
print(hier)  # functools.partial(<function greeter at 0x000001A3B4CBF0D0>, greeting='Hi')

helloer = partial(greeter, greeting="Hello")
print(helloer)  # functools.partial(<function greeter at 0x000001A3B4CBF0D0>, greeting='Hi')

print(hier("brother"))
print(helloer("sister"))