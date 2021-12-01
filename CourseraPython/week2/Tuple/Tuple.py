# Кортежи - Tuple. Неизменяемая структура данных - нельзя добавлять, удалять элементы
# Кортежи эффективнее по скорости работы и занимаемой памяти, тк кортежи неизменяемы, не нужно думать о том, что надо
# меняться, поэтому занимают меньше места и часто их работа может быть оптимизирована интерпретатором.

empty_tuple = ()
empty_tuple = tuple()

immutables = (int, str, tuple)
# immutables[0] = float  # TypeError: 'tuple' object does not support item assignment

# Объекты внутри кортежей изменяемы
list_tuple = ([1], [1])
list_tuple[0][0] = 0
print(list_tuple)  # ([0], [1])

# У кортежей есть функция hash - могут использоваться в качестве ключей в словарях
print(hash(tuple()))  # 5740354900026072187


# необходимо писать запятую при определии кортежа из одного элемента
test_tuple = (1, )
print(type(test_tuple))  # <class 'tuple'>

test_tuple = (1)
print(type(test_tuple))  # <class 'int'>
