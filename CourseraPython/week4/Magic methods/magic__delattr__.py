# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"
# Магический метод __delattr__ управляет поведением, когда мы пытаемся удалить какой-то атрибут объекта

class Polite:
    # можем не удалять, а, например, переопределить как-то поведение или добавить функциональность, например, если
    # хотим каскадно удалить объекты связанные с нашим классом
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f"Goodbye {name}, you were {value}")  # логируем, что происходит удаление

        object.__delattr__(self, name)  # продолжаем удаление с помощью класса object


obj = Polite()

obj.attr = 10
del obj.attr  # Goodbye attr, you were 10