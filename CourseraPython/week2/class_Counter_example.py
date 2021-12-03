# Collections - встроенный модуль Python, реализующий специализированный контейнер типов данных
# Модуль collections - альтернатива встроенных типов


# Counter - подкласс dict, который используется для подсчета объектов hashable
# Элементы хранятся в качестве ключей словаря, количество объектов - значение словаря
from collections import Counter

# со строками (так же сразу сортирует по значению, от большего к меньшему)
count_items = Counter("ABCDEBCDDADCAB")
print(count_items)

# со списками
count_items = Counter([1, 2, 4, 6, 7, 3, 2, 6, 9, 1, 1, 1, 2, 6])
print(count_items)  # Counter({1: 4, 2: 3, 6: 3, 4: 1, 7: 1, 3: 1, 9: 1})

# с предложениями
s = "masha kastenka wrote that her name is masha kastenka"
words = s.split()
print(words)  # ['masha', 'kastenka', 'wrote', 'that', 'her', 'name', 'is', 'masha', 'kastenka']
words_items = Counter(words)
print(words_items)  # Counter({'masha': 2, 'kastenka': 2, 'wrote': 1, 'that': 1, 'her': 1, 'name': 1, 'is': 1})

# вернуть 2 самых популярных ключа (по значению)
print(words_items.most_common(2))  # [('masha', 2), ('kastenka', 2)]
