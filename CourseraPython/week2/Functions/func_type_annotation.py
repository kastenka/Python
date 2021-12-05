# не нужно указывать какие параметры(их типы) функция ожидает тк Python - динамический язык

# есть возможность сделать аннотацию типов - явно указать параметры
def add(x: int, y: int) -> int:
    return x + y


print(add(5, 6))  # вернет значение 11

# если передадим параметры других типов, то код все равно исполнится, тк Python - динамический язык
# аннотация типов призвана помочь программисту отловить какие-то ошибки
print(add("one string ", "plus another string"))  # one string plus another string