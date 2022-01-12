# StaticMethod и ClassMethod релизованы с помощью дескрипторов. Можем также написать свою реализацию

class StaticMethod:
    def __init__(self, func):
        self.func = func  # просто сохраняет функцию

    # когда функция вызывается, когда пытаемся получить соответствующий атрибут, мы просто ее возвращаем
    # тк это статический метод, не нужно передавать ни self, ни class
    def __get__(self, obj, obj_type=None):
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:  # когда вызываем функцию от объекта, те obj_type равен None
            obj_type = type(obj)  # передаем соответствующий obj_type первым значением

        def new_func(*args, **kwargs):
            # classmethod принимаем первым значением класс
            return self.func(obj_type, *args, **kwargs)

        return new_func