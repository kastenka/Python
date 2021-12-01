# Списки. Примеры использования методов

# Метод insert - добавляет указанный элемент в список на указанную позицию
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]

num_list.insert(1, 11)
print(num_list)  # [0, 11, 1, 2, 3, 4]


# модифицирует на месте и возвращает None
print(num_list.insert(0, 00))  # None








