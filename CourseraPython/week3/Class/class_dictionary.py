# Классы и экземпляры. Часть 2 - Словарь экземпляра и класса


class Planet:
    """This class describes planets"""
    count = 1

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")

# когда обращаемся к каким-то атрибутам, Python, в первую очередь в этот словарь, и ищет там эти атрибуты
print(planet.__dict__)  # словарь, у которого есть атрибуты нашего класса

# если добавляем атрибут экземпляру нашего класса, то в словаре экземпляра класса появляется этот атрибут
# соответствнно, когда мы пытаемся получить к нему доступ, Python смотрит в словаре и выдает значение
planet.mass = 5.97e24
print(planet.__dict__)  # {'name': 'Earth', 'population': [], 'mass': 5.97e+24}

# словарь атрибутов есть и у самого класса
print(Planet.__dict__)  # <class 'mappingproxy'>

# если обратимся к свойству __doc__, то свойство будет найдено в этом словаре и Python вернет его значение
print(Planet.__doc__)  # вернет docstring

print(dir(planet))  # увидим методы экземпляра класса

# получим класс, к которому принадлежит экземпляр, используя свойство __class__
print(planet.__class__)  # <class '__main__.Planet'>