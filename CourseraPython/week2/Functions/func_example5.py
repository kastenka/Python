# Область видимости
# переменные, объявляенные вне области видимости функции(объекты из глобальной области видимости), нельзя изменять

# глобальная переменная result
result = 0

# внутри функции пытаемся к глобальной переменной прибавить значение
def increment():
    result += 1
    return result

print(increment())  # UnboundLocalError: local variable 'result' referenced before assignment

# !!! существует возможность изменять глобальные переменные с помощью global, например, или non local !!!
