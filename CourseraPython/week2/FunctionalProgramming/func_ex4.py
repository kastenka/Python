# Списочные выражения


# создаить список - присваиваем number в список (в данном случае списачное выражение работает чуть быстрее, чем
# создавать через цикл)
square_list = [number ** 2 for number in range(10)]
print(square_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)  # [0, 2, 4, 6, 8]


# используя списочные выражения, можно определять словари
square_map = {number: number ** 2 for number in range(5)}
print(square_map)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# использую списочные выражения, можно определять множетсва
reminders_set = {num ** 2 for num in range(5)}
print(type(reminders_set))  # <class 'set'>
print(reminders_set)  # {0, 1, 4, 9, 16}


# получим генератор - объект, в котором можно итерироваться
print(type(num ** 2 for num in range(5)))  # <class 'generator'>