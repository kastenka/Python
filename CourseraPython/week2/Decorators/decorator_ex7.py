# Применим несколько декораторов
# Можно создавать цепочки из декораторов, определяя сразу несколько декораторов друг за другом

def first_decorator(func):
    def wrapped():
        print("Inside first decorator")
        return func()  # вызывается second_decorator
    return wrapped


def second_decorator(func):
    def wrapped():
        print("Inside second decorator")
        return func()  # вызывает decorated
    return wrapped


@first_decorator
@second_decorator
def decorated():
    print("Finally called")


# в начале, при применении декораторов, вызывается функция second_decorator, которая возвращает новую функцию wrapped,
# те подменяется функция wrapped внутри second_decorator ->
# вызывается first_decorator, который принимает функцию полученную из second_decorator'a wrapped и возвращает еще одну
# функцию wrapped, заменяя decorated на нее
decorated()

decorated = first_decorator(second_decorator(decorated))



