# Контекстные менеджеры позволяют определить поведение, происходящее в начале и в конце блока исполнения, блока with
# используются при работе с файлами, соединениями, транзакциями

# Конекстные менеджеры позволяют управлять исключениями, которые произошли внутри блока. Можем эти исключения
# обрабатывать и определять какое-то поведение
# такой контекстный менеджер уже есть в стандартной библиотеке contextlib
class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type  # записываем exc_type и потом будем проверять, произошло это исключение или другое

    def __enter__(self):
        return  # не важно, что возвращается, могли написать pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print("Nothing happend")
            return True


with suppress_exception(ZeroDivisionError):
    number = 1 / 0  # Nothing happend

# вернется исключение, тк в блоке произошло исключение ZeroDivisionError, а было передано другое, ValueError
with suppress_exception(ValueError):
    number = 1 / 0  # ZeroDivisionError: division by zero