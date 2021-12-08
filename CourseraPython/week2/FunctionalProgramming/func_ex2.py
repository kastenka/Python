# Функции можно создавать внутри других функций
# определяем функцию get_multiplier, которая возвращает другую функцию inner
def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


multiplier = get_multiplier()
print(multiplier(10, 2))


print(multiplier.__name__)  # функция inner