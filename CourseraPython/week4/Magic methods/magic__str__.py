# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"


class User:
    # магический метод __init__ отвечает за инициализацию созданного объекта
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # магический метод __str__ отвечает за строковое представление объекта, определяет поведение, например,
    # при вызове функции print. __str__ должен определить какое-то человекочитаемое описание нашего класса,
    # которое может пользователь потом вывести в интерфейсе
    def __str__(self):
        return "{} <{}>".format(self.name, self.email)


masha = User("Masha Kastenka", "mkastenka@gmail.com")
print(masha)  # Masha Kastenka <mkastenka@gmail.com>