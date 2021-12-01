# Словари - Dictionary. Изменяемая структура данных. Хранят данные в формате ключ - значение
# Позволяют получить значение по ключу за константное время - достигается с помощью алгоритма хеширования (быстрая
# проверка на вхождение ключа в словарь, быстрый доступ к значению по ключу)

# Словари содержат ключи и значения в неупорядоченном виде - нельзя гарантировать, что ключи отсортированы и хранятся
# в том порядке, в котором вы их добавили
empty_dict = {}
empty_dict = dict()

collections = {
    "mutable": ["list", "set", "dict"],
    "immutable": ["tuple", "frozenset"]
}
print(collections["immutable"])  # ['tuple', 'frozenset']

# если пытаемся вывести значение по ключу, которого нет, то будет ошибка KeyError
# print(collections["unknown"])  # KeyError: 'unknown'

# можно попытаться взять значение по ключу(даже если такого нет) и в случае неудачи вернуть какое-то дефолтное значение
print(collections.get("unknown", "not found"))  # not found

# проверить, есть ли ключ в словаре
print("mutable" in collections)  # True


# тк словарь - изменяемая структура данных, можно добавлять и удалять элементы из него
collection_map = {
    1: "one",
    2: "two",
    4: "four"
}
print(collection_map)  # {1: 'one', 2: 'two', 4: 'four'}

# добавление элемента по ключу
collection_map[3] = "three"
print(collection_map)  # {1: 'one', 2: 'two', 4: 'four', 3: 'three'}
# Добавление элемента в словарь с помощью update. Обновляет имеющийся словарь. Возвращает None
collection_map.update({
    5: "five"
})
print(collection_map)  # {1: 'one', 2: 'two', 4: 'four', 3: 'three', 5: 'five'}

# удаление элемента из словаря по ключу
del collection_map[4]
print(collection_map)  # {1: 'one', 2: 'two', 3: 'three'}
# удаление из словаря с помощью pop
print(collection_map.pop(5))  # удаляет элемент по ключу и возвращает значение "five"
print(collection_map)  # {1: 'one', 2: 'two', 3: 'three'}


# метод setdefault - проверить, существует ключ в словаре, и в случае неудачи добавить эту пару ключ-значение
unknown_dict = {}
print(unknown_dict.setdefault('key', 'default'))  # если нет такого ключа, то добавляет пару и возвращает default
print(unknown_dict)  # {'key': 'default'}


# Словари, как и все коллекции, поддерживают протокол итерации - поэтому можно итерироваться по словарю
# итерация по ключам словаря
print(collection_map)  # {1: 'one', 2: 'two', 3: 'three'}
for key in collection_map:
    print(key)  # выводит ключи коллекции: 1, 2, 3

# Метод items - для вывода и ключа и значения словаря
for key, value in collection_map.items():
    print("Key: {} and value: {}".format(key, value))

# Метод values - для итерации только по значениям
for value in collection_map.values():
    print(value)  # возвращает значения

# Метод keys - для итерации только по ключам
for key in collection_map.keys():
    print(key)  # возвращает ключи



