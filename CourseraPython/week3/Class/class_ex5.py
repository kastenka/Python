# Классы и экземпляры. Часть 1
# Работа с атрибутами экземпляра


class Planet:
    def __init__(self, name):
        self.name = name  # ставим атрибут экземпляра name и присваиваем его аргументу name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"


mars = Planet("Mars")
print(mars)

# когда создаем экземпляр класса Planet, можем обратиться к атрибуту через точку, например mars.name
print(mars.name)  # Mars

# мы можем в любой момент изменить атрибут экземпляра, присвоив ему другое значение
mars.name = "Second Earth?"
print(mars.name)  # Second Earth?

# если обратимся к несуществующему атрибуту экземпляра, то вызовется ошибка AttributeError
# print(mars.mass)  # AttributeError: 'Planet' object has no attribute 'mass'

# если удалим какой-то атрибут экземпляра,используя del, то обратившись к mars.name, получим AttributeError
del mars.name
print(mars.name)  # AttributeError: 'Planet' object has no attribute 'name'
