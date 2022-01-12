# Декоратор property позволяет использовать функцию как атрибут класса
# property реализовано с помощью дескрипторов, тк разное поведение в зависимости от того, как вызывается объект


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # определяем property full_name, которое хоть и является функцией, которая возвращает строчку, используется потом
    # так же, как и обычный атрибут (те без вызова скобочек)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


amy = User("Amy", "Jones")

# property full_name используется как обычный атрибут (те без вызова скобочек)
print(amy.full_name)  # вызывается full_name, если обращаемся от объекта класса, - Amy Jones
print(User.full_name)  # если попытается обратиться от класса, получится <property object at 0x00000227C9CC8630>