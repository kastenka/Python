# Анонимные функции или lambda-функции
# часто бывает необходимо определить какую-то функцию, но нам не нужно применять её в дальнейшем
# lambda позволяет определить функцию на месте in-place, без литерала def
data = list(map(lambda x: x ** 2, range(5)))  # анонимная фукция принимает один параметр x и возводит его в квадрат
print(data)  # [0, 1, 4, 9, 16]

print(type(lambda x: x ** 2))  # <class 'function'>


data = list(filter(lambda x: x > 0, range(-2, 3)))
print(data)  # [1, 2]

