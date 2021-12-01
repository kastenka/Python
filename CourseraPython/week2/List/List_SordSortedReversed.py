import random


# сортировка списка
numbers = []
for _ in range(10):  # используется '_' для итерации тк не важно, что именно присваивается при итерации
    numbers.append(random.randint(0, 10))

# использование встроенной функции sorted
print(sorted(numbers))   # [2, 2, 3, 7, 7, 8, 9, 10, 10, 10]
# возвращается новый список, старый остаётся неизменным
print(numbers)  # [10, 8, 2, 7, 9, 10, 3, 7, 2, 10]

# использование метода sort, чтобы изменить список
numbers.sort()
print(numbers)  # [2, 2, 3, 7, 7, 8, 9, 10, 10, 10]

# отсортировать в обратном порядке, используя reverse=True
print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)  # [10, 10, 10, 9, 8, 7, 7, 3, 2, 2]

# встроенная функция reversed, которая возвращает reverse оператор - объект, который поддерживает проток итерации и
# можно его преобразовать в список
print(reversed(numbers))  # <list_reverseiterator object at 0x000002A861F8EFD0>
print(list(reversed(numbers)))  # [2, 2, 3, 3, 4, 4, 5, 5, 9, 10]
