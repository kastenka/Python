# Функция map принимает функцию и какой-то итерабельный объект, применяя полученную функцию к итерабельному объекту
def squarify(a):
    return  a ** 2


# передаем map функцию squarify и range
# функция map бежит по этому итерабельному объекту(по rang'у) и применяет squarify к элементу одному за другим
data = list(map(squarify, range(5)))
print(data)  # [0, 1, 4, 9, 16]

# map по-умолчанию возвращает map object, поэтому необходимо применить функцию list
data = map(squarify, range(5))
print(type(data))  # <class 'map'>
print(data)  # <map object at 0x00000138BC5EF310> - какой-то внутренний объект



