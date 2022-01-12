# Мета-классы - классы, которые создают другие классы
# Класс type - базовый мета-класс


# Обычно классы создаются с помощью мета-классов
# можем переопределить поведение при создании класса - добавить какой-то аттрибут или сделать что-то другое

class Meta(type):  # чтобы класс был мета-классом, он должен наследоваться от другого мета-класса
    """
    Мета-класс, который переопределяет функцию __init__
    Логирует, запоминает все созданные подклассы
    """

    # вызывается при инициализации класса
    def __init__(cls, name, bases, attrs):  # принимает название класса, его родителей и аттрибуты
        print("Initializing - {}".format(name))

        # записывает в свой атрибут значения созданных классов
        if not hasattr(cls, "registry"):
            cls.registry = {}  # создается "registry", куда будем записывать все подклассы
        else:
            # записываем в "registry" значение, когда какой-то класс наследуется от Base
            # записываем название созданного класса и ссылку на него, те объект class
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta):  # Initializing - Base
    pass


class A(Base):  # Initializing - A
    pass


class B(Base):  # Initializing - B
    pass


# Выводим все подклассы Base
print(Base.registry)  # {'a': <class '__main__.A'>, 'b': <class '__main__.B'>}
print(Base.__subclasses__())  # [<class '__main__.A'>, <class '__main__.B'>]
    