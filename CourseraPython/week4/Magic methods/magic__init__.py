# Магический метод - это метод, определенный внутри класса, который начинается и заканчивается с "__"

class User:
    # магический метод __init__ отвечает за инициализацию созданного объекта
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            "name": self.name,
            "email": self.email
        }

masha = User("Masha Kastenka", "mkastenka@gmail.com")
print(masha.get_email_data())

