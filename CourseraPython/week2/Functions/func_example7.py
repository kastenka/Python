# Возможность определения функции, которая принимает разные количества аргументов

def printer(*args):
    print(type(args))  # все аргументы записываются в tuple args - <class 'tuple'>
    for argument in args:
        print(argument)


printer(1, 2, 3, 4)


# можно разворачивать список в аргументах
name_list = ["Masha", "Veronika", "Vika"]
printer(name_list)  # как один аргумент для функции ['Masha', 'Veronika', 'Vika']
printer(*name_list)  # развернули список - несколько аргументов


# так же работает со словарями - функция принимает разное количество именованных аргументов
def printer2(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))


printer2(a=10, b=11)

# можно разворачивать словарь в аргментах
payload = {
    "user_id": 17,
    "feedback": {
        "subject": "Registration fields",
        "message": "There is no country for old men"
    }
}
printer2(**payload)  # передаем значения в функцию из словаря как именованные аргументы
