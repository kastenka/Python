# Списки. Примеры использования методов
# Метод clear - удаляет из списка все имеющиеся значения
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]
num_list.clear()
print(num_list)  # []


# метод clear возвращает None
print(num_list.clear())  # None

# другой способ удалить из списка все элементы
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]
del num_list[:]
print(num_list)  # []

