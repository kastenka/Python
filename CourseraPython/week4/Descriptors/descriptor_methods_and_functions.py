# Функции и методы реализованы с помощью дескрипторов
# Чтобы это понять, можно попробовать обратиться к одному и тому же методу с помощью объекта и с помощью класса


class Class:
    def method(self):
        pass


obj = Class()

# Один и тот же метод возвращает разные объекты в зависимости от того, как к нему обращаются - поведение дескриптора

# окажется, что когда обращаемся к методу через точку от объекта, у нас возвращается bound method, те это метод,
# привязанный уже к какому-то объекту, в данном случае object
print(obj.method)  # <bound method Class.method of <__main__.Class object at 0x0000019B0D1A1E20>>

# если обращаемся к методу от класса, то это unbound method, это просто функция
print(Class.method)  # <function Class.method at 0x0000019B0D04B9D0>


# !!! Чем отличается bound и unbound методы?
# В bound метод по умолчанию передается объект, с которым вызван метод