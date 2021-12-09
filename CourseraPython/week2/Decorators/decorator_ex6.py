# Написать декоратор с параметром, который записывает лог в указанный файл

# есть новый декоратор, который принимет не функцию, а filename, и записывет в filename результат выполнения функции
def logger(filename):  # можно рассматривать logger не как декоратор, а как функцию, которая возвращает декоратор
    def decorator(func):  # декоратор, который принимает функцию
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "w") as file:
                file.write(str(result))
            return result
        return wrapped
    return decorator  # должен вернуть декоратор


@logger("new_log.txt")
def summator(num_list):
    return sum(num_list)


# применяется декоратор к функции summator, вызывается функция logger, которой передаем filename ->
# функция logger возвращает декоратор decorator, который применяется с помощью "@" ->
# декоратор decorator принимает функцию summator и возвращает функцию wrapped, которая подменяем функцию summator ->
# потом вызвается именно функция wrapped, внутри функции wrapped вызывается исходная функция summator и записывается
# результат выполнения в filename
# в начале вызовется logger, вернется декоратор, и потом декоратор будет применяться к функции summator
summator([1, 2, 3, 4, 5, 6])

with open("new_log.txt", "r") as f:
    print("Log file: {}".format(f.read()))


# если вызывать функцию, применяя к ней декоратор, не использую синтаксический сахар ("@")
summator = logger("new_log.txt")(summator)