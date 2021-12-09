# Числа Фибоначчи - нужно получить числа Фибоначчи до какого-то момента. Не нужно запоминать огромное количество чисел
# Фибоначчи, которые очень быстро растут, нам нужно помнить только два конкретных числа и возвращаться в момент, когда
# мы остановились
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)
