# Абстрактные методы обязаны переопределять в классе, который наследутеся от класс с таким методом
# Абстрактные методы можно использовать с помощью стандартной бибиотеки abc

from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):

    # @abstractmethod говорит о том, что не получится создать какой-то класс, не определив этот метод
    @abstractmethod
    def send(self):
        """Do something"""


class Child(Sender):
    pass


class AnotherChild(Sender):
     def send(self):
         print("Sending")


# абстрактные методы используются редко, обычно вызывается исключение NotImplementedError, которое говорит о том, что
# этот метод нужно реализовать
class PythoWay:
     def send(self):
         raise NotImplementedError


AnotherChild()  # все ок
Child()  # TypeError: Can't instantiate abstract class Child with abstract method send

