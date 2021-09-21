# Подстановка строк - форматирование в форме выражения и вызова строкового метода
# Все версии
print('%s - first argument' % 'ARG1')  # если 1 аргумент
print('%s - string and %d - number' % ('STR1', 123))  # если много значений, то кортеж со строками подстановки
print('s, eggs, and %s')

# Версии 2.6+, 3.0+
print('{0} - first arg, {1} - second arg'.format('1111', 'NewArg'))

# Версии 2.7+, 3.1+
print('{} - first arg, {} - second arg'.format('0000', 'NewArg2'))  # номера необязательных

# Версии 3.6+
str1 = 'str3.6+'
print(f'str1= {str1}')  # str1=str3.6+

# Версии 3.8+
print(f'{str1=}')  # str1='str3.6+'



