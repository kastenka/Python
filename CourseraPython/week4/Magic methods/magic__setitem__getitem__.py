# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"
# Написать свой контейнер с помощь. __getitem__ и __setitem__
# __getitem__ определяет поведение объекта при доступе по индексу или ключу - obj[key]
# __setitem__ определяет поведение объекта при присваивании по индексу или ключу obj[key] = value


class City:
    def __init__(self, name_list=None):
        self.name_list = name_list or []

    def __getitem__(self, index):
        return f"This is element is {self.name_list[index]}"

    def __setitem__(self, index, value):
        self.name_list[index-1] = value


city = City(["Masha", "Veronika", "Vika"])
print(city[1])  # This is element is Veronika

city[1] = "Not element"  # при этом меняется 0 элемент, тк поведение описано в __setitem__
for el in city:
    print(el)

