import random


# сортировка списка
numbers = []
for _ in range(10):  # используется '_' для итерации тк не важно, что именно присваивается при итерации
    numbers.append(random.randint(0, 10))

# использование встроенной функции sorted
print(sorted(numbers))
# возвращается новый список, старый остаётся неизменным
print(numbers)

# испольщование метода sort чтобы изменить список
numbers.sort()
print(numbers)

# отсортировать в обратном порядке, используя reverse=True
print(sorted(numbers, reverse=True))
numbers.sort(reverse=True)
print(numbers)

# встроенная функция reversed, которая возвращает reverse оператор - объект, который поддерживает проток итерации и
# можно его преобразовать в список
print(reversed(numbers))  # <list_reverseiterator object at 0x000002A861F8EFD0>
print(list(reversed(numbers)))  # [2, 2, 3, 3, 4, 4, 5, 5, 9, 10]



