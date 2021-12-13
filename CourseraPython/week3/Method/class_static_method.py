# Методы. Часть 2
# Статический метод класса @staticmethod

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


# можно обращаться от имени класса
print(Human.is_age_valid(15))  # True

# можно обращаться от имени экземпляра
human = Human("Old Bobby")
print(human.is_age_valid(15))  # True
