import requests
from pprint import pprint  # для удобного отображения данных в json


def get_location():
    # с помощью get получаем данные с сайта
    # с помощью json преобразовываем полученный текст в формате json во внутреннее представление Python (в словарь)
    return requests.get("http://ip-api.com/json/").json()


if __name__ == "__main__":  # чтобы работало только когда запускает интерпретатор Python
    pprint(get_location())
    print("My city is", get_location()["city"])  # получаем значение по ключу
    