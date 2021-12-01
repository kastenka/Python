# Списки. Примеры использования методов

# Метод reverse - перестраивает элементы списка в обратном порядке
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]
num_list.reverse()
print(num_list)  # [4, 3, 2, 1, 0]

# reverse модифицирует исходный объект на месте, возвращая при этом None
print(num_list.reverse())  # None

# также можно использовать num_list[::-1]
print(num_list)  # [0, 1, 2, 3, 4]
num_list = num_list[::-1]
print(num_list)  # [4, 3, 2, 1, 0]
