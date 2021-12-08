# Пример
data = list(zip(
    filter(bool, range(3)),
    [x for x in range(3) if x]
))
print(data)  # [(1, 1), (2, 2)]


# Разбор
filter_data = list(filter(bool, range(3)))
print(list(filter_data))  # [1, 2]

x_list = [x for x in range(3) if x]
print(x_list)  # [1, 2]

zip_data = zip(filter_data, x_list)
print(list(zip_data))  # [(1, 1), (2, 2)]