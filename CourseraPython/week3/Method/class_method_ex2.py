# Методы. Часть 1
from datetime import date


def extract_description(user_string):
    return "открытие чемпиона мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 4)


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.event_date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.event_date}"

    @classmethod  # данный декоратор делает метод методом класса, который полезен как альтернативный конструктор класса
    # первым аргументом принимает не ссылку на экземпляр класса, а принимает сам класс
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        # получив данные, можем проинициализировать класс и вернуть экземпляр класса события на основне user_input
        return cls(description, date)  # возвращаем экземпляр класса Event


event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

# создаем экземпляр класса Event, инициализируя его с помощью описания и даты
event = Event(event_description, event_date)
print(event)

new_event = Event.from_string("Добавить в календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(new_event)