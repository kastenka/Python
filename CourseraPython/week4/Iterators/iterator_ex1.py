# Итератор - какой-то объект, по которому вы можете бежать, те итерироваться
# функция range и цикл for позволяет бежать по какому-то итератору и, например, выводить все числа

# можно создать свой простейший итератор с помощью встроенной функции iter
iterator = iter([1, 2, 3])
print(type(iterator))  # <class 'list_iterator'>

# каждый раз, когда мы хотим получить элемент вызывается функция next, которая возвращает следующий элемент
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# когда элементы исчерпаны, те итератор закончился, выбрасывается исключение StopIteration, которое говорит о том, что,
# например, нужно выйти из цикла for
print(next(iterator))