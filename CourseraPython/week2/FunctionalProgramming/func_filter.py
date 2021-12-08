# Функция filter позволяет фильтровать по какому-то предикату итерабельный объект: те есть какое-то условие, в данном
# случае - это функция, которая принимает число и проверяет, что число больше нуля, и возвращает true в этом случае
def is_positive(a):
    return a > 0


def find_element(num_str):
    return num_str in "ABCD"


# filter принимает функцию и фильтрует все аргументы внутри итерабельного объекта по этому предикату
# filter возвращает filter object
print(list(filter(is_positive, range(-2, 3))))  # [1, 2]

print(list(filter(find_element, ["ab", "A", "BCD", "AD", "Ab"])))  # ['A', 'BCD']

