# Классы и экземпляры. Часть 1

class Planet:
    def __init__(self, name):
        self.name = name  # ставим атрибут экземпляра name и присваиваем его аргументу name

    # метод __str__ переопределяет то, как будет печататься объект
    def __str__(self):
        return self.name


earth = Planet("Earth")
print(earth.name)  # обращение к имени планеты, а точнее к атребуту экземпляра
print(earth)  # печатаем имя Earth, тк был переопределен метод __str__