myStr = 'String'

# find - поиск подстроки
print(myStr.find('ring'))  # Вовращает смещение подстроки
print(myStr.find('ringg'))  # Возвращает -1, тк такой подстроки нет

# replace - глобальный поиск и замена подстроки
print(myStr.replace('ring', 'RING'))

# split - разбить строку по разделителю в список подстрок
str1 = 'aa,bb,cc,dd'
print(f'{str1}   -   Type: {type(str1)}') # тип - строка (str)
str1 = str1.split(',')  # разибение строки
print(f'{str1}   -   Type: {type(str1)}')  # тип - список (list)
str1 = ''.join(str1)  # объединение с пустым разделителем в строку
print(f'{str1}   -   Type: {type(str1)}')  # тип - строка (str)

# upper, lower - преобразовать в верхний/нижний регистр
str2 = 'first'
str3 = 'SECOND'
str2 = str2.upper()  # преобразование в вернхний регистр
print(f'{str2}')
str3 = str3.lower()  # преобразование в нижний регистр
print(f'{str3}')

# isalpha - возвращает флаг, указывающий на то, содержит ли строка только буквы
# другие методы для проверки содержимого: isalnum, isdigit ...
str1 = 'pa1'
str2 = 'pal'
str3 = '2324'
print(f'Is str1 include only letters?: {str1.isalpha()}')  # False
print(f'Is str2 include only letters?: {str2.isalpha()}')  # True
print(f'Is str2 include only letters?: {str3.isdigit()}')  # True

# rstrip - удалить пробельные символы с правой стороны
str1 = '123  '
str1 = str1.rstrip()  # удаляет пробелы справа
print(f'str: {str1} and it\'s length = {len(str1)}')

