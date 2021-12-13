# Методы. Часть 1 - Работа с методами экземпляра
# Методы это - просто функции, которые действуют в контексте экземпляра класса - таким образом, тк они действуют в
# контектсе экземпляра класса и получают ссылку на экземпляр класса, они могут менять его состояние, обращаясь к
# атрибутам экземпляра или делать что-либо другое

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []  # содержит людей, которые есть на планете

    # объявление метода - является методом экземпляра, это просто функция, которая принимает
    # 1-ым аргументом self - ссылка на экземпляр класса, 2-ым аргументом - все что захотим
    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


# создаем экземпляры классов
mars = Planet("Mars")
human = Human("Masha Kastenka")

print(mars.population)  # []
mars.add_human(human)  # Welcome to Mars, Masha Kastenka!
print(mars.population)  # [<__main__.Human object at 0x0000022DA1CB7F10>]  -  population обновилось


