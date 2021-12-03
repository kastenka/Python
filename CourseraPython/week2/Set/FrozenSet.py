# Множества - Frozenset - аналог Set - неизменяемое множество (нельзя добавлять и удалять элементы)
# Гарантирует уникальность элементов

frozen_set = frozenset([1, 2, 3, 4, 1, 1])
print(type(frozen_set))  # <class 'frozenset'>
print(frozen_set)  # frozenset({1, 2, 3, 4})

