# Python позволяет переопределять поведение при доступе к атрибуту. Это механизм, который позволяет незаметно от
# от пользователя определять различные поведения в наших классах
# С помощью дескрипторов реализована вся "магия" при работе с объектами, классами, методами
# Чтобы определить свой собственный дескриптор, нужно определить класс, задать методы __get__, __set__ или __delete__
# Можно переопределить один из 3-х методов и класс уже будет являться дескриптором
# Зависит от того, в каком порядке они будут вызываться при поиске атрибутов
# Если переопределен только метод __get__, то это non-data дескриптор
# Если переопределен метод __set__ или __delete__, то это data дескриптор


class Value:
    """Дескриптор Value, который переопределяет поведение, при присваивании значения в него"""
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class:
    attr = Value()  # атрибут, который является дескриптором


instance = Class()
instance.attr = 10  # при присвании значения в дескриптор, будет модифицированное поведение


print(instance.attr)  # 100