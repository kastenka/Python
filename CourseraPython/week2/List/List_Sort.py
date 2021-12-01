# Списки. Примеры использования методов
# Метод sort - сортирует элементы списка на месте (in place)
num_list = [1, 6, 8, 3, 9, 2, 3, 10]

# флаг reverse указывает, нужно ли производить сортировку в обратном порядке
num_list.sort(reverse=True)
print(num_list)  # [10, 9, 8, 6, 3, 3, 2, 1]

num_list.sort(reverse=False)
print(num_list)  # [1, 2, 3, 3, 6, 8, 9, 10]

# метод sort возвращает None
print(num_list.sort())  # None

# попытка сравнить разные типы в списке
diff_list = [1, '4', 'd', 12]
# diff_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

# сортировка вручную, чтобы определенный элемент был в конце
another_list = [1, '4', 'd', 54, 9, 4, 'd', 'a', 12]
another_list.sort(key=lambda val: val == 'd')
print(another_list)  # [1, '4', 54, 9, 4, 'a', 12, 'd', 'd']
