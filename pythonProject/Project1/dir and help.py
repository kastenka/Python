# dir - получение доп. деталей
print(dir())  # Вывод списка переменых, присвоенных в области видимости вызывающего объекта (вызов без аргумента)

str1 = 'string'
print(dir(str1))  # Список атрибутов, доступныех для переданного объекта

# help - узнать, что делает метод
print(help(str1.find))  # Показывает, что делает метод find для строки
print(help(list.copy))  # Показывает, что делает метод copy для списка


