"""Чаще всего декораторы используются, чтобы модифицировать поведение каких-то функций. Часто бывает необходимо
использовать один декоратор, чтобы какое-то семейство функций переопредилить, модифицировать их поведение. Например,
может быть декоратор login_required, который можем применять к разным функциям, и можем требовать, чтобы в момент
исполнения данной функции человек был залогинин на сайте и тд.
Написав один декоратор, мы можем модифицировать поведение сразу многих функций - полезный и мощный консепт."""


# Написать декоратор, который записывает в лог результат декорируемой функции - при вызове функции summator результат
# выполнения записать в лог-файл. Можем данный декоратор применять к любой функции и всегда результат выполнения будет
# записываться в файл вне зависимости от того, какая это функция.
def logger(func):
    # обычно функции, которые определены внутри декоратора, называются wrapped, decorated, inner - чтобы понять,
    # что это действительно то новое, чем мы переопределяем изначальную функцию

    # wrapped принимает num_list, получает результат работы summator, записывает в файл результат и возвращается
    def wrapped(num_list):
        result = func(num_list)
        with open("log.txt", "w") as f:
            f.write(str(result))
        return result  # возвращаем result, чтобы все работало(чтобы вызвалась функция и вернулось ее значение)
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


# применяя декоратор, подменяем функцию summator новой функцией wrapped и именно функция wrapped уже будет выполняться
num_sum = summator([1, 2, 3, 4, 5])
print(num_sum)

with open("log.txt", "r") as f:
    data = f.read()
    print("Out text file is: " + data)