import argparse
import json
import tempfile
import os


def create_args(*args):
    parser = argparse.ArgumentParser()
    for arg in args:
        parser.add_argument(arg)
    return parser.parse_args()


def create_file(file_name="storage.data"):
    storage_path = os.path.join(tempfile.gettempdir(), file_name)
    if not os.path.exists(storage_path):
        open(storage_path, "w").close()  # создание файла, если его нет
    return storage_path


def read_file(file_path):
    if os.path.getsize(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    return None


def write_file(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def add_data(key, value):
    file_path = create_file()
    data = {}
    if os.path.getsize(file_path):  # проверка, пустой ли файл (те было уже что-то добавлено или нет?)

        data = read_file(file_path)  # если файл не пустой, то читаем его данные

        if key in data:  # проверка, есть ли такой ключ
            if type(data[key]) is str:  # если по ключу найдено только одно значение(строка), делаем из строки список
                data[key] = data[key].split()
            data[key].append(value)  # добавляем к значению по ключу новое
        else:
            data[key] = value  # если ключа еще нет, то просто добавляем данные в словарь
    else:
        data[key] = value  # если файл пустой, то просто добавляем данные в словарь

    write_file(file_path, data)  # записываем данные(словарь) в файл


def get_data(key):
    file_path = create_file()
    data = read_file(file_path)

    if data and key in data:
        if type(data[key]) is str:
            print(data[key])
        else:
            print(", ".join(data[key]))
    else:
        print(None)  # возвращаем None, если нет данных с таким ключом


arguments = ["--key", "--val"]
arg_key, arg_val = create_args(*arguments).key, create_args(*arguments).val

# если введены оба параметра - добавить новое значение и записать в файл
if arg_key and arg_val:
    add_data(arg_key, arg_val)  # добавляем данные и записываем в файл
# если введен только ключ - показать значения по данному ключу
elif arg_key and not arg_val:
    get_data(arg_key)
