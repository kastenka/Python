# Классы и экземпляры. Часть 2 - Атрибуты класса
class Planet:

    # нужно быть осторожным при использовании атрибутов класса - может возникнуть путаница
    count = 0  # атрибут класса

    def __init__(self, name, population=None):
        self.name = name
        population = population or []
        Planet.count += 1


# создаем 2 экземпляра класса Planet
earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
# можем обратиться к атрибуту класса через экземпляр класса и также получим его значение - в этот момент Python видит,
# что внутри экземпляра класса такого атрибута нет, и он проверяет сам класс на наличие атрибута класса
print(mars.count)
