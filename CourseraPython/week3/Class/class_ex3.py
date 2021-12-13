# Классы и экземпляры. Часть 1
# Моделирование создания Солнечной системы с помощью списков и класса

class Planet:
    pass


solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)
print(solar_system)  # список из 8 объектов Planet


solar_system = {}
for i in range(8):
    planet = Planet()
    solar_system[planet]  = True
print(solar_system)  # словарь, где ключи - объекты Planet
