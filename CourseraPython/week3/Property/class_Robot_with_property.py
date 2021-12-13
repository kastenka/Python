# Методы. Часть 2
# Вычисляемые свойства класса(property)

class Robot:

    def __init__(self, power):
        self._power = power  # тк _power, то значит является приватным атрибутом

    # power является объектом property - встроенный объект
    power = property()

    # у property есть три метода: setter, getter, deleter - их можно переопределить, чтобы менять поведение и выполнять
    # какие-то действия при обращении к атрибуту, присваивания ему нового значения или удаления атрибута
    @power.setter  # будет выполняться, когда будем менять атрибут экземпляра power
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter  # будет выполняться, когда будем читать атрибут экземпляра power
    def power(self):
        return self._power

    @power.deleter  # будет выполняться при удалении атрибута power
    def power(self):
        print("Make robot useless")
        del self._power


wall_e = Robot(100)
wall_e.power = -100  # выполняется setter метод
print(wall_e.power)

del wall_e.power  # выполняется deleter метод
