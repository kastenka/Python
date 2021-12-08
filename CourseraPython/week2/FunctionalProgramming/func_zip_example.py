# Функция zip - позволяет склеить 2 итерабельных объекта

num_list = range(7)
squared_list = [x ** 2 for x in num_list]
data = list(zip(num_list, squared_list))  # первый элемент 1-го списка с первым элементом 2-го списка в одном tuple
print(data)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]