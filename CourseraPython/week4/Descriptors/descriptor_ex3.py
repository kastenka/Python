# Написать дескриптор, который пишет в файл все присваиваемые ему значения


class ImportantValue:

    def __init__(self, amount):
        self.amount = amount

    # метод __get__ принимаем объект, с которым вызван дескриптор, и его тип
    def __get__(self, obj, obj_type):
        return self.amount

    # принимает объект и значение, которое надо присвоить
    def __set__(self, obj, value):
        # логирование изменений
        with open("log.txt", "a") as file:
            file.write(str(value))

        self.amount = value


class Account:
    """Класс, с какой-то важной информацией"""
    amount = ImportantValue(100)


bobs_account = Account()

# залогируется все в файл
bobs_account.amount = 200
bobs_account.amount = 300

