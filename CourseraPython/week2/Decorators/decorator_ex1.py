# Декоратор - функция, которая принимает функцию и возвращает функцию

def decorator(func):
    return func


# cинтаксис применения декораторов с использование @name_of_decorator - это синтаксический сахар
@decorator
def decorated():
    print("Hello")


# так же, можно не использовать @decorator, а вызвать декоратор, которому передаётся функция, записывается все
# в функцию, которую декорируем:
decorated = decorator(decorated)
decorated()  # Hello


