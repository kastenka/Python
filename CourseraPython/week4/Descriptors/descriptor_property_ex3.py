# Декоратор property позволяет использовать функцию как атрибут класса
# property реализовано с помощью дескрипторов, тк разное поведение в зависимости от того, как вызывается объект


# Можем написать свой класс property, который будет эмулировать поведение стандартного property
class Property:
    def __init__(self, getter):
        self.getter = getter  # нужно сохранить функцию, которую получает property, тк property - декоратор

    def __get__(self, obj, obj_type=None):
        if obj is None:  # когда обращаемся к объекту, и если он вызван от класса, мы просто возвращаем самого себя
            return self

        return self.getter(obj)  # а если вызван атрибут с объектом, то возвращаем соотв. getter, вызываем функцию


# Можем определить класс и использовать, как стандартный декоратор @property, так и только что созданный @Property
# будут работать идентично, тк property реализован с помощью дескриптора
class Class:
    @property
    def original(self):
        return "original"

    # можем использовать @Property как декоратор с помощью синтаксического сахара
    @Property
    def custom_sugar(self):
        return "custom sugar"

    def custom_pure(self):
        return "custom pure"

    # можем использовать @Property как вызов функции
    custom_pure = Property(custom_pure)



