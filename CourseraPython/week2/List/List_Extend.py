# Списки. Примеры использования методов

# Метод extend - дополняет список элементами из указанного объекта, добавляет их в конец списка
num_list = list(range(5))
another_list = list(range(5, 10))
num_list.extend(another_list)
print(num_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

str_list = ["a", "b", "c"]
str_to_add = "efd"
str_list.extend(str_to_add)
print(str_list)  # ['a', 'b', 'c', 'e', 'f', 'd']

# Метод extend модифицирует объект на месте, возвращая None
print(str_list.extend("New"))  # None





