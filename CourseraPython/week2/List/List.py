# Список - List. Изменяемая структура данных
empty_list = []
empty_list = list()

none_list = [None] * 10

user_data = [
    ["Elena", 45],
    ["Maryia", 23]
]

collections = ['list', 'tuple', 'dict', 'set']
collections[3] = 'frozenset'
# print(collections[10])  # IndexError: list index out of range
print('tuple' in collections)  # проверка нахождения элемента в списке
len(collections)  # выполняется за константное время

# можно делать срезы у списков
range_list = list(range(10))  # range_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_list[2:5])  # [2, 3, 4]
print(range_list[3:])  # [3, 4, 5, 6, 7, 8, 9]
print(range_list[::2])  # [0, 2, 4, 6, 8]
print(range_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# !!! при получении среза создаётся новый объект - получается новый список
print(id(range_list))  # 2740663428224
print(id(range_list[:]))  # 2740663405184

# списки, как и все коллекции, поддерживают протокол итерации
# итерация происходит по элементам, а не по индексам
collections = ['list', 'tuple', 'dict', 'set']
for collection in collections:
    print(collection)

# встроенная функция enumerate возвращает индекс и текущий элемент
for idx, i in enumerate(collections):
    print("index = {}, collection = {}".format(idx, i))

# тк списки - изменяемая структура данных, мы можем удалять и добавлять элементы
collections.append("OrderedDict")  # ['list', 'tuple', 'dict', 'set', 'OrderedDict']

# можно расширить список другим списком
# метод extend добавляет переданный список в конец имеющегося списка
collections.extend(["ponyset", "unicorndict"])  # ['list','tuple','dict','set','OrderedDict','ponyset','unicorndict']

# используя '+', можно добавить переменную в конец списка
collections += [None]

# для удаления элемента использовать del
del collections[4]

# есть встроенные функции для работы с листами: min, max, sum и тд
numbers = [4, 6, 7, 9, 2, 5, 11]
print(min(numbers))  # 2
print(max(numbers))  # 11
print(sum(numbers))  # 44

# метод join позволяет элементы списка преобразовать в строку с помощью разделится
tag_list = ['python', 'of', 'version', '3.10']
print(' '.join(tag_list))  # python of version 3.10