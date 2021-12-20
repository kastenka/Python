# Итератор - какой-то объект, по которому вы можете бежать, те итерироваться
# Можно реализовать свой собственный итератор, не определяя __iter__ и __next__, но написан при этом у класса метод
# __getitem__, который определяет работу класса при обращении к его объектам с помощью "[]", те как к контейнеру
# такой способ используется редко

class IndexIterable:
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


for letter in IndexIterable("string"):
    print(letter)