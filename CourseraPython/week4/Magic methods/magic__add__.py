# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"
# Магический метод __add__ - оператор сложения
import random


class NoisyInt:
    def __init__(self, value):
        self.value = value

    # магический метод __add__ определяет поведение при сложении двух объектов
    def __add__(self, obj):
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise


a = NoisyInt(10)
b = NoisyInt(20)
print(a+b)