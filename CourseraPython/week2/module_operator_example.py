# Модуль operator экспортирует набор функций, соответсвующих внутренним операторам в Python
import operator


print(operator.add(4, 5))  # 9


# Так же модуль operator определяет инструменты для обобщенного поиска атрибутов и элементов
# Инструменты полезны для создания быстрых экстракторов полей в качестве аргументов для функций
# map(), sorted(), itertools.groupby() и др. функций, которые ожидают аргумент функции

# itemgetter(n) создает вызываемый объект, который принимает итеративный объект(список, кортеж и тд) в качестве
# входных данных и извлекает из него элемент n-th
operator_item = operator.itemgetter(1)("ABCDEF")
print(operator_item)  # B

dict_map = {
    1: "one", 2: "two", 3: "three",
    6: "six", 5: "five", 4: "four"
}
dict_items = dict_map.items()
print(dict_items)  # dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (6, 'six') ... )] - список tuples

# сортируем, используя operator.itemgetter(0), где 0 - это 0 элемент каждого tuple из dict_items
sorted_dict = sorted(
    dict_items, key=operator.itemgetter(0), reverse=False
)
print(sorted_dict)  # [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six')]


