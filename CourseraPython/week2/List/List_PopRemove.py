# Списки. Примеры использования методов

# Метод pop - возвращает элемент (на указанной позиции), удаляя его из списка
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]

print(num_list.pop(1))  # 1
print(num_list)  # [0, 2, 3, 4]


# если позиция не указана, то удаляется последний элемент списка
print(num_list.pop())  # 4
print(num_list)  # [0, 2, 3]

# Метод remove - удаляет элемент из списка, не возвращая его
num_list = list(range(5))  # [0, 1, 2, 3, 4]
num_list.remove(0)
print(num_list)  # [1, 2, 3, 4]

print(num_list.remove(1))  # None









