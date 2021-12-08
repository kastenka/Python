# Написать функцию, которая превращает список чисел в список строк
def to_string(num_list):
    str_list = []
    for el in num_list:
        str_list.append(str(el))
    return str_list


def to_string2(num_list):
    return list(map(str, num_list))


numbers = [1, 2, 3, 5, 6]
# Variant 1
output = to_string(numbers)
print(output)  # ['1', '2', '3', '5', '6']

# Variant 2
output = to_string2(numbers)
print(output)  # ['1', '2', '3', '5', '6']
