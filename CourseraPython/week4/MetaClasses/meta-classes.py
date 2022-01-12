# Мета-классы - классы, которые создают другие классы
# Класс type - базовый мета-класс

class Class:
    pass


obj = Class()
print(type(obj))  # <class '__main__.Class'>
print(type(Class))  # <class 'type'>, type создал наш класс. Он является мета-классом

# <class 'type'> - тип самого type является он же сам, это рекурсивное замыкание, которое реализовано с помощью С внутри
print(type(type))


# важно понимать разницу между созданием и наследованием
print(issubclass(Class, type))  # False, type создает класс Class, но Class не наследуется от него
print(issubclass(Class, object))  # True, Class наследуется от класса object

print(issubclass(object, type))  # False, type является базовым мета-классом и создает в том числе базовый класс object