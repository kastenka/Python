# Функции можно создавать внутри других функций
# Концепция замыкания - используется аргумент из скопа выше, из области видимости функции get_multiplier
def get_multiplier(number):
    # функция inner, которая будет принимать один аргумент и умножать на аргумент, который передали в get_multiplier
    def inner(a):
        return a * number
    return inner


multiplier = get_multiplier(2)  # <function get_multiplier.<locals>.inner at 0x00000245B5C5C9D0>
print(multiplier(10))  # вернет 20
