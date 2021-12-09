# Что вернется при вызове multiply(10,2)?
def stringify(func):
    print(str(func))  # <function multiply at 0x0000023E4E74A9D0>
    print(type(str(func)))  # <class 'str'>
    return str(func)


@stringify
def multiply(a, b):
    return a * b


# Случится ошибка - функция multiply после применения декоратора стала строкой, а значит ее нельзя вызывать с помощью ()
multiply(10, 2)  # TypeError: 'str' object is not callable
