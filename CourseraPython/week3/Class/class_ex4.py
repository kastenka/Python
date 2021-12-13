# Классы и экземпляры. Часть 1

class Planet:
    def __init__(self, name):
        self.name = name  # ставим атрибут экземпляра name и присваиваем его аргументу name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"


solar_system = []
planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

# переопределили __str__, но внутри списка видим объекты, которые печатаются в представлении, которое печаталось до
# определения __str__  -  тк в данном случае Python использует другой магический метод, когда мы внутри списка, те
# встроенный, другой магический метод - метод __repr__, который мы имеем возможность также переопределить, чтобы и
# внутренее представление объекта также печаталось в данном случае
print(solar_system)  # [<__main__.Planet object at 0x000002847166FFA0> ... - до переопределения метода __repr__

print(solar_system)  # [Planet Mercury ... - после переопределения метода __repr__