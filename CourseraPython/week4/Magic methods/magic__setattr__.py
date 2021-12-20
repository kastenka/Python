# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"
# Магический метод __setattr__ определяет поведение при присваивании значения к атрибуту


class Ignorant:
    def __setattr__(self, name, value):
        # например, вместо того, чтобы присвоить значение, мы можем вернуть какую-то строку и ничего не делать
        print("Not gonna set {}!".format(name))


obj = Ignorant()

# если попытаемся присвоить значение атрибуту, то ничего не произойдет и атрибут не создасться
obj.math = True  # Not gonna set math!
print(obj.math)  # AttributeError: 'Ignorant' object has no attribute 'math'



